def verifica_primo(numero):
    # Divido o numero por dois para diminuir a quantidade de 
    # operacoes. Isso não afeta o resultado, já que o maior 
    # divisor poissivel difernte do proprio numero é o numero/2
    
    if numero <= 1:
        return False

    for i in range(2, int(numero/2)):
        if numero % i == 0:
            return False
    
    return True

num = int(input("Numero inteiro: "))

if verifica_primo(num):
    print("Numero %d é primo" % num)
        
    