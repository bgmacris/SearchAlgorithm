# Parametros funcion buscar:
# Lista = lista de valores
# Key = valor que tiene que encontrar en lista
def search(lista, key):
    # "l" sera el punto inicial de la izquierda
    l = 0
    # "r" sera el punto final de la derecha
    r = len(lista) - 1

    while l <= r:
        # Calcular la mitad de la lista
        mid = (l + r) // 2
        if key > lista[mid]:
            # si "key" > "mid", el punto inicial "l" pasara a ser mid + 1
            # +1 porque el mid ya lo hemos comprovado.
            l = mid + 1
        elif key == lista[mid]:
            # Se a encontrado la "key" y la posicion en la que esta
            return key, mid + 1 
        else:
            # La "key" no esta en la lista
            r = mid - 1
        
    return -1
    
lista = [1, 5, 10, 30, 50, 67,220,300]
print(search(lista, 301))
