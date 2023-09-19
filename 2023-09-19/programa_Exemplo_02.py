import os

from class_Pessoa import Pessoa
from class_Aluno import Aluno

os.system('cls')

if __name__ == "__main__":

    alunos = list()

    cpfPessoa_1   = '111.222.333-44'
    nomePessoa_1  = 'Pessoa Hipotética #01'
    emailPessoa_1 = 'pessoa_1@email.com'

    cpfPessoa_2   = '555.666.777-88'
    nomePessoa_2  = 'Pessoa Hipotética #02'
    emailPessoa_2 = 'pessoa_2@email.com'

    pessoa_1 = Pessoa(cpfPessoa_1, nomePessoa_1, emailPessoa_1)
    pessoa_2 = Pessoa(cpfPessoa_2, nomePessoa_2, emailPessoa_2)

    alunos.append(Aluno(cpfPessoa_1, '20232014050001', '01405', 'CNAT', pessoa_1))
    alunos.append(Aluno(cpfPessoa_2, '20232014050002', '01405', 'SGA', pessoa_2))
    alunos.append(Aluno(cpfPessoa_1, '20232015000002', '01500', 'PAR', pessoa_1))

    print(alunos,'\n')

    for aluno in alunos:
        print('Dados do Aluno:')
        print(f'{aluno.dados}\n')
