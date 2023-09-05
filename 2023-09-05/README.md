Bubble Sort:
...

Insertion Sort:
...

Selection Sort:
...

Merge Sort:
O Merge Sort é um algoritmo de ordenação eficiente que usa a estratégia "dividir para conquistar". Ele divide a lista em metades menores, ordena cada metade separadamente e, em seguida, combina as metades ordenadas para obter a lista final ordenada.

Quick Sort:
O Quick Sort também é um algoritmo "dividir para conquistar". Ele seleciona um elemento como pivô e rearranja a lista de forma que os elementos menores que o pivô fiquem à sua esquerda, e os elementos maiores, à direita. Em seguida, o Quick Sort é aplicado recursivamente às duas metades resultantes.

Pseudo-aleatório Quick Sort:
O Pseudo-aleatório Quick Sort é uma variação do Quick Sort que seleciona o pivô de forma pseudo-aleatória. Em vez de escolher sempre o primeiro ou o último elemento como pivô, o algoritmo escolhe um elemento aleatório entre o primeiro e o último elemento da lista. Essa abordagem ajuda a evitar casos de pior caso em que o Quick Sort tem desempenho ruim.

Heap Sort:
O Heap Sort utiliza uma estrutura de dados chamada heap para organizar os elementos. Ele constrói um heap máximo (ou mínimo) a partir da lista desordenada e, em seguida, extrai o elemento raiz repetidamente para obter a lista ordenada.

Shell Sort:
O Shell Sort é uma extensão do algoritmo de ordenação por inserção. Ele divide a lista em subgrupos menores usando um espaçamento chamado de lacuna e, em seguida, ordena cada subgrupo usando o algoritmo de inserção. Gradualmente, a lacuna é reduzida até que a lista inteira esteja ordenada.
O Shell Sort é um algoritmo de ordenação que é uma melhoria do Insertion Sort. Ele divide a lista em grupos menores de elementos chamados de "gaps" e ordena esses grupos usando o Insertion Sort. À medida que o algoritmo avança, os gaps são reduzidos até que sejam iguais a 1, e em seguida, é feita uma última passagem com o Insertion Sort para garantir que a lista esteja completamente ordenada.

Counting Sort:
O Counting Sort é um algoritmo de ordenação adequado para listas com elementos inteiros e com um intervalo relativamente pequeno. Ele conta o número de ocorrências de cada elemento e, em seguida, usa essas contagens para colocar os elementos na ordem correta.
O Counting Sort é um algoritmo de ordenação eficiente para listas de números inteiros com um intervalo conhecido. Ele funciona contando o número de ocorrências de cada elemento e, em seguida, recriando a lista ordenada com base nas contagens. É um algoritmo estável e não compara os elementos diretamente.

Radix Sort:
O Radix Sort é um algoritmo de ordenação que ordena os elementos com base nos dígitos individuais. Ele classifica os elementos da lista de acordo com cada posição do dígito, do dígito menos significativo ao dígito mais significativo.
O Radix Sort é um algoritmo de ordenação estável que classifica os elementos com base em seus dígitos individuais, começando pelo dígito menos significativo até o mais significativo. Ele é eficiente para ordenar números inteiros não negativos com um número fixo de dígitos.

Bucket Sort:
O Bucket Sort divide a faixa de valores da lista em um número fixo de "buckets" e distribui os elementos da lista nos respectivos buckets. Em seguida, cada bucket é ordenado individualmente, geralmente usando outro algoritmo de ordenação, ou recursivamente aplicando o Bucket Sort.
O Bucket Sort é um algoritmo de ordenação que divide a lista em intervalos chamados "buckets" e, em seguida, distribui os elementos nos buckets com base em seu valor. Cada bucket é então ordenado individualmente, e os elementos são concatenados na ordem correta para obter a lista ordenada final. O Bucket Sort é eficiente para dados distribuídos uniformemente.

