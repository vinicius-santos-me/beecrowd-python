# ============================================================
# beecrowd - 1048
# https://judge.beecrowd.com/pt/problems/view/1048
# ------------------------------------------------------------
# A empresa ABC resolveu conceder um aumento de salários a
# seus funcionários de acordo com a tabela abaixo: Salário
# Percentual de Reajuste 0 - 400.00 400.01 - 800.00 800.01 -
# 1200.00 1200.01 - 2000.00 Acima de 2000.00 15% 12% 10% 7% 4%
# Leia o salário do funcionário e calcule e mostre o novo
# salário, bem como o valor de reajuste ganho e o índice
# reajustado, em percentual.
#
# Entrada:
#   0 - 400.00
#   400.01 - 800.00
#   800.01 - 1200.00
#   1200.01 - 2000.00
#   Acima de 2000.00
#
# Saída:
#   15%
#   12%
#   10%
#   7%
#   4%
# ============================================================


def main():
    salario = float(input())
    aumento = 0

    if salario <= 400:
        aumento = 15
    elif salario > 400 and salario <= 800:
        aumento = 12
    elif salario > 800 and salario <= 1200:
        aumento = 10
    elif salario > 1200 and salario <= 2000:
        aumento = 7
    else:
        aumento = 4
    reajuste = (salario * aumento)/100 

    print(f"Novo salario: {(salario + reajuste):.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print(f"Em percentual: {aumento} %")
main()
