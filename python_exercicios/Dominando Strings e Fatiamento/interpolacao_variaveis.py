#utilização old style %
nome = "Andrey"
idade = "28"
profissao = "Dev"
linguagem = "Python"
 
print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho com {} e estou matriculado no curso de {}.".format(nome, idade, profissao, linguagem))
print("Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho com {1} e estou matriculado no curso de {0}.".format(linguagem, idade, nome, profissao))
print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho com {trabalho} e estou matriculado no curso de {linguagem}.".format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))