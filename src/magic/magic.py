class Magic:
   

    def fibonacci(self, n: int) -> int:
        if n < 0:
            raise ValueError("n debe ser no negativo")
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    def fibonacci(self, n: int) -> int:
    if n < 0:
        raise ValueError("n debe ser no negativo")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

    def es_primo(self, n: int) -> bool:
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

       def generar_primos(self, n: int) -> list:
        if n < 2:
            return []
        primos = []
        for num in range(2, n + 1):
            if self.es_primo(num):
                primos.append(num)
        return primos


    def es_numero_perfecto(self, n: int) -> bool:
        if n <= 1:
            return False
        suma = 1
        i = 2
        while i * i <= n:
            if n % i == 0:
                suma += i
                if i * i != n:
                    suma += n // i
            i += 1
        return suma == n

    def triangulo_pascal(self, filas: int) -> list:
        if filas <= 0:
            return []
        tri = [[1]]
        for _ in range(1, filas):
            prev = tri[-1]
            fila = [1]
            for j in range(1, len(prev)):
                fila.append(prev[j - 1] + prev[j])
            fila.append(1)
            tri.append(fila)
        return tri

    def factorial(self, n: int) -> int:
        if n < 0:
            raise ValueError("n debe ser no negativo")
        res = 1
        for k in range(2, n + 1):
            res *= k
        return res

    def mcd(self, a: int, b: int) -> int:
        a, b = abs(a), abs(b)
        while b != 0:
            a, b = b, a % b
        return a

    def mcm(self, a: int, b: int) -> int:
        if a == 0 or b == 0:
            return 0
        return abs(a * b) // self.mcd(a, b)

    def suma_digitos(self, n: int) -> int:
        n = abs(n)
        s = 0
        if n == 0:
            return 0
        while n > 0:
            s += n % 10
            n //= 10
        return s

    def es_numero_armstrong(self, n: int) -> bool:
        if n < 0:
            return False
        s = str(n)
        p = len(s)
        total = sum(int(d) ** p for d in s)
        return total == n

    def es_cuadrado_magico(self, matriz: list) -> bool:
        # Debe ser matriz no vacía y cuadrada
        if not matriz or not all(isinstance(f, list) for f in matriz):
            return False
        n = len(matriz)
        if any(len(f) != n for f in matriz):
            return False

        # Suma objetivo: suma de la primera fila
        objetivo = sum(matriz[0])

        # Comprobar filas
        for fila in matriz:
            if sum(fila) != objetivo:
                return False

        # Comprobar columnas
        for c in range(n):
            if sum(matriz[r][c] for r in range(n)) != objetivo:
                return False

        # Comprobar diagonales
        if sum(matriz[i][i] for i in range(n)) != objetivo:
            return False
        if sum(matriz[i][n - 1 - i] for i in range(n)) != objetivo:
            return False

        return True
