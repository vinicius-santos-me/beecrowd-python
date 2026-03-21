# ============================================================
# beecrowd - 1010
# https://judge.beecrowd.com/pt/problems/view/1010
# ------------------------------------------------------------
# Neste problema, deve-se ler o código de uma peça 1, o número
# de peças 1, o valor unitário de cada peça 1, o código de uma
# peça 2, o número de peças 2 e o valor unitário de cada peça
# 2. Após, calcule e mostre o valor a ser pago.
#
# Entrada:
#   12 1 5.30
#   16 2 5.10
#
# Saída:
#   VALOR A PAGAR: R$ 15.50
# ============================================================

contador = 2
total = 0

while contador > 0:
    dados = input().split()
    soma = (int(dados[1]) * float(dados[2]))
    total += soma

    contador -= 1
print(f"VALOR A PAGAR: R$ {total:.2f}")
