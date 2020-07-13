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
        anotar_imagem_redimensionada(nome, 'imagens.txt')
        return nova_imagem

    else:
        anotar_imagem_desconsiderada(imagem, nome, 'imagens_desconsideradas.txt')
        raise KeyError()
        
    
def salvar_imagem_redimensionada(nome, imagem, diretorio):
    cv2.imwrite(diretorio+"/"+nome, imagem)


def anotar_imagem_redimensionada(nome_da_imagem, nome_do_arquivo):
    anotacoes_imagens_desconsideradas = io.open(nome_do_arquivo, "a+")
    anotacoes_imagens_desconsideradas.seek(0)
    classes = ['skull', 'human', 'zombie']
    flag_classe_encontrada = False

    for classe in classes:
        if classe.lower() in nome_da_imagem.lower():
            anotacoes_imagens_desconsideradas.write(nome_da_imagem + ', ' + classe + '\n')
            flag_classe_encontrada = True

    if flag_classe_encontrada == False:
        anotacoes_imagens_desconsideradas.write(nome_da_imagem + ', ' + 'classe nao encontrada' + '\n')

    anotacoes_imagens_desconsideradas.close()


def anotar_imagem_desconsiderada(imagem, nome_da_imagem, nome_do_arquivo):
    anotacoes_imagens_desconsideradas = io.open(nome_do_arquivo, "a+")
    anotacoes_imagens_desconsideradas.seek(0)

    h, w, _ = imagem.shape
    anotacoes_imagens_desconsideradas.write(nome_da_imagem + ', ' + str(w) + ', ' + str(h) + '\n') 
    anotacoes_imagens_desconsideradas.close()

