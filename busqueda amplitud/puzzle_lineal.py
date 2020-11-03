'''
Este codigo es para resolver un puzle lineal con busqueda en amplitud
'''

from arbol import Nodo

def buscar_solucion_BFS(estado_inicial, solucion):
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
        # Extraer nodo y añadirlo a visitado
        nodo = nodos_frontera.pop(0)
        nodos_visitados.append(nodo)
        
        if nodo.get_datos() == solucion:
            # Solucion encontrada
            solucionado = True
            return nodo
        else:
            # Expandir nodo hijo
            dato_nodo = nodo.get_datos()

            #Operador izquierda
            '''
            Operador izquierda lo que va ha hacer es cambiar la posicion 0 con la 1, [1,2,3,4] -> [2,1,3,4]
            En caso de que el hijo_izquierda no este ni en nodos_visitados ni en nodos_frontera lo añadiremos a nodos_frontera.
            '''
            hijo = [dato_nodo[1], dato_nodo[0], dato_nodo[2], dato_nodo[3]]
            hijo_izquierda = Nodo(hijo)
            if not hijo_izquierda.en_lista(nodos_visitados) and not hijo_izquierda.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_izquierda)
            
            #Operador central
            '''
            Operador central lo que va ha hacer es cambiar la posicion 1 con la 2, [1,2,3,4] -> [1,3,2,4]
            En caso de que el hijo_izquierda no este ni en nodos_visitados ni en nodos_frontera lo añadiremos a nodos_frontera.
            '''
            hijo = [dato_nodo[0], dato_nodo[2], dato_nodo[1], dato_nodo[3]]
            hijo_central = Nodo(hijo)
            if not hijo_central.en_lista(nodos_visitados) and not hijo_central.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_central)

            #Operador derecha
            '''
            Operador derecha lo que va ha hacer es cambiar la posicion 0 con la 1, [1,2,3,4] -> [1,2,4,3]
            En caso de que el hijo_izquierda no este ni en nodos_visitados ni en nodos_frontera lo añadiremos a nodos_frontera.
            '''
            hijo = [dato_nodo[0], dato_nodo[1], dato_nodo[3], dato_nodo[2]]
            hijo_derecha = Nodo(hijo)
            if not hijo_derecha.en_lista(nodos_visitados) and not hijo_derecha.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_derecha)

            # Asigna al nodo la lista de hijos de los operadores
            nodo.set_hijos([hijo_izquierda,hijo_central,hijo_derecha])

if __name__ == "__main__":
    estado_inicial = [4,2,3,1]
    solucion = [1,2,3,4]
    nodo_solucion = buscar_solucion_BFS(estado_inicial, solucion)
    resultado = []
    nodo = nodo_solucion
    while nodo.get_padre() != None:
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre()
    resultado.append(estado_inicial)
    print(resultado[::-1])
