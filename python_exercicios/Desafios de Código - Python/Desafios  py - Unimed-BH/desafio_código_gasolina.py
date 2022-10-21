entrada = input().split()
velocidade = int(entrada[0])
distancia = int(entrada[1])
gasolina = float((distancia * velocidade)/12)

print (f"{gasolina:.3f}")
