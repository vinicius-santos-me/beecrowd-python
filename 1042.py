# ============================================================
# beecrowd - 1042
# https://judge.beecrowd.com/pt/problems/view/1042
# ------------------------------------------------------------
# Leia 3 valores inteiros e ordene-os em ordem crescente. No
# final, mostre os valores em ordem crescente, uma linha em
# branco e em seguida, os valores na sequência como foram
# lidos.
#
# Entrada:
#   7 21 -14
#
# Saída:
#   -14
#   7
#   21
#   7
#   21
#   -14
# ============================================================

def insertion_sort(lista):
    for i in range(1,3):
        j = i
        while j > 0 and lista[j] < lista[j-1]:
            lista[j],lista[j-1] = lista[j-1],lista[j]
            j -= 1
def main():
    numeros = list(map(int,input().split()))
    numeros_ordenado = [numeros[e] for e in range(3)]
    insertion_sort(numeros_ordenado)

    for numero in numeros_ordenado:
        print(numero)
    print()

    for i in range(3):
        print(numeros[i])
main()

