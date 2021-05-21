import numpy
from mpi4py import MPI
import time

def soma (inicio, fim, vetor):
    resultado = numpy.zeros(1)

    for x in range (inicio, fim, 1):
        resultado = resultado + vetor[x]

    return resultado

def main():

    tamanho = 100000
    vetor = numpy.random.randint(0,10, tamanho)

    #comunicador
    comm = MPI.COMM_WORLD
    nprocs = comm.Get_size() #qtd de processos
    rank = comm.Get_rank() #identificador

    comm.Bcast (vetor, root=0)
    n = tamanho//nprocs #posições

    total = numpy.zeros(1)

    valor = soma (int(n*rank), int(n*(rank+1)), vetor)
    comm.Reduce (valor, total, op=MPI.SUM, root = 1)

    if rank == 0:
        print("Vetor: ",vetor)

    if rank == 1:
        print("Soma: ",total)

inicio= time.time()
main()
fim=time.time()
tempo=fim-inicio
print("Tempo: %.2f" %tempo)
