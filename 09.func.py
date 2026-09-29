# somar 2 numeros
def somar(a, b):
    a = a + b 
    return a # isso faz ser uma função

a = 5
b = 4
c = somar (5, 4)
print(c)
print(a)



# subtrair dois numeros

def subtrair (a, b):
    '''
    Essa função subtrai o 'a' de 'b' e retorna o valor
    '''
    return a - b

subtrair(1, -1)

# saber se é impar
def impar(numero):
    if not numero % 2 == 0:
        return True

    return False