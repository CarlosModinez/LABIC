def determinar_volume_inicial(volume_final, numero_de_dias):
    # PG (a1 = an / q^(n-1))
    return volume_final/(2**(numero_de_dias-1))

numero_de_dias = int(input("Número de dias: "))
volume_final = float(input("Volume final da cultura: "))
 
print("Volume incial necessário: %.2f" % determinar_volume_inicial(volume_final, numero_de_dias))