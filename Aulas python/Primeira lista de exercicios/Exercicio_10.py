def verifica_palindromo(palavra):
    #deixar tudo em minusculo
    palavra = palavra.lower()

    #remover os espacos
    palavra = palavra.replace(" ", "")

    #transformar em lista para utilizar o metodo reverse
    lista_caracteres = list(palavra)
    
    #verificar lista na ordem normal e invertida
    if lista_caracteres[::-1] == lista_caracteres:
        return True
    else:
        return False
    

palavra = input("Pavra ou frase para verificar se é polindromo: ")
if verifica_palindromo(palavra):
    print("'%s' é poilindromo" % palavra)
else:
    print("'%s' não é poilindromo" % palavra)




