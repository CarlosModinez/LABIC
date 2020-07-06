numeros_inseridos = []

while True:
    num = int(input("Numero (0  caso deseje finalizar): "))
    if num == 0:
        break
    else: 
        numeros_inseridos.append(num)

soma = sum(numeros_inseridos)
media = (soma / len(numeros_inseridos))

print("Soma: %d" % soma)
print("Media: %.2f" % media)