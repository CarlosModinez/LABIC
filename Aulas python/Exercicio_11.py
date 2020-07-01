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

def informar_horas_estacionada():
    placa = input("Placa: ")
    if placa in carros_estacionados.keys():
        print("Periodo estacionado: %s" % carros_estacionados[placa])
    else:
        print("placa invalida")
    
    print ("\n1 - para voltar para o menu")
    print("2 - tentar novamente")
    print ("0 - para sair")


    opcao = int(input())
    if opcao == 1:
        apresentar_menu()
    elif opcao == 2:
        informar_horas_estacionada()
    elif opcao == 0:
        return
    else:
        print("Opcao invalida")
    
def consultar_valor_recebido():
    print("Valor no caixa: %.2f" % valor_no_caixa)

    print ("\n1 - para voltar para o menu")
    print ("0 - para sair")
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
carros_estacionados = {"RSG4520": "12:52:50",
                       "AHG8520": "5:05:50",
                       "GSD4568": "9:12:50",
                       "LDM4582": "12:32:50",
                       "FJR2684": "1:11:50",
                       "FJR4820": "4:15:50"}

valor_no_caixa = 100.52
apresentar_menu()


