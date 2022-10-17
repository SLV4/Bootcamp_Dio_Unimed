#if aninhado - é possível criar estruturas condicionais aninhadas, ou seja, um "if dentro do if (ou elif, etc)" bastando adicionar as demais condiçoes dentro do bloco a ser executado

conta_universitaria = False #inverter
conta_especial = True #adicionado ao final da aula 
conta_normal = False
saldo = 2000
saque = 2500 #alterar para 2500 e testar
cheque_especial = 450


if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso de cheque especial")
    else:
        print("Não foi possível realziar o saque! Saldo insuficiente")
elif conta_universitaria:
    if saldo >= saque:
        print ("Saque Realizado com sucesso")
    else:
        print("Não foi possível realizar o saque! Saldo insuficiente")
elif conta_especial:
    print("Conta especial selecionada")
else: 
    print("O sistema não reconheceu o tipo de conta! Entre em contato com o seu gerente.")

    