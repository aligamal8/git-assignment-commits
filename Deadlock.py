import threading
import time

lock1 = threading.Lock()
lock2 = threading.Lock()

def thread_1():
    print("Thread 1: Acquire Lock 1")
    lock1.acquire()
    time.sleep(1)
    print("Thread 1: Waiting for Lock 2...")
    lock2.acquire()
    print("Thread 1: Acquired Lock 2")

def thread_2():
    print("Thread 2: Acquire Lock 2")
    lock2.acquire()
    time.sleep(1)
    print("Thread 2: Waiting for Lock 1...")
    lock1.acquire()
    print("Thread 2: Acquired Lock 1")

t1 = threading.Thread(target=thread_1)
t2 = threading.Thread(target=thread_2)

t1.start()
t2.start()
