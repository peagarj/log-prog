# Construa um programa onde o usuário digitará seis notas (números reais). 
# O programa deve calcular a média dessas notas e, em seguida, 
# exibir quantas e quais notas ficaram estritamente acima da média calculada.

notas = []

# solicita ao usuário as seis notas
for i in range(0, 6):
    nota = float(input(f"Digite uma nota: "))
    notas.append(nota)

print(85 * '=')

# calcula a média das seis notas
media = sum(notas) / len(notas)
print(f"\nMédia das notas: {media:.2f}")

acima_da_media = []

# verifica quais notas são maiores que a média
for nota in notas:
    if nota > media:
        acima_da_media.append(nota)

print(f"Quantidade de notas acima da média: {len(acima_da_media)}")

# verifica se existe alguma nota acima da média
if len(acima_da_media) > 0:
    print("Notas acima da média:")

    # exibe cada nota que ficou acima da média
    for nota in acima_da_media:
        print(nota)
else:
    
    # exibe cada nota que não fica acima da média
    print("Nenhuma nota ficou acima da média.")



