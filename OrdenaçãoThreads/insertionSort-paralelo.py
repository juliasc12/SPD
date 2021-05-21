import random
import time
import threading

array1 = []
array2 = []

def ControllingThread(array,size,half,thread_num):
    if(thread_num == 0):
        for i in range(size):
            x = array[i]

            if(x < half):
                array1.append(x)

            if(x >= half):
                array2.append(x)

    if(thread_num == 1):
        InsertionSort(array1)

    if(thread_num == 2):
        InsertionSort(array2)

def InsertionSort(array):
    for p in range(len(array)):
        current_element = array[p]

        while p > 0 and array[p - 1] > current_element:
            array[p] = array[p - 1]
            p -= 1

        array[p] = current_element
    print(array)

def Threads():
    size = 20
    array = list(range(0,size))
    random.shuffle(array)
    print(array)
    half = int(size/2)
    threads=[]
    using =  3

    for i in range(using):
        t = threading.Thread(target=ControllingThread, args=(array,size,half,i,))
        threads.append(t)
        t.start()

    for i in threads:
        i.join()

ini = time.time()
Threads()
fim = time.time()
exec = fim - ini
print(exec)
