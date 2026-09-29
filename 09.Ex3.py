# sorteia um número aleatório entre 1 e 100
# informa ao jogador que o jogo começou
# repete até o jogador acertar

import random

numero_secreto = random.randint(1, 100)
print("Tente adivinhar o número entre 1 e 100.")

# Repete até o jogador acertar
while True:

# pede para o jogador digitar um número
# verifica se a tentativa é menor que o número secreto
    
    tentativa = int(input("Digite sua tentativa: "))

    if tentativa < numero_secreto:
        print("O número secreto é maior.")

# verifica se a tentativa é maior que o número secreto
# se não for maior nem menor, significa que acertou

    elif tentativa > numero_secreto:
        print("O número secreto é menor.")

    else:
        print("Parabéns! Você acertou o número.")
        break
    