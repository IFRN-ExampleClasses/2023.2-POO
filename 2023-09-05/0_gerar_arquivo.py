import random, os

# ----------------------------------------------------------------------
# Gerando uma lista com 100.000 elementos 
# com valores entre 1 e 1.000.000 (pode haver números repetidos)
SIZELISTA = 10000
MINVALUE  = 1
MAXVALUE  = 1000000
lstValores = [random.randint(MINVALUE, MAXVALUE) for _ in range(SIZELISTA)]

# ----------------------------------------------------------------------
# Excrevendo a lista em um arquivo
DIRATUAL    = os.path.dirname(os.path.abspath(__file__)) 
NOMEARQUIVO = DIRATUAL + '\\valores_nao_ordenados.txt'
arquivo     = open(NOMEARQUIVO, 'w')
for i in lstValores: arquivo.write(f'{i}\n')
arquivo.close()