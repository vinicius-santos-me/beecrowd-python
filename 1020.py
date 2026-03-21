# ============================================================
# beecrowd - 1020
# https://judge.beecrowd.com/pt/problems/view/1020
# ------------------------------------------------------------
# Leia um valor inteiro correspondente à idade de uma pessoa
# em dias e informe-a em anos, meses e dias Obs.: apenas para
# facilitar o cálculo, considere todo ano com 365 dias e todo
# mês com 30 dias. Nos casos de teste nunca haverá uma
# situação que permite 12 meses e alguns dias, como 360, 363
# ou 364. Este é apenas um exercício com objetivo de testar
# raciocínio matemático simples.
#
# Entrada:
#   400
#
# Saída:
#   1 ano(s)
#   1 mes(es)
#   5 dia(s)
# ============================================================

dias_total = int(input())

ano = dias_total // 365
meses = (dias_total % 365) // 30
dias_restantes = (dias_total % 365) % 30


print(f"{ano} ano(s)")
print(f"{meses} mes(es)")
print(f"{dias_restantes} dia(s)")
