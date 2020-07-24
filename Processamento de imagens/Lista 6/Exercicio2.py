### importação da biblioteca opencv, matplotlib, numpy
import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread('../figures/dados.jpg')

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur_image = cv2.blur(gray_image, (10,10), 0)
ret, binarized_image = cv2.threshold(blur_image, 80, 255, cv2.THRESH_BINARY)
edges = cv2.Canny(binarized_image, 100, 200)

objetos, lx = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(image, objetos, -1, (255, 0, 0), 3) 

print("Quantidade de dados:", len(objetos))
plt.imshow(image)
plt.show()