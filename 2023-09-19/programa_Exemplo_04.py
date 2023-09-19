import os, sys

from class_Pessoa import Pessoa
from class_Aluno import Aluno

os.system('cls')

if __name__ == "__main__":

    alunos  = dict()
    pessoas = dict()

    cpfPessoa_1   = '111.222.333-44'
    nomePessoa_1  = 'Pessoa Hipotética #01'
    emailPessoa_1 = 'pessoa_1@email.com'

    cpfPessoa_2   = '555.666.777-88'
    nomePessoa_2  = 'Pessoa Hipotética #02'
    emailPessoa_2 = 'pessoa_2@email.com'

    pessoas[cpfPessoa_1] = Pessoa(cpfPessoa_1, nomePessoa_1, emailPessoa_1)
    pessoas[cpfPessoa_2] = Pessoa(cpfPessoa_2, nomePessoa_2, emailPessoa_2)

    print(pessoas,'\n')

    for cpf, pessoa in pessoas.items():
        print(f'Dados da Pessoa: {cpf}')
        print(f'{pessoa.dados}\n')


    print('\n','-'*100,'\n')

    alunos[cpfPessoa_1] = Aluno(cpfPessoa_1, '20232014050001', '01405', 'CNAT', pessoas[cpfPessoa_1])
    alunos[cpfPessoa_2] = Aluno(cpfPessoa_2, '20232014050002', '01405', 'SGA' , pessoas[cpfPessoa_2])
    alunos[cpfPessoa_1] = Aluno(cpfPessoa_1, '20232015000002', '01500', 'PAR' , pessoas[cpfPessoa_1])

    print(alunos,'\n')

    for matricula, aluno in alunos.items():
        print(f'Dados do Aluno: {matricula}')
        print(f'{aluno.dados}\n')
