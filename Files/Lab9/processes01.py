import multiprocessing as mp
import time
import os

index = 0

class MyProcess(mp.Process):

    # metoda uruchamiana w momencie gdy uruchamiamy nowy proces
    def run(self):
        index = 0

        while(True):
            print(f'Hello from process! {os.getpid()}')
            time.sleep(1)
            index = index * index

if __name__ == '__main__':

    p1 = MyProcess()
    p1.start()
    p2 = MyProcess()
    p2.start()


    index = 0
    while(True):
        print(f'Hello from main! {os.getpid()}')
        time.sleep(1)
        index = index * index