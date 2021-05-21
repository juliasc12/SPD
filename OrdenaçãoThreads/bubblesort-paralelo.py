import random
import time
import threading

def Vetor(vet,tam,thread_num):

    if(thread_num == 0):
        for i in range(tam):
            num = int(random.randint(0,9))
            vet.append(num)
        #print("vetor preenchido: " + str(vet))

    if(thread_num == 1):
        for tam in range(tam, 0, -1):
            trocou = False
            atual=0; prox=1
            for atual in range(0, tam-1):
                prox=atual+1
                if (vet[atual] > vet[prox]):
                    vet[prox], vet[atual] = vet[atual], vet[prox]
                    trocou = True
        #print("vetor ordenado: " + str(vet))

def threads():
    vet = []
    tam = 20000
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
