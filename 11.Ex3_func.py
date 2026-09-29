# Construa um programa onde o usuário digitará 
# cinco números e o programa deverá colocar esses números 
# dentro do vetor em ordem crescente.

numeros = []

# solicita 5 números ao usuário
for i in range(0, 5):
    numero = float(input(f"Digite o {i + 1}º número: "))
    numeros.append(numero)

# ordena os números em ordem crescente
numeros.sort()

# mostra os números ordenados
print("Números em ordem crescente:")
print(numeros)

