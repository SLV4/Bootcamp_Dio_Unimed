#utilização old style % #utilização .format e utilização "f"
#exemplo 1
nome = "Andrey"
idade = "28"
profissao = "Dev"
linguagem = "Python"

dados = {"nome": "Guilherme", "idade": 28}
Saldo = 45.435

print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho com {} e estou matriculado no curso de {}.".format(nome, idade, profissao, linguagem))
print("Olá, me chamo {0}. Eu tenho {3} anos de idade, trabalho com {2} e estou matriculado no curso de {1}.".format(linguagem, idade, nome, profissao))
#nomes trocados propositalmente acima 
print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho com {profissao} e estou matriculado no curso de {linguagem}.".format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))
print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho com {profissao} e estou matriculado no curso de {linguagem}.")

#exemplo 2
PI = 3.14159
print(f"valor de PI: {PI: .2f}")
print(f"Valor de PI: {PI: 10.2f}")

#voltando ao primeiro exemplo
print("Nome: %s Idade: %s" % (nome, idade))
print("Nome: {} Idade: {}" .format (nome, idade))
print("Nome: {1} Idade: {0}" .format (nome, idade))
print("Nome: {0} Idade: {1} Nome: {0}" .format (nome, idade))
print("Nome: {0} Idade: {1} Nome: {0}" .format (nome, idade))
print("Nome: {name} Idade: {age} Nome: {name}" .format (age=idade, name=nome))
print("Nome: {nome} Idade: {idade} .".format(**dados))
print(f"Nome: {nome} Idade: {idade}")
print(f"Nome: {nome} Idade: {idade} Saldo: {Saldo:10.2f}")
print(f"Nome: {nome} Idade: {idade} Saldo: {Saldo:.3f}")