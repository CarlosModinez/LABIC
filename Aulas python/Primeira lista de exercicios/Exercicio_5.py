def verificar_vogal(caracter):
    if caracter == 'a' or caracter == 'e' or caracter == 'i' or caracter == 'o' or caracter == 'u':
        return True
    else:
        return False

def verificar_caracter_especial(caracter):
    if (ord(caracter) < 97 or ord(caracter) > 122):
        return True
    else:
        return False

caracter = input("Caracter: ")  
caracter_minusculo = caracter.lower()#já passo para minusculo para facilitar a verificacao de caracteres especiais 

if verificar_vogal(caracter_minusculo):
    print("O caracter é uma vogal")

elif not verificar_caracter_especial(caracter_minusculo):
    print("O caracter é uma consoante")

else:
    print("Caracter inválido")
