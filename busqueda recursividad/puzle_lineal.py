from arbol import Nodo

def DFS_rec(nodo, solucion, visitados):
    visitados.append(nodo.get_datos())

    if nodo.get_datos() == solucion:
        return nodo
    else:
        dato_nodo = nodo.get_datos()
        hijo = [dato_nodo[1], dato_nodo[0], dato_nodo[2], dato_nodo[3]]
        hijo_izquierda = Nodo(hijo)
        hijo = [dato_nodo[0], dato_nodo[2], dato_nodo[1], dato_nodo[3]]
        hijo_central = Nodo(hijo)
        hijo = [dato_nodo[0], dato_nodo[1], dato_nodo[3], dato_nodo[2]]
        hijo_derecha = Nodo(hijo)
        nodo.set_hijos([hijo_izquierda, hijo_central, hijo_derecha])

        for nodo_hijo in nodo.get_hijos():
            if not nodo_hijo.get_datos() in visitados:
                s = DFS_rec(nodo_hijo, solucion, visitados)
                if s != None:
                    return s
        return None

if __name__ == "__main__":
    estado_inicial = [4,2,3,1]
    solucion = [1,2,3,4]
    nodo_solucion = None
    visitados = []
    nodo_inicial = Nodo(estado_inicial)
    nodo = DFS_rec(nodo_inicial, solucion, visitados)
    
    resultado = []
    while nodo.get_padre() != None:
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre()
    resultado.append(estado_inicial)
    print(resultado[::-1])