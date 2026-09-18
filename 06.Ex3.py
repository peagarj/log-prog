# solicitar o cargo do usuário
# solicitar a hora atual
# verificar se a chave de emergência está ativa
# se a chave de emergência estiver ativa, 
# o acesso é liberado
# se for supervisor, o acesso também é liberado
# se for operador e estiver entre 8 e 17 horas, 
# o acesso é liberado
# caso nenhuma condição seja atendida, 
# o acesso é bloqueado

cargo = input("Digite o cargo (operador ou supervisor): ")
hora_atual = int(input("Digite a hora atual (0 a 23): "))
chave_emergencia = True

if chave_emergencia:
    print("Acesso Concedido")

elif cargo == "supervisor":
    print("Acesso Concedido")

elif cargo == "operador" and 8 <= hora_atual <= 17:
    print("Acesso Concedido")

else:
    print("Acesso Bloqueado")

