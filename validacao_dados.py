# Aplique a validação de dados para que:
# O programa nunca seja interrompido por erro. A nota seja entre 0 e 10 e O número de faltas seja entre 0 e 20.

nome_aluno = input('Digite seu nome: ')

valid_nota = False
while valid_nota == False:
    prova1 = input('Digite a nota da prova 1: ')
    try:
        prova1 = float(prova1)
        if prova1 < 0 or prova1 > 10:
            print('Nota inválida. Valor deve ser entre 0 e 10.')
        else:
            valid_nota = True
    except:
        print("Nota inválida. Use apenas número e separe os decimento com ponto. (Ex: 9.5)")

valid_nota = False
while valid_nota == False:
    prova2 = input('Digite a nota da prova 2: ')
    try:
        prova2 = float(prova2)
        if prova2 < 0 or prova2 > 10:
            print('Nota inválida. Valor deve ser entre 0 e 10.')
        else:
            valid_nota = True
    except:
        print("Nota inválida. Use apenas número e separe os decimento com ponto. (Ex: 9.5)")

media = (prova1 + prova2) / 2

valid_faltas = False
while valid_faltas == False:
    faltas = input('Digite o total de faltas: ')
    try:
        faltas = float(faltas)
        if faltas < 0 or faltas > 20:
            print('Número de faltas inválida. Valor deve ser entre 0 a 20.')
        else:
            valid_faltas = True
    except:
        print("Número de faltas inválida. Use apenas número e separe os decimento com ponto. (Ex: 15.5)")

aulas = 20
frequencia = (((aulas - faltas) / aulas) * 100)

if frequencia >= 70 and media >= 6:
    resultado = 'Parabéns, aluno aprovado!'
elif frequencia < 70 and media < 6:
    resultado = 'Aluno reprovado por falta e nota!'
elif frequencia < 70 and media >= 6:
    resultado = 'Aluno reprovado por falta!'
else:
    resultado = 'Aluno reprovado por nota!'

print('Nome:', nome_aluno)
print('Média:', media)
print('Frequência:',frequencia, '%')
print('Resultado:', resultado)
