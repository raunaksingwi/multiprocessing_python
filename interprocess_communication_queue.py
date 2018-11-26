from multiprocessing import Process, Queue


def calculate_square(numbers, queue):
    for number in numbers:
        queue.put(number**2)


if __name__ == '__main__':
    queue = Queue()
    numbers = [n for n in range(1, 15)]
    calculate_square_process = Process(target=calculate_square, args=(numbers, queue))
    calculate_square_process.start()
    calculate_square_process.join()
    queue.get()
    queue.get()