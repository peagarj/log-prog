# Construa uma página/programa onde o usuário digitará o nome e o bairro de
# dez pessoas. O programa exibirá o nome e bairro das pessoas em ordem alfabética.

pessoas = []

for i in range(0, 3):
    nome = input(f"Digite o nome da {i + 1}ª pessoa: ")
    bairro = input(f"Digite o bairro de {nome}: ")
    pessoas.append([nome, bairro])

# ordenar pelo bairro
pessoas.sort(key=lambda x: x[1])

# Exibir em ordem alfabética
print("\nPessoas em ordem alfabética:")

for pessoa in pessoas:
    print(f"Nome: {pessoa[0]} - Bairro: {pessoa[1]}")
