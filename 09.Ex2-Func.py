# pegue o nome e a cidade
# se a cidade for RJ,
# print "seja bem vindo a cidade maravilhosa, nome"
# se nao for rj, exiba o nome da pessoa e da cidade

def verificar_local(nome, cidade):
    if cidade == 'Rio de Janeiro' or cidade == 'RJ':
        print(f'Seja bem vindo à Cidade Maravilhosa, {nome}')
    else:
        print(f'Seja bem vindo à {cidade}, {nome}')
    
nome = input('Digite o seu nome: ')
cidade = input('Digite a cidade: ')

verificar_local(nome, cidade)

