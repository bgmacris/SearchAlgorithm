# SearchAlgorithm
Algoritmos de busqueda y resolucion de problemas.

# Busqueda Binaria
¡IMPORTANTE! Para que esta función sirva es necesario una lista donde los valores estén ordenados y sean secuencias numéricas que se puedan comparar.

Esta búsqueda nos permite buscar un elemento en una lista sin necesidad de iterar toda la lista.
Separando la lista en un punto iniciar y uno final, calculamos el valor medio de los puntos y lo comparamos con el valor que buscamos, y dependiendo si es mayor, menor o igual sabemos en que parte de la lista nos toca buscar.

# Busquedas amplietud-profundidad-recursiva
Todas las busquedas, son busquedas no informadas. Y itilizaremos el mismo ejemplo del puzle linea y viaje en avion, de esta manera podemos comprovar cual nos da la mejor solución.
Una solución optima en estos dos ejemplos es solucionar el problema con los minimos pasos posibles y recorriendo el minimo de niveles posibles del grifo.

# Buesqueda en amplietud
Esta busqueda lo que hace es desde el nodo principal ir decendiendo nivieles, por cada nivel se recorren todos los nodos hasta dar con la solución. 

Output puzle_linea:
[[4, 2, 3, 1], [2, 4, 3, 1], [2, 3, 4, 1], [2, 3, 1, 4], [2, 1, 3, 4], [1, 2, 3, 4]]

Output viaje:
['malaga', 'barcelona', 'santiago']

# Busqueda en profundidad
Esta busqueda recorre todo el grado de manera ordenada pero no uniforme, consiste en expandir todos los nodos que va localizando y recorrer de forma recurrente un camino concreto, cuando no quedan mas nodos en ese camino, regresa en el nodo anterior y repite el mismo proceso con los nodos hermanos.

Output:
[[4, 2, 3, 1], [4, 2, 1, 3], [4, 1, 2, 3], [4, 1, 3, 2], [4, 3, 1, 2], [3, 4, 1, 2], [3, 4, 2, 1], [3, 2, 4, 1], [3, 2, 1, 4], [3, 1, 2, 4], [1, 3, 2, 4], [1, 2, 3, 4]]
Esta no es una solución optima para este problema, ya que nosotros buscamos los minimos pasos para solucionar el problema.

# Busqueda recursiva
Si a la busqueda en profundida le aplicamos recursividad, conseguiremos menos uso de memoria RAM, ya que dejamos de utilizar la lista de nodos visitados. Pero eso no es del todo bueno, ya que el codigo se podria poner en un bucle infinito y no salir de alli.
Tanto si aplicamos recursividad como no, la solución con este metodo para este tipo de problemas solo seria eficaz si tenemos la suerte de encontrarla en los primeros nodos.

Output:
[[4, 2, 3, 1], [2, 4, 3, 1], [2, 3, 4, 1], [3, 2, 4, 1], [3, 4, 2, 1], [4, 3, 2, 1], [4, 3, 1, 2], [3, 4, 1, 2], [3, 1, 4, 2], [1, 3, 4, 2], [1, 4, 3, 2], [4, 1, 3, 2], [4, 1, 2, 3], [1, 4, 2, 3], [1, 2, 4, 3], [2, 1, 4, 3], [2, 1, 3, 4], [1, 2, 3, 4]]

# Busqueda profundidad limitada
Con limitar la busqueda en profundidad, podemos evidar que el programa se quede en bucle en algun nodo. En caso de no encontrar la solución devuelve None.

# Busqueda profundidad iterativa
Partiendo de esta mejora podemos conseguir, además, que el algoritmo sea optimo. La idea es ir repitiendo la busqueda de forma iterativa pero incrementando el nivel de profundidad en cada iteración.
En este caso utilizamos el problema de los aviones, que si os fijais es la misma salida que en busqueda amplietd. La solución es correcta ya que hace los minimos transbordos posibles para llegar a su meta.

Output:
['malaga', 'barcelona', 'santiago']


