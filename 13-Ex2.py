# Construa um programa que o usuário digitará o nome e a idade de dez
# pessoas e o programa escreverá o nome do usuário mais novo.

pessoas = []

for i in range(3):
    nome = input(f"Digite o nome da {i + 1}ª pessoa: ")
    idade = int(input(f"Digite a idade de {i + 1}ª pessoa: "))
    pessoas.append([nome, idade])

# considerando a primeira pessoa como a mais nova
mais_novo = pessoas[0]

# procura a menor idade
for pessoa in pessoas:
    if pessoa[1] < mais_novo[1]:
        mais_novo = pessoa

print(f"\nA pessoa mais nova é: {mais_novo[0]}")
print(f"Idade: {mais_novo[1]} anos")
