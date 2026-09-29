# Construa um programa onde o usuário digitará 
# sete números e o programa escreverá, na tela, 
# quantos deles são pares e quantos são ímpares.

numeros = []
pares = 0
impares = 0

# solicita 7 números ao usuário 
for i in range(0, 7):
    numero = float(input(f"Digite o {i + 1}° número: "))
    numeros.append(numero)

# verifica se o número é par
for numero in numeros:
    if numero % 2 == 0:
        pares += 1
    else:
# caso não seja par, ele é ímpar
        impares += 1

# exibe os resultados
print("Números digitados:", numeros)
print("Quantidade de números pares:", pares)
print("Quantidade de números ímpares:", impares)



