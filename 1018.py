# ============================================================
# beecrowd - 1018
# https://judge.beecrowd.com/pt/problems/view/1018
# ------------------------------------------------------------
# Leia um valor inteiro. A seguir, calcule o menor número de
# notas possíveis (cédulas) no qual o valor pode ser
# decomposto. As notas consideradas são de 100, 50, 20, 10, 5,
# 2 e 1. A seguir mostre o valor lido e a relação de notas
# necessárias.
#
# Entrada:
#   576
#
# Saída:
#   576
#   5 nota(s) de R$ 100,00
#   1 nota(s) de R$ 50,00
#   1 nota(s) de R$ 20,00
#   0 nota(s) de R$ 10,00
#   1 nota(s) de R$ 5,00
#   0 nota(s) de R$ 2,00
#   1 nota(s) de R$ 1,00
# ============================================================

valor = int(input())
print(valor)
c_100 = 0
c_50 = 0
c_20 = 0
c_10 = 0
c_5 = 0
c_2 = 0
c_1 = 0

while valor > 0:
    if valor >= 100:
        c_100 += 1
        valor = (valor - 100)

    elif valor >= 50:
        c_50 += 1
        valor = (valor - 50)

    elif valor >= 20:
        c_20 += 1
        valor = (valor - 20)

    elif valor >= 10:
        c_10 += 1
        valor = (valor - 10)

    elif valor >= 5:
        c_5 += 1
        valor = (valor - 5)

    elif valor >= 2:
        c_2 += 1
        valor = (valor - 2)

    elif valor >= 1:
        c_1 += 1
        valor = (valor - 1)

print(f"{c_100} nota(s) de R$ 100,00")
print(f"{c_50} nota(s) de R$ 50,00")
print(f"{c_20} nota(s) de R$ 20,00")
print(f"{c_10} nota(s) de R$ 10,00")
print(f"{c_5} nota(s) de R$ 5,00")
print(f"{c_2} nota(s) de R$ 2,00")
print(f"{c_1} nota(s) de R$ 1,00")
