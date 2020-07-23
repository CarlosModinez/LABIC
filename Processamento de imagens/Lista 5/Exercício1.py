import cv2
import matplotlib.pyplot as plt 
import numpy as np


image = cv2.imread('../figures/bandeiras.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image)
plt.show()

_, binarized_image = cv2.threshold(image, 80, 255, cv2.THRESH_BINARY)
plt.imshow(binarized_image)
plt.show()