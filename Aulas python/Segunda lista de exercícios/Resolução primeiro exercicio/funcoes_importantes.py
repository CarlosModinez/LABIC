import cv2
import os
import io


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
        anotar_imagem_desconsiderada(nome, 'imagens_desconsideradas.txt')
        raise KeyError()
        
    
def salvar_imagem_redimensionada(nome, imagem, diretorio):
    cv2.imwrite(diretorio+"/"+nome, imagem)

def anotar_imagem_desconsiderada(nome_da_imagem, nome_do_arquivo):
    anotacoes_imagens_desconsideradas = io.open(nome_do_arquivo, "a+")
    anotacoes_imagens_desconsideradas.seek(0)
    anotacoes_imagens_desconsideradas.write(nome_da_imagem + ', ' + 'classe\n')
    anotacoes_imagens_desconsideradas.close()