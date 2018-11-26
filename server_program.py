from multiprocessing import Process
import os
from time import sleep


def tell_count():
    print()
    print("I am child process and my PID is :",os.getpid())
    sleep(4)
    print("child process still running....")
    sleep(4)
    print("child process still running....")
    sleep(4)
    print("child process still running....")
    sleep(14)
    print("Child process of the server terminated now.")

def main():
    print("I am main process and my PID is :", os.getpid())
    print()
    p = Process(target=tell_count)
    p.start()
    print("Main process of the server terminated.", str(p.pid))
    print()
    return 1


if __name__ == '__main__':
    main()
