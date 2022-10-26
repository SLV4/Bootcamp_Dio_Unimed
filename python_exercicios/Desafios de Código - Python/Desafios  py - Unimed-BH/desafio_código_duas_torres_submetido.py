#Desafio de código submetido:
entrada = ['100,2,2']
entrada = input().split()
distancia = int(entrada[0])
diametro1 = int(entrada[1])
diametro2 = int(entrada[2])

# TODO: Calcule o ICM da comunicação dos Palatír de Sauron e Saruman, com 2 casas decimais no espaço #em branco abaixo:
ICM = ((distancia /(diametro1 + diametro2)))

print (f"{ICM: .2f}")
