def depositar(saldo, valor):
    saldo += valor
    return saldo

def sacar(saldo, valor_saque):
    if saldo >= valor_saque:
        saldo -= valor_saque
    else:
        print("A operação não é possível, saldo insuficiente, tecle v para voltar \n")
    return saldo

def extrato(saldo):
    print("Saldo:", saldo)
    return saldo

saldo = 0
limite_transacoes_diario = 0

while True:
    if limite_transacoes_diario > 2:
        print("Você atingiu o limite máximo diário de transações, só é possivel continuar amanhã")
        break
    else:
        print("Saldo Atual:",saldo)
        menu = input("Escolha a opção: [d] Depósito, [s] Saque, [e] Extrato, [q] Sair\n")
        if menu == "d":
            extrato(saldo)
            valor = float(input("Digite o valor para depósito: \n"))
            saldo = depositar(saldo, valor)
            limite_transacoes_diario += 1
        elif menu == "s":
            extrato(saldo)
            valor_saque = float(input("Digite o valor para saque: \n"))
            saldo = sacar(saldo, valor_saque)
            limite_transacoes_diario += 1
        elif menu == "e":
                extrato(saldo)
        elif menu == "q":
            break
        else:
             print("Por favor, digite uma tecla válida")
