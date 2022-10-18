# Abaixo segue um exemplo de código que você pode ou não utilizar
#entrada = input().split()
#distancia = int(entrada[0])
#diametro1 = int(entrada[1])
#diametro2 = int(entrada[2])
#Todo: Calcule o ICM da comunicação dos Palatír de Sauron e Saruman, com 2 casas decimais no espaço #em branco abaixo:
#(0 < N < 10000), X e Y(0 < X, Y < 100)

     
distancia = int(input("Informe a distância entre os Palantír:  ")) #definir regra para o intervalo aceito entre a distancia (0 < N < 10000)
diametro1 = int(input("Informe o diametro do primeiro Palantír: ")) #definir regra para o intervalo aceito entre a distancia X e Y(0 < X, Y < 100)
diametro2 = int(input("Informe o diametro do segundo Palantír: ")) 
ICM = int((diametro1 + diametro2) // distancia) 

print ("O valor do ICM encontrado entre as Palantír é: {ICM}") #exibir valor com duas casas decimais

print(ICM)