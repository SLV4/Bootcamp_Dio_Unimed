saldo = 2000 #trocar
saque = 2500

status = "Sucesso" if saldo >= saque else "Falha"
print(f"{status} ao realizar o saque!")