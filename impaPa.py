# passo 1 : criar variavel
# passo1.5: atribuir valor a variavel
numero = int(input('Digite um numero: '))
# passo 2 : verificar se o resto da divisão da variavel
# por "2" é 0
print(numero)
result = numero%2
# passo 2.1: se for -> "é par"
if result == 0:
    print('é par')
else:
    print('é impar')    

# passo 3 : se não for -> "é impar"
print(result)

