import cv2
import matplotlib.pyplot as plt
import numpy as np
from Exercicio1 import hor_inverted_image as tv

cat = cv2.imread('../figures/gato.jpg')
cat = cv2.cvtColor(cat, cv2.COLOR_BGR2RGB)

new_size = (268, 190)
resized_cat = cv2.resize(cat, new_size)

mascara = np.zeros(resized_cat.shape[:2], dtype = "uint8")
cv2.rectangle(mascara, (60, 30), (tv.shape[1]-30, tv.shape[0]-30), 255, -1)
#Qua a diferenca desse com o de cima? 
#mascara[30:tv.shape[0]-30, 60:tv.shape[1]-30] = 255

cat_mask = cv2.bitwise_and(resized_cat, resized_cat, mask=mascara)


new_image = cv2.add(tv, cat_mask)
plt.imshow(new_image)
plt.show()


new_image = tv + cat_mask
plt.imshow(new_image)
plt.show()


#Este ultimo modo parece dar mais controle para a sobreposicao das imagens, além de ser mais facil de ajustar
new_image = cv2.addWeighted(tv, 0.2, cat_mask, 0.8, 0)
plt.imshow(new_image)
plt.show()

