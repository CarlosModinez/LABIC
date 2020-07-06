def obter_conceito(nota):
    #A (10-9), B(7-8.9), C(5-6.9), D(4-5.9) e E(0-3.9).
    if nota <=10 and nota >= 9:
        conceito = "A"
    elif nota <=8.9 and nota >= 7:
        conceito = "B"
    elif nota <=6.9 and nota >= 5:
        conceito = "C"
    elif nota <=4.9 and nota >= 5:
        conceito = "D"
    elif nota <=4.9 and nota >= 0:
        conceito = "E"

    return conceito

def receber_notas():
    primeira_nota = float(input("Primeira nota: "))
    segunda_nota = float(input("Segunda nota: "))
    notas = [primeira_nota, segunda_nota]
    return notas

def calcular_media(primeira_nota, segunda_nota):
    return (primeira_nota + segunda_nota) / 2


notas_do_aluno = receber_notas()
media_do_aluno = calcular_media(notas_do_aluno[0], notas_do_aluno[1])
conceito = obter_conceito(media_do_aluno)
print("Média: %.1f - conceito: %s" % (media_do_aluno, conceito))

