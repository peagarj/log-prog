
a = int(input("Digite o lado a: "))
b = int(input("Digite o lado b: "))
c = int(input("Digite o lado c: "))

# Verifica se os lados são positivos e se satisfazem a condição de existência

if a <= 0 or b <= 0 or c <= 0:
    print("Erro: os lados devem ser valores positivos.")
elif a + b > c and a + c > b and b + c > a:

# Classificação do triângulo

    if a == b == c:
        print("Triângulo Equilátero")
    elif a == b or a == c or b == c:
        print("Triângulo Isósceles")
    else:
        print("Triângulo Escaleno")
else:
    print("Erro: as medidas não formam um triângulo.")
