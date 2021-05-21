import numpy as np
import cv2
import time
import matplotlib as plt

inicio= time.time()

image = cv2.imread("img.jpg", 0)

altura, largura = image.shape
newimage = np.zeros((altura, largura),dtype = 'uint8')

for y in range(1,altura - 1):
    for x in range(1, largura - 1):
        media = int(image[y-1][x-1]) + int(image[y-1][x]) + int(image[y-1][x+1])
        media += int(image[y][x-1]) + int(image[y][x]) + int(image[y][x-1])
        media += int(image[y+1][x-1]) + int(image[y+1][x]) + int(image[y+1][x+1])

        media = int(media / 9)

        newimage[y][x] = media

fim=time.time()
tempo=fim-inicio
print("Tempo: %.2f" %tempo)
