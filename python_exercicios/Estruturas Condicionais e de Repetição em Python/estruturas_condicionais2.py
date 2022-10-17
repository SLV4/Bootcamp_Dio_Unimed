#exemplo sistema CNH 

IDADE_ESPECIAL = 17
MAIOR_IDADE = 18
idade = int(input ("informe sua idade: \n"))
if idade >= MAIOR_IDADE:
    print("Maior idade, pode tirar a CNH")
else:
    print("Ainda não pode tirar a CNH")
    
#exemplo3 (IDADE_ESPECIAL)
idade = int(input ("informe sua idade: \n"))

if idade >= MAIOR_IDADE:
    print("Maior idade, pode tirar a CNH")
    
elif idade == 17:
    print("Pode fazer as aulas teóricas, porém não pode fazer as aulas práticas") 
else:
    print("Não pode tirar a CNH")


