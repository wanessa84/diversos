alunos = []

while True:
    aluno = input('Digite nome do aluno:')
    alunos.append(aluno)

    resposta = input('Deseja cadastrar outro aluno? (s/n): ')
    if resposta.lower() !='s':
        break


print("\nlista de alunos cadastrados:")
for aluno in alunos:
    print(aluno)
    
        