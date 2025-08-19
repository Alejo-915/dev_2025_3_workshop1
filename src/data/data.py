class Data:
    
    # metodo para invertir una lista sin usar slicing
    def invertir_lista(self, lista):
        resultado = []
        # recorro la lista desde el final hacia el inicio
        for i in range(len(lista) - 1, -1, -1):
            resultado.append(lista[i])
        return resultado

    # metodo para buscar un elemento en la lista
    def buscar_elemento(self, lista, elemento):
        # recorro elemento por elemento
        for i in range(len(lista)):
            if lista[i] == elemento:
                return i  # si lo encuentro devuelvo el indice
        return -1  # si no esta retorno -1

    # metodo para eliminar duplicados manteniendo el orden original
    def eliminar_duplicados(self, lista):
        resultado = []
        vistos = set()  # uso set para mejorar eficiencia
        for item in lista:
            if item not in vistos:
                resultado.append(item)
                vistos.add(item)
        return resultado

    # metodo para mezclar dos listas ordenadas en una sola lista ordenada
    def merge_ordenado(self, lista1, lista2):
        i, j = 0, 0
        resultado = []
        # comparo elementos de ambas listas mientras tengan valores
        while i < len(lista1) and j < len(lista2):
            if lista1[i] <= lista2[j]:
                resultado.append(lista1[i])
                i += 1
            else:
                resultado.append(lista2[j])
                j += 1
        # agrego lo que sobre de lista1
        resultado.extend(lista1[i:])
        # agrego lo que sobre de lista2
        resultado.extend(lista2[j:])
        return resultado

    # metodo para rotar una lista k posiciones a la derecha
    def rotar_lista(self, lista, k):
        if not lista:  # si esta vacia devuelvo lista vacia
            return []
        k = k % len(lista)  # ajusto k para que no sea mayor al tamano
        return lista[-k:] + lista[:-k]

    # metodo para encontrar el numero faltante en una secuencia 1..n
    def encuentra_numero_faltante(self, lista):
        n = len(lista) + 1  # el tamano real deberia ser n
        suma_esperada = n * (n + 1) // 2
        suma_actual = sum(lista)
        return suma_esperada - suma_actual

    # metodo para verificar si conjunto1 es subconjunto de conjunto2
    def es_subconjunto(self, conjunto1, conjunto2):
        return set(conjunto1).issubset(set(conjunto2))

    # implementacion de una pila con funciones internas
    def implementar_pila(self):
        pila = []

        def push(x):
            pila.append(x)

        def pop():
            return pila.pop() if pila else None

        def peek():
            return pila[-1] if pila else None

        def is_empty():
            return len(pila) == 0

        # devuelvo un diccionario con las operaciones
        return {"push": push, "pop": pop, "peek": peek, "is_empty": is_empty}

    # implementacion de una cola con funciones internas
    def implementar_cola(self):
        cola = []

        def enqueue(x):
            cola.append(x)

        def dequeue():
            return cola.pop(0) if cola else None

        def peek():
            return cola[0] if cola else None

        def is_empty():
            return len(cola) == 0

        # devuelvo un diccionario con las operaciones
        return {"enqueue": enqueue, "dequeue": dequeue, "peek": peek, "is_empty": is_empty}

    # metodo para calcular la transpuesta de una matriz
    def matriz_transpuesta(self, matriz):
        if not matriz:  # caso matriz vacia
            return []
        return [list(fila) for fila in zip(*matriz)]
