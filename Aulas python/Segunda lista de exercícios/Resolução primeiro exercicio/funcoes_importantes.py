import cv2
import os

def carregar_nomes_imagens(folder):
    return os.listdir(folder)

def criar_diretorio_de_saida(nome):
    if os.path.isdir(nome):
        return
    else:
        os.mkdir(nome)

def redimensionar_imagem(nome, novas_dimensoes, tamanho_minimo):
    imagem = cv2.imread(nome)
    h, w, _ = imagem.shape

    #O maior tamanho da imagem deve ser maior que o tamanho minimo
    if h > w:
        maior_dimensao = h
    else:
        maior_dimensao = w

    if maior_dimensao > tamanho_minimo:
        nova_imagem = cv2.resize(imagem, novas_dimensoes)
        return nova_imagem
    
    else:
        return
    
def salvar_imagem_redimensionada(nome, imagem, diretorio):
    cv2.imwrite(diretorio+"/"+nome, imagem)