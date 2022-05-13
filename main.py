alunos = int(input('Quantos alunos vc tem na turma? '))
materias = int(input('Quantas materias eles estudam? '))

mediaTurma = 0
for aluno in range(alunos):
    print('Aluno', aluno+1, ':')

mediaAluno = 0
for materia in range(materias):
    print('Nota da materia ', materia+1, ': ', end='')
    nota = float(input())
    mediaAluno += nota

    mediaAluno /= materias
    print(f'Média desse aluno, {mediaAluno:.2f},' ':', end='')

    mediaTurma += mediaAluno

    mediaTurma /= mediaAluno
    print(f'Média da Turma é, {mediaTurma:.2f}')



