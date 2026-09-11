import random

opcoes = ["pedra", "papel", "tesoura"]

print("=== PEDRA, PAPEL E TESOURA ===")

while True:
    jogador = input("Escolha pedra, papel ou tesoura (ou 'sair'): ").lower()

    if jogador == "sair":
        print("Jogo encerrado. Até logo")
        break

    if jogador not in opcoes:
        print("Opção inválida. Tente novamente.")
        continue

    computador = random.choice(opcoes)

    print("Você escolheu:", jogador)
    print("Computador escolheu:", computador)

    if jogador == computador:
        print("Empate!")

    elif (
        (jogador == "pedra" and computador == "tesoura") or
        (jogador == "papel" and computador == "pedra") or
        (jogador == "tesoura" and computador == "papel")
    ):
        print("Você venceu!")

    else:
        print("O computador venceu!")