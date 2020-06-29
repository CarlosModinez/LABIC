def reajustar_salario(salario):
    return salario*1.35

salario = float(input("Salário: R$ "))
print("Salário com reajuste: R$ %.2f" % reajustar_salario(salario))