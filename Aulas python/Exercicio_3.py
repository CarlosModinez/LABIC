def gerar_multiplos_de_tres(numero_inicial, numero_final):
    lista = []
    for i in range (numero_inicial, numero_final, 3):
        if i != 0:
            lista.append(i)
    return lista


lista = gerar_multiplos_de_tres(0, 50)

print("Tamanho da lista: %d" % len(lista))
print("Maior valor: %d" % max(lista))
print("Menor valor: %d" % min(lista))
print("Soma de todos os valores: %d" % sum(lista))

lista.sort()
print("Ordem crescente: %ls" % lista)

lista.reverse()
print("Ordem decrescente: %ls" % lista)