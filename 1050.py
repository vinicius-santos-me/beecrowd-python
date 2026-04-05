# ============================================================
# beecrowd - 1050
# https://judge.beecrowd.com/pt/problems/view/1050
# ------------------------------------------------------------
# Leia um número inteiro que representa um código de DDD para
# discagem interurbana. Em seguida, informe à qual cidade o
# DDD pertence, considerando a tabela abaixo: Se a entrada for
# qualquer outro DDD que não esteja presente na tabela acima,
# o programa deverá informar: DDD nao cadastrado
#
# Entrada:
#   11
#
# Saída:
#   Sao Paulo
# ============================================================

def main():
    ddd = {61: "Brasilia",71: "Salvador",11: "Sao Paulo",21: "Rio de Janeiro",32: "Juiz de Fora",19: "Campinas",27: "Vitoria",31: "Belo Horizonte"}
    try:
        print(ddd[int(input())])
    except KeyError:
        print("DDD nao cadastrado")
main()

