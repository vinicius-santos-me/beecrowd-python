# ============================================================
# beecrowd - 1045
# https://judge.beecrowd.com/pt/problems/view/1045
# ------------------------------------------------------------
# Leia 3 valores de ponto flutuante A, B e C e ordene-os em
# ordem decrescente, de modo que o lado A representa o maior
# dos 3 lados. A seguir, determine o tipo de triângulo que
# estes três lados formam, com base nos seguintes casos,
# sempre escrevendo uma mensagem adequada: se A ≥ B+C,
# apresente a mensagem: NAO FORMA TRIANGULO se A 2 = B 2 + C 2
# , apresente a mensagem: TRIANGULO RETANGULO se A 2 > B 2 + C
# 2 , apresente a mensagem: TRIANGULO OBTUSANGULO se A 2 < B 2
# + C 2 , apresente a mensagem: TRIANGULO ACUTANGULO se os
# três lados forem iguais, apresente a mensagem: TRIANGULO
# EQUILATERO se apenas dois dos lados forem iguais, apresente
# a mensagem: TRIANGULO ISOSCELES
#
# Entrada:
#   7.0 5.0 7.0
#
# Saída:
#   TRIANGULO ACUTANGULO
#   TRIANGULO ISOSCELES
# ============================================================

def definir_tipo_triangulo(a,b,c):
    triangulo = ""
    if a >= (b+c):
        triangulo = "NAO FORMA TRIANGULO"
    elif (a**2) == ((b**2) + (c**2)):
        triangulo = "TRIANGULO RETANGULO"

    elif (a**2) > ((b**2) + (c**2)):
        triangulo = "TRIANGULO OBTUSANGULO"
    
    elif (a**2) < ((b**2) + (c**2)):
        triangulo = "TRIANGULO ACUTANGULO"

    print(triangulo)
def main():
    a,b,c = sorted(map(float, input().split()), reverse=True)
    definir_tipo_triangulo(a,b,c)
    
    if (a == b == c):
        print("TRIANGULO EQUILATERO")
    elif a == b or b == c or c == a:
        print("TRIANGULO ISOSCELES")
main()

