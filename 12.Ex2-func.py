# Construa um programa que peça ao usuário para digitar oito números 
# e os guarde em um vetor. Depois, o programa deve pedir um número adicional 
# e informar se esse número está presente no vetor. 
# Se estiver, informe em qual posição (índice) ele foi encontrado pela primeira vez.

numeros = []

for i in range(0, 8):
    numero = int(input(f"Digite o {i + 1}º número: "))
    numeros.append(numero)

# pede o número que será procurado no vetor
numero_busca = int(input("Digite o número que deseja procurar: "))

# verifica se o número está presente no vetor

if numero_busca in numeros:
    posicao = numeros.index(numero_busca)
    print(f"O número {numero_busca} foi encontrado na posição {posicao}.")

else:
    # caso o número não esteja presente
    print(f"O número {numero_busca} não está presente no vetor.")
