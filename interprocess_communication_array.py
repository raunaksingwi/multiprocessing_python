from multiprocessing import Process, Array


def calculate_square(numbers, results):
    for index,number in enumerate(numbers):
        results[index] = number**2


if __name__ == '__main__':
    results = Array('i', 3)
    numbers = [1, 2, 3]
    calculate_process = Process(target=calculate_square, args=(numbers, results))
    calculate_process.start()
    calculate_process.join()
    print(results[:])
