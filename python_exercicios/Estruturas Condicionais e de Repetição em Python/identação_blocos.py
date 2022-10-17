#identar código é uma forma de manter o código fonte mais legícel e manutenível. Em python, há porém uma segunda função
#através da identação, o interpretador consegue determinar onde um bloco inicia e onde ele termina. 

def sacar(valor: float):
    saldo = 500

    if saldo >= valor:   #abordado somente o conceito de identação. Ignorar o conceito função "if"
        print("valor sacado!")     
        print("retire o seu dinheiro na boca do caixa.")           
    print("Obrigado por ser nosso cliente, tenha um bom dia!")
sacar(100)


def depositar(valor):
    saldo = 500
    saldo+= valor

sacar(1000)