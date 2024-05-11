# inicialização da variável onde será o valor de similiaridade
# iterador [i] no 1o elemento do array
# outro iterador [j] que vai percorrer o resto da array (até ao final do array)
# condição onde 1 elemento é maior que os outros elementos do array **
# ** e a posicao do iterador j é maior que o iterador i
# similiaridade incrementa
# retorna o valor de similiaridade
#%%
def filtro_colaborativo_bruteforce(arr):
    similarity = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j] and i < j :
                similarity += 1
    return similarity
#%%
print("similarity with brute force:",filtro_colaborativo_bruteforce([5,4,3,2,1]))

#--------------------------------------

# passa se um array , o indice inicial , o indice final
# se esse array tiver um elemento ou menos entao retorna 0 (caso base)
# se nao , calcula o index onde se encontra a metade do array
# vai se dividindo até ficar 1 elemento
# ( ao dividir se o array se for ímpar , o mais à direita é o que fica com + elemento (mid+1))
# ao juntar-se depois os elementos vai verificando se o mais à esquerda > mais à direita , se for , troca a posicao e a similiriadade +=1
# se nao , nao troca
# %%
def merge(arr, start, mid, end):
    left_arr = arr[start:mid + 1]
    right_arr = arr[mid + 1:end + 1]
    i = j = k = 0
    similarity = 0

    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] > right_arr[j]:
            arr[start + k] = right_arr[j]
            similarity += (mid + 1) - (start + i)
            j += 1
        else:
            arr[start + k] = left_arr[i]
            i += 1
        k += 1

    while i < len(left_arr):
        arr[start + k] = left_arr[i]
        i += 1
        k += 1

    while j < len(right_arr):
        arr[start + k] = right_arr[j]
        j += 1
        k += 1

    return similarity


def mergesort(arr, start, end):
    if start < end:
        mid = (start + end) // 2
        similarity = 0

        similarity += mergesort(arr, start, mid)
        similarity += mergesort(arr, mid + 1, end)
        similarity += merge(arr, start, mid, end)

        return similarity
    else:
        return 0



def filtro_colaborativo_divideconquer(array):
    return mergesort(array, 0, len(array) - 1)


# %%
print("similarity with divide & conquer:", filtro_colaborativo_divideconquer([5, 4, 3, 2, 1]))



# Parametros:
#   -> array de inteiros
# Descrição:
#   -> se a length da array for < 1 entao retorna 0 , se nao
#   -> calcula o elemento que se encontra a metade do array
#   -> a cada metade chama recursivamente pelo filtro_colaborativo_mergesort
#   -> e a cada chamada da funcao incrementa a variavel similitary de forma a contar as inversões
# Output:
#   -> retorna o valor de similiaridade
#%%
def merge(arr, start, mid, end):
    left_arr = arr[start:mid + 1]
    right_arr = arr[mid + 1:end + 1]
    i = j = k = 0
    similarity = 0

    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] > right_arr[j]:
            arr[start + k] = right_arr[j]
            similarity += (mid + 1) - (start + i)
            j += 1
        else:
            arr[start + k] = left_arr[i]
            i += 1
        k += 1

    while i < len(left_arr):
        arr[start + k] = left_arr[i]
        i += 1
        k += 1

    while j < len(right_arr):
        arr[start + k] = right_arr[j]
        j += 1
        k += 1

    return similarity


def filtro_colaborativo_mergesort(arr, start, end):
    if start < end:
        mid = (start + end) // 2
        similarity = 0

        similarity += filtro_colaborativo_mergesort(arr, start, mid)
        similarity += filtro_colaborativo_mergesort(arr, mid + 1, end)
        similarity += merge(arr, start, mid, end)

        return similarity
    else:
        return 0