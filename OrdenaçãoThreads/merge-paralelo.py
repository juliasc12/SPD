from mpi4py import MPI
import random
import numpy
import time

def main():

    inicio = time.time()
    comm = MPI.COMM_WORLD
    nprocs = comm.Get_size()
    myrank = comm.Get_rank()

    x=10
    size = int(x/nprocs)
    vetor = None
    vetorFinal = None

    if myrank == 0:    
        vetor = numpy.random.randint(200, size=x)
        vetorFinal = numpy.zeros(x, dtype='i')

    vetorPartido = numpy.zeros(size, dtype='i')
    comm.Scatterv(vetor, vetorPartido, root=0)
    mergeSort(vetorPartido, 0, len(vetorPartido))
    comm.Gatherv(vetorPartido, vetorFinal, root=0)

    if myrank == 0:
        mergeSort(vetorFinal, 0, len(vetorFinal))        
        fim = time.time()
        tempo = fim - inicio        
        print("Vetor Original:", vetor)
        print("Vetor final: ", vetorFinal)
        print("Tempo: ", tempo)


def mergeSort(vetor, inicio, fim):
    if fim - inicio > 1:
        meio = int((inicio + fim)//2)
        mergeSort(vetor, inicio, meio)
        mergeSort(vetor, meio, fim)
        merge(vetor, inicio, meio, fim)
 
def merge(vetor, inicio, meio, fim):
    left = numpy.copy(vetor[inicio:meio])
    right = numpy.copy(vetor[meio:fim])
    k = inicio
    i = 0
    j = 0
    while (inicio + i < meio and meio + j < fim):
        if (left[i] <= right[j]):
            vetor[k] = left[i]
            i = i + 1
        else:
            vetor[k] = right[j]
            j = j + 1
        k = k + 1
    if inicio + i < meio:
        while k < fim:
            vetor[k] = left[i]
            i = i + 1
            k = k + 1
    else:
        while k < fim:
            vetor[k] = right[j]
            j = j + 1
            k = k + 1
            
if __name__ == '__main__':
    main()
