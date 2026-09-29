# Construa um programa onde o usuário digitará cinco números para preencher um vetor. 
# O programa deve criar um segundo vetor que contenha os mesmos elementos do primeiro,
# porém na ordem inversa, e exibir o novo vetor na tela.

lista = []
for i in range(0, 5):
    numero = int(input('Digite um número: '))
    lista.append(numero)

# 1° forma -> copiar o vetor e inverter o novo
nova_lista = lista.copy()
nova_lista.reverse()
print(nova_lista)

# 2° forma -> copiar no processo de inversão
lista2 = reversed(lista)
for numero in lista2:
    print(lista2)

# 3° forma -> sem função
lista_inversa = []
j = 0
lista = [0, 1, 9, -5, 8]
                   # (4[inicio] -1 [parada], -1 [passo])
for i in range(len(lista)-1, 0, -1):
    lista_inversa[j] = lista[i]
    j = j + 1
    
