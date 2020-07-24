### importação da biblioteca opencv, matplotlib, numpy
import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread('../figures/moedas.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# aplicando a suavização da imagem com uma mascara 7x7  -  por que 7x7 da certo e valores muito próximos nao??
blur_image = cv2.blur(gray_image, (7, 7))
ret,binarized_image = cv2.threshold(blur_image,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
edges = cv2.Canny(binarized_image, 100, 200)
plt.imshow(edges, cmap='gray')
plt.show()


objetos, lx = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print("Quantidade de moedas:", len(objetos))

cv2.drawContours(image, objetos, -1, (255, 0, 0), 3) 
plt.imshow(image)
plt.show()

