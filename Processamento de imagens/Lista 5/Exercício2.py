import cv2
import matplotlib.pyplot as plt 
import numpy as np

image = cv2.imread('../figures/bandeiras.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Monta o histograma dos tons de cinza
h2, b = np.histogram(image, bins=256, range=(0, 256))
plt.figure()
plt.title('histograma')
plt.xlabel('intensidade')
plt.ylabel('quantidade de pixels')
plt.plot(h2)
plt.xlim([0, 256])
plt.show()


#como preto é 0, preciso apenas separa-lo do restante das intensidades. 
_, binarized_image = cv2.threshold(image, 20, 255, cv2.THRESH_BINARY)
plt.imshow(binarized_image, cmap='gray')
plt.show()
