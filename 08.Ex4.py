# Solicita ao usuário que digite um número
numero = int(input("Digite um número: "))

for i in range(0, 10):
    resultado = numero * (i + 1)
    print(f'{numero} x {i + 1} = {resultado}')



