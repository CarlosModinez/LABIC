import cv2
import os

def redimensionar_imagens_e_salvar(dir_imagens_originais, dir_imagens_redimensionadas, nova_dimensao, tamanho_minimo):
    imagens = carregar_nomes_imagens(dir_imagens_originais)
    criar_diretorio_de_saida(dir_imagens_redimensionadas)
    imagens_redimensionadas = []
    for imagem in imagens:
        imagens_redimensionadas.append(redimensionar_imagem('imagens/'+imagem, nova_dimensao, tamanho_minimo))
        salvar_imagem_redimensionada(imagem, imagens_redimensionadas[-1], dir_imagens_redimensionadas)


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
    
redimensionar_imagens_e_salvar('imagens', 'imagens_redimensionadas2', (200, 150), 200)

