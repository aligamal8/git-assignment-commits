import threading
import time

semaphore = threading.Semaphore(2)

def access_resource(thread_number):
    print(f"Thread {thread_number} is waiting...")
    semaphore.acquire()
    print(f"Thread {thread_number} GRANTED access!")
    time.sleep(2)
    print(f"Thread {thread_number} releasing...")
    semaphore.release()

for i in range(5):
    t = threading.Thread(target=access_resource, args=(i,))
    t.start()
