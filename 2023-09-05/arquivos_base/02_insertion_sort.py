import time, os

print('\nExemplo de Ordenação utilizando o Método INSERTION SORT...\n')

# ----------------------------------------------------------------------
# Montando a lista de valores a partir de um arquivo
print('\nMontando a lista...\n')
DIRATUAL      = os.path.dirname(os.path.abspath(__file__)) 
ARQUIVO_INPUT = DIRATUAL + '\\valores_nao_ordenados.txt'
arquivo       = open(ARQUIVO_INPUT, 'r')
lstValores    = list()
while True:
    valor = arquivo.readline()[:-1]
    if not valor: break
    lstValores.append(int(valor))
arquivo.close()

# ----------------------------------------------------------------------
# Ordenando a lista usando o algoritmo INSERTION SORT
print('\nIniciando a Ordenação...\n')
tInicial = time.time()

for i in range(1, len(lstValores)):
    key = lstValores[i]
    j = i - 1
    while j >= 0 and lstValores[j] > key:
        lstValores[j + 1] = lstValores[j]
        j -= 1
    lstValores[j + 1] = key

tFinal = time.time()
dTime  = tFinal - tInicial

# ----------------------------------------------------------------------
# Excrevendo a lista em um arquivo
ARQUIVO_OUTPUT = DIRATUAL + '\\valores_ordenados.txt'
arquivo        = open(ARQUIVO_OUTPUT, 'w')
for i in lstValores: arquivo.write(f'{i}\n')
arquivo.close()


print(f'\nTempo de Execução: {dTime} segundos\n')
