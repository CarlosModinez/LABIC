import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread('../figures/vermelho.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

image[0:image.shape[0], 0:image.shape[1]] = (0, 0, 0)

plt.imshow(image)
plt.show()