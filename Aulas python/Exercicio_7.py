def fizz_buzz(numero_inicial, numero_final):
    lista = []
    for i in range(numero_inicial, numero_final):
        if i % 3 == 0:
            if i % 5 == 0:
                i = 'FizzBuzz'
            else:
                i = 'Fizz'

        elif i % 5 == 0:
            i = 'Buzz'

        lista.append(i)
    return lista


print(fizz_buzz(1, 51))