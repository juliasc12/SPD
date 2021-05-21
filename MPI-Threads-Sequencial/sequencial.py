import numpy
import time

def soma (inicio, fim):
    resultado = numpy.zeros(1)

    for x in range (inicio, fim, 1):
        resultado = resultado + vetor[x]
    return resultado

inicio= time.time()
tamanho = 100000
vetor = numpy.random.randint(0,10, tamanho)

total = numpy.zeros(1)
total = soma(0, tamanho)

print("Vetor: ",vetor)
print(total)

fim=time.time()
tempo=fim-inicio
print("Tempo: %.2f" %tempo)
