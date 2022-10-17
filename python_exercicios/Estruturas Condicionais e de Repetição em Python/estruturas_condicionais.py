#exemplo if / else
saldo = 2000.0
saque = float(input("informe o valor do saque: "))

if saldo >= saque:
    print("Realizando saque!")
else:
    print("Saldo insuficiente!")
    
#exemplo if/else/elif

opcao = int(input("informe uma opção: [1] Sacar \n[2] Extrato: \n"))

if opcao == 1:
    valor = float(input("informe a quantia para o saque: "))
elif opcao == 2:
    print("exibindo o extrato...\n")
    print(saldo)
else:
    print("Opção inválida")


    
    