import numpy
import time
import threading

def soma (inicio, fim):
    global resultadoSoma
    for x in range (inicio, fim,1):
         resultadoSoma = resultadoSoma + vetor[x]

inicio= time.time() #iniciando a contagem de execucao

tamanho = 100000
qtdThreads = 4
intervaloThread = tamanho//qtdThreads
posicaoInicial = 0
posicaoFinal = intervaloThread
resultadoSoma = 0

vetor = numpy.random.randint(0,10, tamanho)
print("Vetor: ",vetor)

threads = []

for i in range (qtdThreads):
    t = threading.Thread(target=soma, args=(posicaoInicial,posicaoFinal))
    threads.append(t)
    t.start()
    posicaoInicial = posicaoFinal
    posicaoFinal = posicaoFinal + intervaloThread

for i in threads:
    i.join()

print ("Resultado: ",resultadoSoma)

#finalizando a contagem de execucao e printando na tela
fim=time.time()
tempo=fim-inicio
print("Tempo: %.2f" %tempo)
