### importação da biblioteca opencv e matplotlib
import cv2
import matplotlib.pyplot as plt
import numpy as np

candle = cv2.imread('../figures/vela.jpg')
candle = cv2.cvtColor(candle, cv2.COLOR_BGR2GRAY)

#recortando e mostrando a imagem
cropped_candle = candle[35:380, 265:380]
plt.imshow(cropped_candle, cmap='gray')
plt.show()

imagem_equalizada = cv2.equalizeHist(cropped_candle)
plt.imshow(imagem_equalizada, cmap='gray')
plt.show()

#Criação do histograma
h = cv2.calcHist([cropped_candle], [0], None, [256], [0, 256])
plt.figure()
plt.title("Sem equalização")
plt.xlabel("Intensidade")
plt.ylabel("Quantidade de Pixels")
plt.plot(h)
plt.xlim([0, 256])
plt.show()

h = cv2.calcHist([imagem_equalizada], [0], None, [256], [0, 256])
plt.figure()
plt.title("Com equalização")
plt.xlabel("Intensidade")
plt.ylabel("Quantidade de Pixels")
plt.plot(h)
plt.xlim([0, 256])
plt.show()