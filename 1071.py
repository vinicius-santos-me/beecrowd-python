# ============================================================
# beecrowd - 1071
# https://judge.beecrowd.com/pt/problems/view/1071
# ------------------------------------------------------------
# Leia 2 valores inteiros X e Y . A seguir, calcule e mostre a
# soma dos números impares entre eles.
#
# Entrada:
#   6
#   -5
#
# Saída:
#   5
# ============================================================

def soma_impares(menor,maior):
    soma = 0
    for i in range(menor+1,maior,1):
        if i % 2 != 0:
            soma += i
    return soma
def main():
    x,y = int(input()),int(input())

    if x < y:
        print(soma_impares(x,y))
    else:
        print(soma_impares(y,x))
main()

