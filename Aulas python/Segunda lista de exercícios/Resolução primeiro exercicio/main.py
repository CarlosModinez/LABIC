import funcoes_importantes as fi

def redimensionar_imagens_e_salvar(dir_imagens_originais, dir_imagens_redimensionadas, nova_dimensao, tamanho_minimo):
    imagens = fi.carregar_nomes_imagens(dir_imagens_originais)
    fi.criar_diretorio_de_saida(dir_imagens_redimensionadas)
    imagens_redimensionadas = []
    for imagem in imagens:

        try:
            nova_imagem = fi.redimensionar_imagem('imagens/'+imagem, nova_dimensao, tamanho_minimo)
            imagens_redimensionadas.append(nova_imagem)
            fi.salvar_imagem_redimensionada(imagem, imagens_redimensionadas[-1], dir_imagens_redimensionadas)
        except KeyError:
            print("Imagem nao tem tamanho minimo para ser redimensionada")
    

redimensionar_imagens_e_salvar('imagens', 'imagens_redimensionadas', (150, 200), 300)