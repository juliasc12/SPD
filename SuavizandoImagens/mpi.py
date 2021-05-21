import numpy as np
from mpi4py import MPI
import cv2
import time
import matplotlib as plt

inicio= time.time()

comm = MPI.COMM_WORLD #comunicador
nprocs = comm.Get_size() #qtd de processos
myrank = comm.Get_rank() #identificador

localImage = None #partes da img
firstImage = None #primeira app de filtro
image = None #img
n = 0  #posições
largura = 0
altura = 0
secondImage = None #img p mostrar inteira

if myrank == 0:
    image = cv2.imread("img.jpg", 0)
    altura, largura = image.shape
    n = int(altura/nprocs)
    secondImage = np.zeros((altura,largura), dtype= 'uint8') #np.zeros preenche com zero

(n,largura) = comm.bcast((n,largura), root = 0) #broadcast
localImage = np.zeros((n,largura), dtype= 'uint8')
comm.Scatterv(image, localImage, root = 0) #ele pega a img e passa partes da imagem(localimg) pra cada processo
firstImage = np.zeros((n,largura), dtype= 'uint8')

for y in range(1, n-1): #filtro
    for x in range(1, largura-1):
        media =  int(localImage[y-1][x-1]) + int(localImage[y-1][x]) + int(localImage[y-1][x+1])
        media +=  int(localImage[y][x-1]) + int(localImage[y][x]) + int(localImage[y][x+1])
        media +=  int(localImage[y+1][x-1]) + int(localImage[y+1][x]) + int(localImage[y+1][x+1])
        media = int(media/9)

        firstImage[y][x] = media

comm.Gatherv(firstImage, secondImage, root = 0)

fim=time.time()
tempo=fim-inicio
print("Tempo: %.2f" %tempo)
