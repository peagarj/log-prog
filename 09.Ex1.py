# Construa um programa onde o usuário digitará dois números, 
# utilizando passagem de parâmetros e, dentro da função, 
# irá calcular a soma desses dois números.

numero1 = int(input('Digite um némero: '))
numero2 = int(input('Digite um némero: '))

def somar(numero1, numero2):
    print(numero1 + numero2)

resultado = somar(numero1, numero2)
print(resultado)
