import random
import time

def preencheVetor(vet,tam):
    for i in range(tam):
        num = int(random.randint(0,9))
        vet.append(num)
    #print("vetor preenchido: " + str(vet))

    ini = time.time()
    bubbleSort(vet,tam)
    fim = time.time()

    exec = fim - ini
    print("\nTempo de inicialização: "+str(ini)+
    "\nTempo de Finizalização: "+str(fim)+
    "\nTempo de Execução: "+ str(exec))

def bubbleSort(vet,tam):
    for tam in range(tam, 0, -1):
        trocou = False

        for i in range(0, tam-1):
            if vet[i] > vet[i + 1]:
                vet[i + 1], vet[i] = vet[i], vet[i + 1]
                trocou = True

        if not trocou:
            break
    #print("vetor ordenado: " + str(vet))

def main():
    tam = 20000
    vet = []
    preencheVetor(vet,tam)

main()
