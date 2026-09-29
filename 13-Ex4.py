# Construa uma página onde o usuário digitará o nome e a média de cinco
# alunos e o programa só aceitará a média do aluno 
# caso ela esteja entre zero e dez.


lista = []
for i in range(3):
    nome = input(f"Digite o nome da {i + 1}ª pessoa: ")
    media = float(input(f"Digite a média de {nome}: "))
    while media < 0 or media > 10:
        media = float(input(f"Digite a média de {nome}: "))
    lista.append([nome, media])
