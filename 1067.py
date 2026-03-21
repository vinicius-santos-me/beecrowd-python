# ============================================================
# beecrowd - 1067
# https://judge.beecrowd.com/pt/problems/view/1067
# ------------------------------------------------------------
# Leia um valor inteiro X (1 <= X <= 1000). Em seguida mostre
# os ímpares de 1 até X , um valor por linha, inclusive o X ,
# se for o caso.
#
# Entrada:
#   8
#
# Saída:
#   1
#   3
#   5
#   7
# ============================================================

def main():
    for i in range(int(input())+1):
        if i % 2 != 0:
            print(i)
main()

