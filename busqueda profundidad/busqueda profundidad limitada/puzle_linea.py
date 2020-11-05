from arbol import Nodo


def DFS_limitado(nodo, solucion, visitados, limite):
    if limite > 0:
        visitados.append(nodo)
        if nodo.get_datos() == solucion:
            return nodo
        else:
            dato_nodo = nodo.get_datos()
            lista_hijos = []
            for un_hijo in conexiones[dato_nodo]:
                hijo = Nodo(un_hijo)
                if not(hijo in visitados):
                    lista_hijos.append(hijo)

            nodo.set_hijos(lista_hijos)

            for nodo_hijo in nodo.get_hijos():
                if not nodo_hijo.get_datos() in visitados:
                    s = DFS_limitado(nodo_hijo, solucion, visitados, limite-1)
                    if s != None:
                        return s

        return None

def DFS_prof_iter(nodo, solucion):
    for limite in range(0,9):
        print(limite)
        visitados = []
        s = DFS_limitado(nodo, solucion, visitados, limite)
        if s != None:
            return s

if __name__ == "__main__":
    conexiones = {
        'malaga': {'salamanca', 'madrid', 'barcelona'},
        'sevilla': {'santiago', 'madrid'},
        'granada': {'valencia'},
        'valencia': {'barcelona', 'granada'},
        'madrid': {'salamanca', 'sevilla', 'malaga', 'barcelona', 'santander'},
        'barcelona': {'zaragoza', 'santiago', 'madrid', 'malaga', 'valencia'},
        'salamanca': {'malaga', 'madrid'},
        'santiago': {'sevilla', 'santander', 'barcelona'},
        'santander': {'santiago', 'madrid'},
        'zaragoza': {'barcelona'}
    }
    estado_inicial = 'santander'
    solucion = 'granada'
    nodo_inicial = Nodo(estado_inicial)
    nodo = DFS_prof_iter(nodo_inicial, solucion)

    if nodo != None:
        resultado = []
        while nodo.get_padre() != None:
            resultado.append(nodo.get_datos())
            nodo = nodo.get_padre()
        resultado.append(estado_inicial)
        print(resultado[::-1])
    else:
        print(None)