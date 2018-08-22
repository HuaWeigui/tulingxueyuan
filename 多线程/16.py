import threading
import time

semaphore = threading.Semaphore(3)

def func():
    if semaphore.acquire():
        for i in range(5):
            print(threading.currentThread().getName() +' get semaphore')
        time.sleep(3)
        semaphore.release()
        print(threading.currentThread().getName() +' release semaphore')
for i in range(8):
    t1 = threading.Thread(target=func)
    t1.start()