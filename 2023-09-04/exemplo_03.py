from class_Pessoa_v2 import Pessoa

pessoa = Pessoa()

print(f'\nCPF...: {pessoa.CPF}')
print(f'Nome..: {pessoa.Nome}')
print(f'E-Mail: {pessoa.Email}')

pessoa.CPF   = '111.222.333-44'
pessoa.Nome  = 'Charles Cesar Magno de Freitas'
pessoa.Email = 'charles.freitas@ifrn.edu.br'

print(f'\nCPF...: {pessoa.CPF}')
print(f'Nome..: {pessoa.Nome}')
print(f'E-Mail: {pessoa.Email}')
