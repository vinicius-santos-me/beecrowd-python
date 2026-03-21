# ============================================================
# beecrowd - 1175
# https://judge.beecrowd.com/pt/problems/view/1175
# ------------------------------------------------------------
# Faça um programa que leia um vetor N [20]. Troque a seguir,
# o primeiro elemento com o último, o segundo elemento com o
# penúltimo, etc., até trocar o 10º com o 11º. Mostre o vetor
# modificado.
#
# Entrada:
#   0
#   -5
#   ...
#   63
#   230
#
# Saída:
#   N[0] = 230
#   N[1] = 63
#   ...
#   N[18] = -5
#   N[19] = 0
# ============================================================

def reversed_by_me(lista):
    for i in range(len(lista)//2):
        lista[i],lista[len(lista)-1-i]=lista[len(lista)-1-i],lista[i]
def main():
    lista = [input() for _ in range(20)]
    reversed_by_me(lista)

    for i in range(len(lista)):
        print(f"N[{i}] = {lista[i]}")
main()

