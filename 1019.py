# ============================================================
# beecrowd - 1019
# https://judge.beecrowd.com/pt/problems/view/1019
# ------------------------------------------------------------
# Leia um valor inteiro, que é o tempo de duração em segundos
# de um determinado evento em uma fábrica, e informe-o
# expresso no formato horas:minutos:segundos.
#
# Entrada:
#   556
#
# Saída:
#   0:9:16
# ============================================================

segundos = int(input())

horas = (segundos // 3600)

minutos = (segundos // 60) - (horas * 60)

segundos_restantes = segundos - ((minutos * 60) + (horas * 3600))

print(f"{horas}:{minutos}:{segundos_restantes}")
