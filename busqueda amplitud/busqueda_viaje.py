'''
Este codigo es para resolver un problema de buscar una ruta de viaje donde se pase por menos ciudades posibles con busqueda en amplitud
'''

from arbol import Nodo

def buscar_solucion(conexiones, estado_inicial, objetivo):
    solucionado = False
    '''
    nodos_visitados nos servira para saber que nodos hemos visto
    nodos_fronteras seran los nodos que vamos a visitar
    nodoInicial como su nombre indica es el nodo raiz y por el que empezara la "ramificacion" para encontrar el resultado
    '''
    nodos_visitados = []
    nodos_frontera = []
    nodoInicial = Nodo(estado_inicial)
    nodos_frontera.append(nodoInicial)

    while (not solucionado) and len(nodos_frontera) != 0:
        nodo = nodos_frontera.pop(0)
        nodos_visitados.append(nodo)

        if nodo.get_datos() == objetivo:
            # Hemos encontrado la solucion y nos lo devuelve
            solucionado = True
            return nodo

        else:
            dato_nodo = nodo.get_datos()
            # Creamos una lista donde vamos a añadir los hijos de cada nodo
            lista_hijos = []
            # Por cada nodo que hay en conexiones se va a recorrer sus hijos
            for un_hijo in conexiones[dato_nodo]:
                hijo = Nodo(un_hijo)
                # añadir hijo en lista hijos
                lista_hijos.append(hijo)
                # Si el hijo no esta ni en visitados ni en frontera, se añadira en la lista frontera
                if not hijo.en_lista(nodos_visitados) and not hijo.en_lista(nodos_frontera):
                    nodos_frontera.append(hijo)
        
        nodo.set_hijos(lista_hijos)

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
    estado_inicial = 'malaga'
    objetivo = 'santiago'
    resultado = []
    nodo_solucion = buscar_solucion(conexiones, estado_inicial, objetivo)
    nodo = nodo_solucion
    # Para obtener la solucion, hiremos de nodo.padre de cada hijo, y lo añadiremos a la lista resultado
    while nodo.get_padre() != None:
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre()
    resultado.append(estado_inicial)
    # Imprimimos la lista resultado al reves, para ver el recorrido que se hace des de el inicio al objetivo
    print(resultado[::-1])

