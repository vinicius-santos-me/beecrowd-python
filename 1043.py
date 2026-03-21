# ============================================================
# beecrowd - 1043
# https://judge.beecrowd.com/pt/problems/view/1043
# ------------------------------------------------------------
# Leia 3 valores reais (A, B e C) e verifique se eles formam
# ou não um triângulo. Em caso positivo, calcule o perímetro
# do triângulo e apresente a mensagem: Perimetro = XX.X Em
# caso negativo, calcule a área do trapézio que tem A e B como
# base e C como altura, mostrando a mensagem Area = XX.X
#
# Entrada:
#   6.0 4.0 2.0
#
# Saída:
#   Area = 10.0
# ============================================================

def verificador_triangulo(a,b,c):
    if a < (b+c) and b < (a+c) and c < (a+b):
        return True
    else:
        return False
def main():
    a,b,c = list(map(float,input().split()))
    
    if verificador_triangulo(a,b,c):
        print(f"Perimetro = {(a+b+c):.1f}")
    else:
        area = ((a+b) * c)/2
        print(f"Area = {area:.1f}")
main()
