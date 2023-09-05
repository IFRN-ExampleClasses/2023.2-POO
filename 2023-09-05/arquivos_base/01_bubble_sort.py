import time, os

print('\nExemplo de Ordenação utilizando o Método BUBBLE SORT...\n')

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
# Ordenando a lista usando o algoritmo BUBBLE SORT
print('\nIniciando a Ordenação...\n')
tInicial = time.time()

intSize = len(lstValores)
for i in range(intSize):
    for j in range(intSize - i - 1):
        if lstValores[j] > lstValores[j + 1]:
            lstValores[j], lstValores[j + 1] = lstValores[j + 1], lstValores[j]

tFinal = time.time()
dTime  = tFinal - tInicial

# ----------------------------------------------------------------------
# Excrevendo a lista em um arquivo
ARQUIVO_OUTPUT = DIRATUAL + '\\valores_ordenados.txt'
arquivo        = open(ARQUIVO_OUTPUT, 'w')
for i in lstValores: arquivo.write(f'{i}\n')
arquivo.close()


print(f'\nTempo de Execução: {dTime} segundos\n')
