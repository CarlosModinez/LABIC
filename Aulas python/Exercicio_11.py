#Opcao 1 no menu
def imprimir_taxas():
    print("O estacionamento cobra R$2,00 pela entrada + R$0,50 por hora \nsendo o valor máximo para um periodo de 24h R$10,00")
    print ("\n1 - para voltar para o menu")
    print ("0 - para sair")
    
    opcao = int(input())
    if opcao == 1:
        apresentar_menu()
    elif opcao == 0:
        return
    else:
        print("Opcao invalida")

#opcao 2 do menu
def informar_horas_estacionada():
    placa = input("Placa: ")
    if placa in carros_estacionados.keys():
        print("Carro já cadastrado")
    else:
        horas = input("Tempo no esetacionamento(horas:minutos): ")
        carros_estacionados[placa] = horas
        print("Carro cadastrado com sucesso")


    print("\n1 - para voltar para o menu")
    print("2 - Cadastrar novo veiculo")
    print("0 - para sair")
    

    opcao = int(input())
    if opcao == 1:
        apresentar_menu()
    elif opcao == 2:
        informar_horas_estacionada()
    elif opcao == 0:
        return
    else:
        print("Opcao invalida")

#Opcao 3 do menu
def consultar_valor_recebido():
    valor_total = 0
    for placa in carros_estacionados:
        valor_total += 2
        tempo = carros_estacionados[placa].split(sep=":")
        minutos = int(tempo[1])
        horas = int(tempo[0])
        if minutos > 0:
            horas += 1
        valor_total += 0.5 * horas
        
    print("Valor recebido até o momento: R$%.2f" % valor_total)
    print("\n1 - para voltar para o menu")
    print("0 - para sair")
    

    opcao = int(input())
    if opcao == 1:
        apresentar_menu()
    elif opcao == 0:
        return
    else:
        print("Opcao invalida")


def apresentar_menu():
    print("Menu")
    print("1 – Imprimir taxas do estacionamento.")
    print("2 – Informar horas estacionada do veículo")
    print("3 – Consultar valor recebido até o momento")
    print("0 – Sair")

    while True:
        opcao = int(input())
        if opcao == 1: 
            imprimir_taxas()
            break
        elif opcao == 2:
            informar_horas_estacionada()
            break
        elif opcao == 3:
            consultar_valor_recebido()
            break
        elif opcao == 0:
            return
            break
        else:
            print("Opcao invalida")



#alguns dados fictícios
carros_estacionados = {"DSD8526": "23:35",
                       "GDS8975": "12:58",
                       "FJD5685": "12:00"}
apresentar_menu()