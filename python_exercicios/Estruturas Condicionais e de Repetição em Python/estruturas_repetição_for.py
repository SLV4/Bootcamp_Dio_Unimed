#são estruturas utilizadas para rodar um código um determinado número de vezes. Esse valor pode ser pre determinado,
# ou pode ser determinado a partir de uma expressão lógica


#exemplo usando função iteravel
texto = input("Informe um texto: ")

VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=" ")
else:
    print() #adiciona quebra de linha 
    print("Executa no final do laço")
    

#exemplo utilizando range e list
for numero in range(0,51,5): #notar que a variável foi criada logo apos o "for" (sem ser declarada)
    print(numero, end= " ")
    
    