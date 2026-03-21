# ============================================================
# beecrowd - 1017
# https://judge.beecrowd.com/pt/problems/view/1017
# ------------------------------------------------------------
# Joaozinho quer calcular e mostrar a quantidade de litros de
# combustível gastos em uma viagem, ao utilizar um automóvel
# que faz 12 KM/L. Para isso, ele gostaria que você o
# auxiliasse através de um simples programa. Para efetuar o
# cálculo, deve-se fornecer o tempo gasto na viagem (em horas)
# e a velocidade média durante a mesma (em km/h). Assim,
# pode-se obter distância percorrida e, em seguida, calcular
# quantos litros seriam necessários. Mostre o valor com 3
# casas decimais após o ponto.
#
# Entrada:
#   10
#   85
#
# Saída:
#   70.833
# ============================================================

horas = int(input())
total_distancia = int(input())

km = horas * total_distancia
litros = km/12

print(f"{litros:.3f}")

