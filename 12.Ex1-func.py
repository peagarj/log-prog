# Construa um programa onde o usuário digitará dez números inteiros 
# para preencher um vetor. Em seguida, o programa deve percorrer 
# o vetor e substituir todos os números negativos por zero, 
# exibindo o vetor final na tela.

numeros = []

for i in range(0, 10):
    num = int(input('Digite um número inteiro: '))
    numeros.append(num)

print(85*'=')

for i in range(0, 10):
    if numeros[i] < 0:
        numeros[i] = 0

print(numeros)

