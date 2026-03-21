# ============================================================
# beecrowd - 1035
# https://judge.beecrowd.com/pt/problems/view/1035
# ------------------------------------------------------------
# Leia 4 valores inteiros A, B, C e D. A seguir, se B for
# maior do que C e se D for maior do que A, e a soma de C com
# D for maior que a soma de A e B e se C e D, ambos, forem
# positivos e se a variável A for par escrever a mensagem
# "Valores aceitos" , senão escrever "Valores nao aceitos" .
#
# Entrada:
#   5 6 7 8
#
# Saída:
#   Valores nao aceitos
# ============================================================

def verificacao(lista):
    if (lista[1] > lista[2]) and (lista[2] + lista[3] > lista[0] + lista[1]) and (lista[2] > 0 and lista[3] > 0) and (lista[0] % 2 == 0):
        return "Valores aceitos"
    else:
        return "Valores nao aceitos" 
def main():
    valores = list(map(int,input().split()))
    print(verificacao(valores))
main()
