import random
import threading
import time

def preencheVetor(vet,tam):
    for i in range(tam):
        num = int(random.randint(0,9))
        vet.append(num)
    print("Vetor Original: "+str(vet))

def ordenaVetor(vet,tam,thread_num,parcela1,parcela2,metade):
    print("Iniciando thread: " + str(thread_num))
    vetOrdenado1 = []
    vetOrdenado2 = []
    vetOrdenado3 = []
    vetOrdenado4 = []
    ofc = []

    if(thread_num==0):
        for i in range(parcela1):
            y = vet[i]
            vetOrdenado1.append(y)
            ofc = sorted(vetOrdenado1)
        #print("Primeira parte do vetor selecionada: " + str(vetOrdenado1))

    #cont1=parcela1
    if(thread_num == 1):
        for cont1 in range(parcela1,metade):
            x = vet[cont1]
            vetOrdenado2.append(x)
            ofc = sorted(vetOrdenado2)
        #print("Segunda parte do vetor selecionada: " + str(vetOrdenado2))

    #cont2=metade
    if(thread_num == 2):
        for cont2 in range(metade,parcela2):
            z = vet[cont2]
            vetOrdenado3.append(z)
            ofc = sorted(vetOrdenado3)
        #print("Terceira parte do vetor selecionada: " + str(vetOrdenado3))

    #cont3=parcela2
    if(thread_num == 3):
        for cont3 in range (parcela2,tam):
            w = vet[cont3]
            vetOrdenado4.append(w)
            ofc = sorted(vetOrdenado4)
        #print("Quarta parte do vetor selecionada: " + str(vetOrdenado4))

    #print("Parcela ordenada: "+str(ofc))
    print("Thread: "+ str(thread_num)+" saindo")

def threads(vet,tam):
    threads=[]
    qtdThreads =  4
    metade = int(tam/2)
    parcela1 = int(metade/2)
    parcela2 = int(metade+parcela1)

    for i in range(qtdThreads):
        t = threading.Thread(target=ordenaVetor, args=(vet,tam,i,parcela1,parcela2,metade,))
        threads.append(t)
        t.start()

    for i in threads:
        i.join()

def main():
    tam = 80000
    vet = []
    preencheVetor(vet,tam)

    ini = time.time()
    threads(vet,tam)
    fim = time.time()

    exec = fim - ini
    print("\nTempo de inicialização: "+str(ini)+"\nTempo de Finizalização: "+str(fim) + "\nTempo de Execução: "+ str(exec))

main()
