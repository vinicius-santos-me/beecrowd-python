# ============================================================
# beecrowd - 1044
# https://judge.beecrowd.com/pt/problems/view/1044
# ------------------------------------------------------------
# Leia 2 valores inteiros (A e B). Após, o programa deve
# mostrar uma mensagem "Sao Multiplos" ou "Nao sao Multiplos"
# , indicando se os valores lidos são múltiplos entre si.
#
# Entrada:
#   6 24
#
# Saída:
#   Sao Multiplos
# ============================================================

def main():
    a,b = list(map(int,input().split()))    
    if a % b == 0 or b % a == 0:
        print("Sao Multiplos")
    else:
        print("Nao sao Multiplos")
main()

