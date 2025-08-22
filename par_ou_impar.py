import random

soma = rodadas = vitorias =  derrotas = 0

while True:
    poui = input("Você quer ser par ou ímpar? P/I\n")
    
    if poui in ["p", "P"]:
        print("Você escolheu par! O computador será ímpar.")
        jogada = int(input("Que número você vai jogar? (1 a 10)\n"))
        computador = random.randint(1,11)

        soma = jogada + computador

        if soma % 2 == 0:
            print(f"Você jogou {jogada} e o computador {computador}.")
            res = input(f"{soma} é par! Você ganhou esta rodada! Quer continuar jogando? S/N\n")
            rodadas += 1
            vitorias += 1
        else:
            print(f"Você jogou {jogada} e o computador {computador}.")
            res = input(f"{soma} é ímpar... Você perdeu esta rodada... Quer continuar jogando? S/N\n")
            rodadas += 1
            derrotas += 1

    elif poui in ["i", "I"]:
        print("Você escolheu ímpar! O computador será par.")
        jogada = int(input("Que número você vai jogar? (1 a 10)\n"))
        computador = random.randint(1,11)

        soma = jogada + computador

        if soma % 2 != 0:
            print(f"Você jogou {jogada} e o computador {computador}.")
            res = input(f"{soma} é ímpar. Você ganhou esta rodada! Quer continuar jogando? S/N\n")
            rodadas += 1
            vitorias += 1

        else:
            print(f"Você jogou {jogada} e o computador {computador}.")
            res = input(f"{soma} é par... Você perdeu esta rodada... Quer continuar jogando? S/N\n")
            rodadas += 1
            derrotas += 1
        
    if res in ["s", "S"]:
        continue
    else: 
        break

print(f"Jogo finalizado! Você jogou {rodadas} vezes, ganhou {vitorias} vez(es) e perdeu {derrotas} vez(es).")