# ============================================================
# beecrowd - 1046
# https://judge.beecrowd.com/pt/problems/view/1046
# ------------------------------------------------------------
# Leia a hora inicial e a hora final de um jogo. A seguir
# calcule a duração do jogo, sabendo que o mesmo pode começar
# em um dia e terminar em outro, tendo uma duração mínima de 1
# hora e máxima de 24 horas.
#
# Entrada:
#   16 2
#
# Saída:
#   O JOGO DUROU 10 HORA(S)
# ============================================================

def main():
    hora_inicial,hora_final = map(int,input().split())
    
    if hora_inicial >= hora_final:
        duracao = (24-hora_inicial) + hora_final
    else:
        duracao = hora_final - hora_inicial
    print(f"O JOGO DUROU {duracao} HORA(S)")

main()

