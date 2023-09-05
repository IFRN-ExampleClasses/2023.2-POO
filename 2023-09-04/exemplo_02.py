from class_Pessoa_v2 import Pessoa

pessoa = Pessoa('111.222.333-44', 'Charles', 'charles.freitas@ifrn.edu.br')

print(f'\nCPF...: {pessoa.CPF}')
print(f'Nome..: {pessoa.Nome}')
print(f'E-Mail: {pessoa.Email}')

pessoa.Nome = 'Charles Cesar Magno de Freitas'

print(f'\nCPF...: {pessoa.CPF}')
print(f'Nome..: {pessoa.Nome}')
print(f'E-Mail: {pessoa.Email}')
