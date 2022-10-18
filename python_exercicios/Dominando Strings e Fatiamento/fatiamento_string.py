
#Fatiamento de string
nome = "dinossauro com pena colorida"
print(nome[0])
print(nome [:9])
print(nome[10:])
print(nome[10:13])
print(nome[10:10:2])
print(nome[:])
print(nome[::-1])

#string em múltiplas linhas
nome = "dinossauro"

mensagem = f"""
"Olá, meu nome é {nome}. 
    Eu estou aprendendo Python"
"""
print(mensagem)

print(f""" 
      ######### MENU #########
      
      1 - DEPOSITAR
      2 - SACAR 
      0 - SAIR 
      
      Obrigado por usar o nosso sistema!
      
       ######### MENU ######### \n
      """)