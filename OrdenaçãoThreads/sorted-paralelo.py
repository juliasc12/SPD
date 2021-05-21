import random
import threading
import time

def Vetor(vet,tam,thread_num):
    vetOrdenado1 = []
    ofc=[]

    if(thread_num==0): #preenche
        for i in range(tam):
            num = int(random.randint(0,9))
            vet.append(num)

    if(thread_num==1): #ordena
        for i in range(tam):
            y = vet[i]
            vetOrdenado1.append(y)
            ofc = sorted(vetOrdenado1)

def threads():
    vet = []
    tam = 80000
    threads=[]
    qtdThreads =  2
    for i in range(qtdThreads):
        t = threading.Thread(target=Vetor, args=(vet,tam,i,))
        threads.append(t)
        t.start()

    for i in threads:
        i.join()

def main():
    ini = time.time()
    threads()
    fim = time.time()

    exec = fim - ini
    print("\nTempo de inicialização: "+str(ini)+"\nTempo de Finizalização: "+str(fim) + "\nTempo de Execução: "+ str(exec))

main()
