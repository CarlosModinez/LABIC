import cv2
import matplotlib.pyplot as plt
import numpy as np

def draw_square_in_center(square_size, position):

    initial_position = [int(position[0] - square_size[0]/2), int(position[1] - square_size[0]/2)]
    final_position = [int(position[0] + square_size[0]/2), int(position[1] + square_size[1]/2)]
    image[initial_position[0]:final_position[0], initial_position[1]:final_position[1]] = (0, 0, 0)


image = cv2.imread('../figures/vermelho.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

position = (image.shape[0]/2, image.shape[1]/2)
draw_square_in_center((100, 50), position)
plt.imshow(image)
plt.show()