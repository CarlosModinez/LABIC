def gerar_multiplos_de_tres(numero_inicial, numero_final):
    lista = []
    numero_inicial_da_lista = numero_inicial

    # Obtem o menor numero multiplo de 3 que vai na lista
    while True:
        if numero_inicial_da_lista % 3 == 0 and numero_inicial_da_lista != 0:
            break
        else:
            numero_inicial_da_lista += 1

    # Monta a lista a parir do menor multiplo de 3 entre o numero_inicial e o numero_final
    for i in range (numero_inicial_da_lista, numero_final, 3):
        lista.append(i)
    return lista


lista = gerar_multiplos_de_tres(1, 50)

print("Tamanho da lista: %d" % len(lista))
print("Maior valor: %d" % max(lista))
print("Menor valor: %d" % min(lista))
print("Soma de todos os valores: %d" % sum(lista))

lista.sort()
print("Ordem crescente: %ls" % lista)

lista.reverse()
print("Ordem decrescente: %ls" % lista)
