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

valor = float(input())


cedula_100 = int(valor // 100)
cedula_50 = int((valor % 100) // 50)
cedula_20 = int((valor % 50) // 20)
cedula_10 = int((valor % 10) // 10)
cedula_5 = int((valor % 10) // 5)
cedula_2 = int((valor % 5) // 2)

moeda_1 = int((valor % 5) // 1)
moeda_50 = int((valor % 1) // 0.5)
moeda_25 = int((valor % 0.5) // 0.25)
moeda_10 = int((valor % 0.25) // 0.1)
moeda_05 = int((valor % 0.1) // 0.05)
moeda_01 = int(((valor % 0.1) + 0.001 )// 0.01)
               

print("NOTAS:")
print(f"{cedula_100} nota(s) de R$ 100.00")
print(f"{cedula_50} nota(s) de R$ 50.00")
print(f"{cedula_20} nota(s) de R$ 20.00")
print(f"{cedula_10} nota(s) de R$ 10.00")
print(f"{cedula_5} nota(s) de R$ 5.00")
print(f"{cedula_2} nota(s) de R$ 2.00")

print("MOEDAS:")
print(f"{moeda_1} moeda(s) de R$ 1.00")
print(f"{moeda_50} moeda(s) de R$ 0.50")
print(f"{moeda_25} moeda(s) de R$ 0.25")
print(f"{moeda_10} moeda(s) de R$ 0.10")
print(f"{moeda_05} moeda(s) de R$ 0.05")
print(f"{moeda_01} moeda(s) de R$ 0.01")