Cocktail Shaker Sort (Cocktail Sort):
O Cocktail Shaker Sort é uma variação do Bubble Sort em que a ordenação ocorre em ambas as direções. Ele passa pela lista alternadamente da esquerda para a direita e da direita para a esquerda, trocando elementos adjacentes fora de ordem.
O Cocktail Sort é uma variação do Bubble Sort. Ele percorre a lista alternadamente da esquerda para a direita e da direita para a esquerda, trocando os elementos adjacentes que estão fora de ordem, semelhante a um movimento de "agitador de coquetel".

Comb Sort:
O Comb Sort é um algoritmo de ordenação que é semelhante ao Bubble Sort, mas usa um fator de redução maior. Isso permite que elementos distantes sejam movidos rapidamente para suas posições corretas, resultando em um desempenho melhorado em comparação com o Bubble Sort.
O Comb Sort é uma variação do Bubble Sort que visa superar a lentidão do Bubble Sort em arrays grandes. Ele utiliza um fator de redução (shrink factor) para determinar a distância entre os elementos que são comparados e trocados. À medida que o algoritmo avança, o fator de redução é gradualmente reduzido, permitindo que elementos distantes sejam comparados e trocados, o que melhora a eficiência do algoritmo.

Tim Sort:
O Tim Sort é um algoritmo de ordenação híbrido que combina os conceitos do Merge Sort e do Insertion Sort. Ele foi projetado para fornecer um bom desempenho em uma ampla variedade de casos, incluindo listas com elementos parcialmente ordenados ou com muitos elementos repetidos.
O Tim Sort é um algoritmo de ordenação híbrido baseado no Merge Sort e no Insertion Sort. Ele foi projetado para ter bom desempenho em diferentes tipos de dados e tamanhos de lista. O Tim Sort utiliza uma abordagem de divisão e conquista, combinando elementos em blocos ordenados e, em seguida, mesclando esses blocos até obter a lista totalmente ordenada.

Gnome Sort:
O Gnome Sort é um algoritmo de ordenação simples que funciona movendo elementos fora de ordem para sua posição correta. Ele faz isso comparando um elemento com o seu antecessor e, se estiverem fora de ordem, troca-os e move-se para trás na lista para verificar se o elemento anterior também está fora de ordem.
O Gnome Sort é um algoritmo de ordenação simples que funciona movendo um elemento para a sua posição correta em relação aos elementos anteriores. Ele faz isso comparando um elemento com o seu antecessor e, se estiver fora de ordem, troca-os. Em seguida, retrocede para comparar o elemento com o seu antecessor anterior, repetindo o processo até que o elemento esteja na posição correta.

Tree Sort:
O Tree Sort é um algoritmo de ordenação que constrói uma árvore binária de busca a partir dos elementos da lista e, em seguida, realiza um percurso em ordem na árvore para obter a lista ordenada.

Pigeonhole Sort:
O Pigeonhole Sort é um algoritmo de ordenação que é eficiente para listas onde o intervalo dos elementos é relativamente pequeno em comparação com o número total de elementos. Ele distribui os elementos da lista em "pigeonholes" (buracos de pombo) com base nos valores dos elementos e, em seguida, os coloca de volta na lista em ordem.

Cycle Sort:
O Cycle Sort é um algoritmo de ordenação eficiente que minimiza o número de escritas para a lista. Ele funciona identificando um item na posição correta e, em seguida, colocando todos os outros itens em suas posições corretas, ciclicamente.

Stooge Sort:
O Stooge Sort é um algoritmo de ordenação recursivo e in-place. Ele divide a lista em três partes: a primeira terço, a última terço e o terço restante. Em seguida, ele recursivamente ordena a primeira e a última terço, seguido por um processo de ordenação adicional no terço restante. É um algoritmo simples, mas não é eficiente para grandes listas.

Strand Sort:
O Strand Sort é um algoritmo de ordenação baseado em ordenação por fusão (merge sort) e lista encadeada. Ele divide a lista em sublistas ordenadas e, em seguida, mescla repetidamente essas sublistas até obter a lista totalmente ordenada. É um algoritmo de ordenação eficiente para listas encadeadas, mas pode não ser tão eficiente para estruturas de dados baseadas em arrays.

Pancake Sort
...

Bitonic Sort
...

Bogo Sort (também conhecido como Monkey Sort ou Permutation Sort)
...

