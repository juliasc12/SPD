import random
import threading
import time

def preencheVetor(vet,tam):
    for i in range(tam):
        num = int(random.randint(0,9))
        vet.append(num)
    #print("\nVetor: "+ str(vet)+"\n")

def somaVetor(vet,tam,thread_num):
    soma1=0;soma2=0
    metade = 10
    print("Iniciando thread: " + str(thread_num))

    for i in range(metade):
        soma1+=vet[i]

    if(thread_num == 1):
        for metade in range(20):
            soma2+=vet[metade]
            #print("Elemento: "+ str(vet[metade]))
        print(soma1)
        print(soma2)
        SomaTotal = soma1+soma2
        print("Soma total: "+str(SomaTotal))

    #time.sleep(5)
    print("Thread: "+ str(thread_num)+" saindo")


def threads(vet,tam):
    threads=[]
    qtdThreads =  2

    for i in range(qtdThreads):
        t = threading.Thread(target=somaVetor, args=(vet,tam,i,))
        threads.append(t)
        t.start()

    for i in threads:
        i.join()


def main():
    tam = 2000000
    vet = []
    preencheVetor(vet,tam)

    ini = time.time()
    threads(vet,tam)
    fim = time.time()
    exec = fim - ini
    print("\nTempo de inicialização: "+str(ini)+"\nTempo de Finizalização: "+str(fim) + "\nTempo de Execução: "+ str(exec))




main()
