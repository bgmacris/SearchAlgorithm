'''
¡IMPORTANTE! ESTE ALGORITMO NO ES ADECUADO PARA ESTE PROBLEMA, ES PARA MOSTRAR LA DIFERENCIA.

Este codigo es para resolver un puzle lineal con busqueda en profundidad, tota la explicación se 
encuentra en el codigo de busqueda en amplietud. EL funcionamiento es casi igual que en la busqueda 
amplietud la diferencia esta en nodos_frontera, que funciona como Pila LIFO y no Cola FIFO
'''

from arbol import Nodo


def buscar_solucion_BFS(estado_inicial, solucion):
    solucionado = False
    nodos_visitados = []
    nodos_frontera = []
    nodoInicial = Nodo(estado_inicial)
    nodos_frontera.append(nodoInicial)

    while (not solucionado) and len(nodos_frontera) != 0:
        nodo = nodos_frontera.pop()
        nodos_visitados.append(nodo)

        if nodo.get_datos() == solucion:
            solucionado = True
            return nodo
        else:
            dato_nodo = nodo.get_datos()

            hijo = [dato_nodo[1], dato_nodo[0], dato_nodo[2], dato_nodo[3]]
            hijo_izquierda = Nodo(hijo)
            if not hijo_izquierda.en_lista(nodos_visitados) and not hijo_izquierda.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_izquierda)

            hijo = [dato_nodo[0], dato_nodo[2], dato_nodo[1], dato_nodo[3]]
            hijo_central = Nodo(hijo)
            if not hijo_central.en_lista(nodos_visitados) and not hijo_central.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_central)

            hijo = [dato_nodo[0], dato_nodo[1], dato_nodo[3], dato_nodo[2]]
            hijo_derecha = Nodo(hijo)
            if not hijo_derecha.en_lista(nodos_visitados) and not hijo_derecha.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_derecha)

            nodo.set_hijos([hijo_izquierda, hijo_central, hijo_derecha])


if __name__ == "__main__":
    estado_inicial = [4, 2, 3, 1]
    solucion = [1,2,3,4]
    nodo_solucion = buscar_solucion_BFS(estado_inicial, solucion)
    resultado = []
    nodo = nodo_solucion
    while nodo.get_padre() != None:
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre()
    resultado.append(estado_inicial)
    print(resultado[::-1])
