import cv2
import matplotlib.pyplot as plt 
import numpy as np

# abrindo a imagem
imagem = cv2.imread('../figures/gato.jpg')
# converte imagem para tons de cinza (gray)
imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# aplicando o ruído gaussiano
mean = 0.1
var = 1
sigma = var ** 0.5

imagem = imagem / 255.0
ruido_gaussiano = np.random.normal(mean, sigma, imagem.shape)
imagem_ruido_gaussiano = np.clip((imagem * (1 + ruido_gaussiano * 0.2)),0,1)

# convertendo a imagem para 8bits e valores de pixels entre 0 e 255
imagem_ruido_gaussiano = (imagem_ruido_gaussiano * 255).astype("uint8")

plt.title('original')
plt.imshow(imagem, cmap='gray')
plt.show()

# mostrando a imagem do ruido
plt.title('imagem com ruido')
plt.imshow(imagem_ruido_gaussiano, cmap='gray')
plt.show()

#testando alguns filtros
bilateral_image = cv2.bilateralFilter(imagem_ruido_gaussiano, 5, 100, 100)
plt.title('Bilateral')
plt.imshow(bilateral_image, cmap='gray')
plt.show()

blur_image = cv2.blur(imagem_ruido_gaussiano, (5, 5))
plt.title('Blur')
plt.imshow(blur_image, cmap='gray')
plt.show()

gauss_image = cv2.GaussianBlur(imagem_ruido_gaussiano, (5, 5), 100)
plt.title('Gaussiana')
plt.imshow(gauss_image, cmap='gray')
plt.show()

median_image = cv2.medianBlur(imagem_ruido_gaussiano, 5)
plt.title('Mediana')
plt.imshow(median_image, cmap='gray')
plt.show()


#########################################################################################################
#Apesar do filtro da Gaussiana apresentar o melhor resultado, o fitro blur tbm obteve um bom resultado.
#########################################################################################################