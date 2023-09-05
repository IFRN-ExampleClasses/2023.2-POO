from class_Pessoa_v1 import Pessoa

pessoa = Pessoa('111.222.333-44', 'Charles', 'charles.freitas@ifrn.edu.br')

print(f'\nCPF...: {pessoa.get_CPF()}')
print(f'Nome..: {pessoa.get_Nome()}')
print(f'E-Mail: {pessoa.get_Email()}')

pessoa.set_Nome('Charles Cesar Magno de Freitas')

print(f'\nCPF...: {pessoa.get_CPF()}')
print(f'Nome..: {pessoa.get_Nome()}')
print(f'E-Mail: {pessoa.get_Email()}')
