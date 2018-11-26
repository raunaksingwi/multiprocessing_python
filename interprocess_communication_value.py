from multiprocessing import Process, Value


def update_value(value_object):
    value_object.value = value_object.value**3


if __name__ == '__main__':
    value_object = Value('i', 3)
    update_value_process = Process(target=update_value, args=(value_object,))
    update_value_process.start()
    update_value_process.join()
    print(value_object.value)