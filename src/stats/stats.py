from collections import Counter
import math

class Stats:
    def promedio(self, numeros):
        # si la lista esta vacia retorno 0 para evitar division por cero
        return sum(numeros) / len(numeros) if numeros else 0

    def mediana(self, numeros):
        # si la lista esta vacia retorno 0 como valor neutro
        if not numeros:
            return 0
        # ordeno los numeros para encontrar el valor central
        numeros_ordenados = sorted(numeros)
        n = len(numeros_ordenados)
        mitad = n // 2
        # si la cantidad es par promedio los dos del centro
        if n % 2 == 0:
            return (numeros_ordenados[mitad - 1] + numeros_ordenados[mitad]) / 2
        else:
            # si es impar retorno el valor central directamente
            return float(numeros_ordenados[mitad])

    def moda(self, numeros):
        # si la lista esta vacia no hay moda
        if not numeros:
            return None
        # uso counter para contar frecuencias
        frecuencia = Counter(numeros)
        max_frecuencia = max(frecuencia.values())
        # retorno el primer valor que tenga la frecuencia maxima
        for num in numeros:
            if frecuencia[num] == max_frecuencia:
                return num

    def desviacion_estandar(self, numeros):
        # si la lista esta vacia retorno 0 como desviacion nula
        if not numeros:
            return 0
        # calculo la media para usarla en la formula
        media = self.promedio(numeros)
        # sumo los cuadrados de las diferencias respecto a la media
        suma_cuadrados = sum((x - media) ** 2 for x in numeros)
        # aplico la raiz cuadrada sobre la media de los cuadrados
        return math.sqrt(suma_cuadrados / len(numeros))

    def varianza(self, numeros):
        # si la lista esta vacia retorno 0 como varianza nula
        if not numeros:
            return 0
        # la varianza es el cuadrado de la desviacion estandar
        return self.desviacion_estandar(numeros) ** 2

    def rango(self, numeros):
        # si la lista esta vacia no hay rango
        if not numeros:
            return 0
        # rango es la diferencia entre el maximo y el minimo
        return max(numeros) - min(numeros)
