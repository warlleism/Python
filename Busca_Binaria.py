#Busca Binária

minha_lista = [11,23,32,45,56,67,78,57,1,3,7,5,4,59,68,35,24,34,465,76,24,34,62,12,41,42,43,54,65,120,102,150,104,200,3025,203,506,450]

minha_lista.sort()

def busca_binaria(lista, elemento_procurado):
    primeiro = 0
    ultimo = len(lista) - 1 ##Tamanho da lista = 6

    while primeiro <= ultimo:
        indice = (primeiro + ultimo) // 2
        elemento = lista[indice]

        if elemento < elemento_procurado:
            primeiro = indice + 1

        elif elemento > elemento_procurado:
            ultimo = indice - 1

        else:
            return indice
        
    return None

print(busca_binaria(minha_lista, 76))
