# ============================================================
# beecrowd - 1037
# https://judge.beecrowd.com/pt/problems/view/1037
# ------------------------------------------------------------
# Você deve fazer um programa que leia um valor qualquer e
# apresente uma mensagem dizendo em qual dos seguintes
# intervalos ([0,25], (25,50], (50,75], (75,100]) este valor
# se encontra. Obviamente se o valor não estiver em nenhum
# destes intervalos, deverá ser impressa a mensagem “Fora de
# intervalo”. O símbolo ( representa "maior que". Por exemplo:
# [0,25] indica valores entre 0 e 25.0000, inclusive eles.
# (25,50] indica valores maiores que 25 Ex: 25.00001 até o
# valor 50.0000000
#
# Entrada:
#   25.01
#
# Saída:
#   Intervalo (25,50]
# ============================================================

def verificar_intervalo(valor):
    
    if valor >= 0 and valor <= 25:
        return "[0,25]"
    elif valor > 25 and valor <= 50:
        return "(25,50]"
    elif valor > 50 and valor <= 75:
        return "(50,75]"
    elif valor > 75 and valor <= 100:
        return "(75,100]"
    
def main():
    valor = float(input())
    verificador = verificar_intervalo(valor)
    if verificador:
        print(f"Intervalo {verificador}")
    else:
        print("Fora de intervalo")
main()

