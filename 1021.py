# ============================================================
# beecrowd - 1021
# https://judge.beecrowd.com/pt/problems/view/1021
# ------------------------------------------------------------
# Leia um valor de ponto flutuante com duas casas decimais.
# Este valor representa um valor monetário. A seguir, calcule
# o menor número de notas e moedas possíveis no qual o valor
# pode ser decomposto. As notas consideradas são de 100, 50,
# 20, 10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25,
# 0.10, 0.05 e 0.01. A seguir mostre a relação de notas
# necessárias.
#
# Entrada:
#   576.73
#
# Saída:
#   NOTAS:
#   5 nota(s) de R$ 100.00
#   1 nota(s) de R$ 50.00
#   1 nota(s) de R$ 20.00
#   0 nota(s) de R$ 10.00
#   1 nota(s) de R$ 5.00
#   0 nota(s) de R$ 2.00
#   MOEDAS:
#   1 moeda(s) de R$ 1.00
#   1 moeda(s) de R$ 0.50
#   0 moeda(s) de R$ 0.25
#   2 moeda(s) de R$ 0.10
#   0 moeda(s) de R$ 0.05
#   3 moeda(s) de R$ 0.01
# ============================================================

n = float(input())

valor = round(n * 100)

notas_moedas = [10000, 5000, 2000, 1000, 500, 200, 100, 50, 25, 10, 5, 1]
nomes = [
    "nota(s) de R$ 100.00",
    "nota(s) de R$ 50.00",
    "nota(s) de R$ 20.00",
    "nota(s) de R$ 10.00",
    "nota(s) de R$ 5.00",
    "nota(s) de R$ 2.00",
    "moeda(s) de R$ 1.00",
    "moeda(s) de R$ 0.50",
    "moeda(s) de R$ 0.25",
    "moeda(s) de R$ 0.10",
    "moeda(s) de R$ 0.05",
    "moeda(s) de R$ 0.01",
]

print("NOTAS:")
for i in range(6):
    qtd = valor // notas_moedas[i]
    valor %= notas_moedas[i]
    print(f"{qtd} {nomes[i]}")

print("MOEDAS:")
for i in range(6, 12):
    qtd = valor // notas_moedas[i]
    valor %= notas_moedas[i]
    print(f"{qtd} {nomes[i]}")

