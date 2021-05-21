import random
import time

def preencheVetor(vet,tam):
    for i in range(tam):
        num = int(random.randint(0,9))
        vet.append(num)

def OrdenaVetor(vet,tam):
    vetOrdenado = []
    for i in range(tam):
        vetOrdenado = sorted(vet)

def main():
    tam = 80000
    vet = []
    preencheVetor(vet,tam)

    ini = time.time()
    OrdenaVetor(vet,tam)
    fim = time.time()

    exec = fim - ini
    print("\nTempo de inicialização: "+str(ini)+
    "\nTempo de Finizalização: "+str(fim)+
    "\nTempo de Execução: "+ str(exec))

main()
