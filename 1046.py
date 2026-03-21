def main():
    hora_inicial,hora_final = map(int,input().split())
    
    if hora_inicial >= hora_final:
        duracao = (24-hora_inicial) + hora_final
    else:
        duracao = hora_final - hora_inicial
    print(f"O JOGO DUROU {duracao} HORA(S)")

main()
