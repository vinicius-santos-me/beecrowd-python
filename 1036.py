# ============================================================
# beecrowd - 1036
# https://judge.beecrowd.com/pt/problems/view/1036
# ------------------------------------------------------------
# Leia 3 valores de ponto flutuante e efetue o cálculo das
# raízes da equação de Bhaskara. Se não for possível calcular
# as raízes, mostre a mensagem correspondente “Impossivel
# calcular” , caso haja uma divisão por 0 ou raiz de numero
# negativo.
#
# Entrada:
#   10.0 20.1 5.1
#
# Saída:
#   R1 = -0.29788
#   R2 = -1.71212
# ============================================================

from math import sqrt
def delta(lista):
    a,b,c = lista[0],lista[1],lista[2]
    delta = (b ** 2) - (4*a*c)
    return delta

def bhaskara(lista):
    delta_bhaskara = delta(lista)
    
    a,b,c = lista[0],lista[1],lista[2]
    if a == 0:
        print("Impossivel calcular")
    elif delta_bhaskara < 0:
        print("Impossivel calcular")
    else:
        x1 = ((b * -1) + (sqrt(delta_bhaskara)))/(2 * a)

        x2 = ((b * -1) - (sqrt(delta_bhaskara)))/(2 * a)

        print(f"R1 = {x1:.5f}")
        print(f"R2 = {x2:.5f}")
def main():
    valores = list(map(float,input().split()))
    bhaskara(valores)
main()

