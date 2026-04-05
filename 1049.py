# ============================================================
# beecrowd - 1049
# https://judge.beecrowd.com/pt/problems/view/1049
# ------------------------------------------------------------
# Neste problema, você deverá ler 3 palavras que definem o
# tipo de animal possível segundo o esquema abaixo, da
# esquerda para a direita. Em seguida conclua qual dos animais
# seguintes foi escolhido, através das três palavras
# fornecidas.
#
# Entrada:
#   vertebrado
#   mamifero
#   onivoro
#
# Saída:
#   homem
# ============================================================

def main():
    dict = {"vertebrado": {"ave": ["carnivoro","onivoro","aguia","pomba"], "mamifero": ["onivoro","herbivoro","homem","vaca"]},"invertebrado": {"inseto": ["hematofago","herbivoro","pulga","lagarta"], "anelideo": ["hematofago","onivoro","sanguessuga","minhoca"]},}

    a = input()
    b = input()
    c = input()
    if dict[a][b][0] == c:
        print(f"{dict[a][b][2]}")
    else:
        print(f"{dict[a][b][3]}")
main()

