import random
import time

def InsertionSort(array,size):
    for p in range(size):
        current_element = array[p]

        while p > 0 and array[p - 1] > current_element:
            array[p] = array[p - 1]
            p -= 1

        array[p] = current_element
    #print(array)

ini = time.time()
size = 20000
array = list(range(0,size))

random.shuffle(array)
#print(array)
InsertionSort(array,size)
fim = time.time()
exec = fim - ini
print(exec)
