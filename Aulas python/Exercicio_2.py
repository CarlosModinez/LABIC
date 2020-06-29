def receber_coordenadas():
    x = int(input("Coordenada X: "))
    y = int(input("Coordenada Y: "))
    
    #Estou utilizando o ponto como uma Tupla
    ponto = (x, y)
    return ponto

def calcular_distancia(A, B):
    return ((B[0] - A[0])**2 + (B[1] - A[1])**2)**(1/2)


print("Ponto A")
ponto_A = receber_coordenadas()

print("\nPonto B")
ponto_B = receber_coordenadas()

distancia = calcular_distancia(ponto_A, ponto_B)
print("\nDistância: %.4f" % distancia)

