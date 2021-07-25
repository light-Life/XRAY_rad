import os
import time
import threading

def asd():
    for i in range(100):
        os.system("echo 1")
def zxc():
    for i in range(100):
        os.system("echo 2")

if __name__ == "__main__":
    t = threading.Thread(target=asd)
    t1 = threading.Thread(target=zxc)
    t.start()
    t1.start()
    t1.join()
    t.join()