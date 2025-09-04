from collections import Counter
import math

class Stats:
    def promedio(self, numeros):
        return sum(numeros) / len(numeros) if numeros else 0


       def mediana(self, numeros):
        if not numeros:
            return 0
        numeros_ordenados = sorted(numeros)
        n = len(numeros_ordenados)
        mitad = n // 2
        if n % 2 == 0:
            return (numeros_ordenados[mitad-1] + numeros_ordenados[mitad]) / 2
        else:
            return float(numeros_ordenados[mitad])


       def moda(self, numeros):
        if not numeros:
            return None
        frecuencia = Counter(numeros)
        max_frecuencia = max(frecuencia.values())
        for num in numeros:
            if frecuencia[num] == max_frecuencia:
                return num

          def test_desviacion_estandar(self):
        assert round(self.stats.desviacion_estandar([1, 2, 3, 4, 5]), 2) == 1.41
        assert self.stats.desviacion_estandar([5, 5, 5]) == 0.0
        assert self.stats.desviacion_estandar([]) == 0



        def varianza(self, numeros):
        if not numeros:
            return 0
        return self.desviacion_estandar(numeros) ** 2

        def rango(self, numeros):
        if not numeros:
            return 0
        return max(numeros) - min(numeros)

