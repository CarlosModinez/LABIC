

### importação da biblioteca opencv e matplotlib
import cv2
import matplotlib.pyplot as plt

# abrindo a imagem
imagem = cv2.imread('../../figures/oceano.jpg')
# converte imagem para o modelo de cor RGB
imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# mostrando a imagem colorida
plt.imshow(imagem, cmap="gray")

