# ============================================================
# beecrowd - 1038
# https://judge.beecrowd.com/pt/problems/view/1038
# ------------------------------------------------------------
# Com base na tabela abaixo, escreva um programa que leia o
# código de um item e a quantidade deste item. A seguir,
# calcule e mostre o valor da conta a pagar.
#
# Entrada:
#   3 2
#
# Saída:
#   Total: R$ 10.00
# ============================================================

mapa = {1: 4.00,2: 4.50,3: 5.00, 4: 2.00,5: 1.50}
entrada = list(map(int,input().split()))
print(f"Total: R$ {mapa[entrada[0]] * entrada[1]:.2f}")
