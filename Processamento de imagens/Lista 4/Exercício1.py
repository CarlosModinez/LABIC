import cv2
import matplotlib.pyplot as plt
import numpy as np

# abrindo a imagem
imagem = cv2.imread('../figures/gato.jpg')
# converte imagem para tons de cinza (gray)
imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# Normalizando os valores dos pixels da imagem
imagem = imagem / 255.0

# aplicando o ruído de sal e pimenta na imagem
ruido = np.random.randint(101, size = (imagem.shape[0], imagem.shape[1]))

imagem_ruido_salepimenta = np.where(ruido == 0, 0, imagem)
imagem_ruido_salepimenta = np.where(ruido == (100-1), 1, imagem_ruido_salepimenta)

# convertendo a imagem para 8bits e valores de pixels entre 0 e 255
imagem_ruido_salepimenta = (imagem_ruido_salepimenta * 255).astype("uint8")

# mostrando a imagem do ruido
plt.imshow(imagem_ruido_salepimenta, cmap='gray')
plt.show()

#testando alguns filtros
bilateral_image = cv2.bilateralFilter(imagem_ruido_salepimenta, 5, 100, 100)
plt.imshow(bilateral_image, cmap='gray')
plt.show()

blur_image = cv2.blur(imagem_ruido_salepimenta, (5, 5))
plt.imshow(blur_image, cmap='gray')
plt.show()

gauss_image = cv2.GaussianBlur(imagem_ruido_salepimenta, (5, 5), 0)
plt.imshow(gauss_image, cmap='gray')
plt.show()

median_image = cv2.medianBlur(imagem_ruido_salepimenta, 5)
plt.imshow(median_image, cmap='gray')
plt.show()

#########################################################################################################
#Como já era esperado, a melhor técnica para remoção do ruído foi a suavização pela mediano.
#########################################################################################################