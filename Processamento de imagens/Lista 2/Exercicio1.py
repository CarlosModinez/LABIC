import cv2
import matplotlib.pyplot as plt

image = cv2.imread('../figures/televisao.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

cropped_image = image[30:220, 62:330]
hor_inverted_image = cv2.flip(cropped_image, 1) 

plt.imshow(hor_inverted_image)
plt.show()