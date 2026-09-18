# inicializa os acumuladores do expediente

faturamento_total = 0.0
quantidade_clientes = 0

# inicia o atendimento dos clientes

total_compra = float(input("digite 0 para encerrar ou qualquer outro valor para iniciar um cliente: "))

while total_compra != 0:

# zera o total da compra do cliente atual
# lê os valores dos produtos até o cliente finalizar a compra
# aplica o desconto de acordo com o valor total da compra
    
    total_compra = 0.0
    
    valor_produto = float(input("digite o valor do produto ou -1 para finalizar a compra: "))

    while valor_produto != -1:
        total_compra += valor_produto
        valor_produto = float(input("digite o valor do produto ou -1 para finalizar a compra: "))

# aplica o desconto de acordo com o valor total da compra
    
    if total_compra > 200:
        desconto = total_compra * 0.10
    elif total_compra > 100:
        desconto = total_compra * 0.05
    else:
        desconto = 0.0

# calcula o valor final após o desconto
    
    valor_final = total_compra - desconto

    print("total da compra: R$", total_compra)
    print("desconto: R$", desconto)
    print("valor final: R$", valor_final)

    # solicita a quantidade de parcelas
    
    parcelas = int(input("digite a quantidade de parcelas (1 a 6): "))

    # calcula o valor exato de cada parcela
    valor_parcela = valor_final / parcelas

    # exibe o cronograma de pagamento usando um loop for
    print("cronograma de pagamento:")

    for numero_parcela in range(1, parcelas + 1):
        print("parcela", numero_parcela, ": R$", valor_parcela)

    # atualiza os acumuladores do expediente
    faturamento_total += valor_final
    quantidade_clientes += 1

    # pergunta se haverá outro cliente
    total_compra = float(input("digite 0 para encerrar ou qualquer outro valor para iniciar outro cliente: "))

# exibe o resumo do expediente
print("resumo do expediente")
print("faturamento total do dia: R$", faturamento_total)
print("quantidade de clientes atendidos:", quantidade_clientes)
