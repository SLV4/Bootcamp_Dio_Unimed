#abaixo se encontra a forma como eu refiz o desafio de código 1, para praticar outras funções de entrada e visualização dos dados no terminal:

distancia = int(input("Informe a distância entre os Palantír:  ")) #definir regra para o intervalo aceito entre a distancia (0 < N < 10000)
diametro1 = int(input("Informe o diametro do primeiro Palantír: ")) #definir regra para o intervalo aceito entre a distancia X e Y(0 < X, Y < 100)
diametro2 = int(input("Informe o diametro do segundo Palantír: ")) 
ICM = ((distancia /(diametro1 + diametro2)))

print (f"O valor do ICM encontrado entre as Palantír é: {ICM: .2f}") #exibir valor com duas casas decimais