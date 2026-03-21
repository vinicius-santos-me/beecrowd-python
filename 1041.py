# ============================================================
# beecrowd - 1041
# https://judge.beecrowd.com/pt/problems/view/1041
# ------------------------------------------------------------
# Leia 2 valores com uma casa decimal (x e y), que devem
# representar as coordenadas de um ponto em um plano. A
# seguir, determine qual o quadrante ao qual pertence o ponto,
# ou se está sobre um dos eixos cartesianos ou na origem (x =
# y = 0). Se o ponto estiver na origem, escreva a mensagem
# “Origem”. Se o ponto estiver sobre um dos eixos escreva
# “Eixo X” ou “Eixo Y”, conforme for a situação.
#
# Entrada:
#   4.5 -2.2
#
# Saída:
#   Q4
# ============================================================

x,y = map(float,input().split())
plano = ""
if x == 0 and y == 0:
    plano = "Origem"

elif x > 0 and y > 0:
    plano = "Q1"
elif x < 0 and y > 0:
    plano = "Q2"
elif x < 0 and y < 0:
    plano = "Q3"
elif x > 0 and y < 0:
    plano = "Q4"
elif x == 0 and y != 0:
    plano = "Eixo Y"
elif x != 0 and y == 0:
    plano = "Eixo X"
print(plano)
