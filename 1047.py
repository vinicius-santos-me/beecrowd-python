# ============================================================
# beecrowd - 1047
# https://judge.beecrowd.com/pt/problems/view/1047
# ------------------------------------------------------------
# Leia a hora inicial, minuto inicial, hora final e minuto
# final de um jogo. A seguir calcule a duração do jogo. Obs: O
# jogo tem duração mínima de um (1) minuto e duração máxima de
# 24 horas.
#
# Entrada:
#   7 8 9 10
#
# Saída:
#   O JOGO DUROU 2 HORA(S) E 2 MINUTO(S)
# ============================================================

def main():
    hora_inicial,minuto_inicial,hora_final,minuto_final = map(int,input().split())
    
    inicio = hora_inicial * 60 + minuto_inicial
    fim = hora_final * 60 + minuto_final

    if fim <= inicio:
        fim += 24 * 60
    duracao = fim - inicio

    horas = duracao // 60
    minutos = duracao % 60
    print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")

main()

