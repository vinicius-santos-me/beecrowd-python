# ============================================================
# beecrowd - 1040
# https://judge.beecrowd.com/pt/problems/view/1040
# ------------------------------------------------------------
# Leia quatro números (N 1 , N 2 , N 3 , N 4 ), cada um deles
# com uma casa decimal, correspondente às quatro notas de um
# aluno. Calcule a média com pesos 2, 3, 4 e 1,
# respectivamente, para cada uma destas notas e mostre esta
# média acompanhada pela mensagem "Media: " . Se esta média
# for maior ou igual a 7.0, imprima a mensagem "Aluno
# aprovado." . Se a média calculada for inferior a 5.0,
# imprima a mensagem "Aluno reprovado." . Se a média calculada
# for um valor entre 5.0 e 6.9, inclusive estas, o programa
# deve imprimir a mensagem "Aluno em exame." . No caso do
# aluno estar em exame, leia um valor correspondente à nota do
# exame obtida pelo aluno. Imprima então a mensagem "Nota do
# exame: " acompanhada pela nota digitada. Recalcule a média
# (some a pontuação do exame com a média anteriormente
# calculada e divida por 2). e imprima a mensagem "Aluno
# aprovado." (caso a média final seja 5.0 ou mais ) ou "Aluno
# reprovado." , (caso a média tenha ficado 4.9 ou menos). Para
# estes dois casos (aprovado ou reprovado após ter pego exame)
# apresente na última linha uma mensagem "Media final: "
# seguido da média final para esse aluno.
#
# Entrada:
#   2.0 4.0 7.5 8.0
#   6.4
#
# Saída:
#   Media: 5.4
#   Aluno em exame.
#   Nota do exame: 6.4
#   Aluno aprovado.
#   Media final: 5.9
# ============================================================

def definir_media(notas):
    media = ((notas[0] * 2) + (notas[1] * 3) + (notas[2] * 4) + (notas[3] * 1))/10 
    return media

def main():
    notas = list(map(float,input().split()))
    verificador = definir_media(notas)
    print(f"Media: {verificador:.1f}")
    if verificador >= 7:
        print("Aluno aprovado.")
    elif verificador < 5:
        print("Aluno reprovado.")
    elif verificador >= 5 and verificador <= 6.9:
        print("Aluno em exame.")
        exame = float(input())
        print(f"Nota exame: {exame:.1f}")
        nova_media = (verificador + exame)/2
        if nova_media >= 5:
            print("Aluno aprovado.")
        else:
            print("Aluno reprovado.")
        print(f"Media final: {nova_media:.1f}")
main()

