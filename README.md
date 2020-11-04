# SearchAlgorithm
Algoritmos de busqueda y resolucion de problemas.

# Busqueda Binaria
¡IMPORTANTE! Para que esta función sirva es necesario una lista donde los valores estén ordenados y sean secuencias numéricas que se puedan comparar.

Esta búsqueda nos permite buscar un elemento en una lista sin necesidad de iterar toda la lista.
Separando la lista en un punto iniciar y uno final, calculamos el valor medio de los puntos y lo comparamos con el valor que buscamos, y dependiendo si es mayor, menor o igual sabemos en que parte de la lista nos toca buscar.

# Busqueda amplitud
En este problema tenemos que resolver el puzle 1,2,3,4 que nos lo darán desordenado y otro problema de buscar la solucion de la mejor ruta para ir de un punto inicial al objetivo, y pasar por los minimos nodos posibles

arbol.py ->Utilizaremos la clase nodo, para administrar los nodos(construir un árbol genealógico).
puzle_lineal.py -> Sera el codigo que resuelve el problema del puzle, para crear los nodos utilizira 3 operadores, operador izquieda- operador central-operador derecha.

Operador izquierda: Operador izquierda lo que va ha hacer es cambiar la posicion 0 con la 1, [1,2,3,4] -> [2,1,3,4]
Operador central: Operador central lo que va ha hacer es cambiar la posicion 1 con la 2, [1,2,3,4] -> [1,3,2,4]
Operador derecha: Operador derecha lo que va ha hacer es cambiar la posicion 0 con la 1, [1,2,3,4] -> [1,2,4,3]

busqueda_viaje.py -> Es el codigo para resolver el problema del viaje.
