class Strings:
    # metodo para verificar si una cadena es palindromo
    def es_palindromo(self, texto):
        texto = texto.lower().replace(" ", "")
        return texto == texto[::-1]

    # metodo para invertir una cadena sin slicing ni reversed
    def invertir_cadena(self, texto):
        resultado = ""
        for i in range(len(texto) - 1, -1, -1):
            resultado += texto[i]
        return resultado

    # metodo para contar vocales en una cadena
    def contar_vocales(self, texto):
        texto = texto.lower()
        vocales = "aeiou"
        contador = 0
        for letra in texto:
            if letra in vocales:
                contador += 1
        return contador

    # metodo para contar consonantes en una cadena
    def contar_consonantes(self, texto):
        texto = texto.lower()
        consonantes = "bcdfghjklmnpqrstvwxyz"
        contador = 0
        for letra in texto:
            if letra in consonantes:
                contador += 1
        return contador

    # metodo para verificar si dos cadenas son anagramas
    def es_anagrama(self, texto1, texto2):
        texto1 = sorted(texto1.replace(" ", "").lower())
        texto2 = sorted(texto2.replace(" ", "").lower())
        return texto1 == texto2

    # metodo para contar palabras en una cadena
    def contar_palabras(self, texto):
        palabras = texto.strip().split()
        return len(palabras)

    # metodo para poner en mayuscula la primera letra de cada palabra
    def palabras_mayus(self, texto):
        resultado = ""
        mayus = True
        for char in texto:
            if mayus and char.isalpha():
                resultado += char.upper()
                mayus = False
            else:
                resultado += char
            if char == " ":
                mayus = True
        return resultado

    # metodo para eliminar espacios duplicados
    def eliminar_espacios_duplicados(self, texto):
        resultado = ""
        espacio = False
        for char in texto:
            if char != " ":
                resultado += char
                espacio = False
            else:
                if not espacio:
                    resultado += char
                    espacio = True
        return resultado

    # metodo para verificar si una cadena representa un numero entero sin usar isdigit
    def es_numero_entero(self, texto):
        if not texto:
            return False
        if texto[0] == "-":
            texto = texto[1:]
        for char in texto:
            if char < "0" or char > "9":
                return False
        return True

    # metodo para cifrar una cadena usando cifrado cesar
    def cifrar_cesar(self, texto, desplazamiento):
        resultado = ""
        for char in texto:
            if char.isalpha():
                base = ord("A") if char.isupper() else ord("a")
                nueva = (ord(char) - base + desplazamiento) % 26 + base
                resultado += chr(nueva)
            else:
                resultado += char
        return resultado

    # metodo para descifrar una cadena cifrada con cesar
    def descifrar_cesar(self, texto, desplazamiento):
        return self.cifrar_cesar(texto, -desplazamiento)

    # metodo para encontrar todas las posiciones de una subcadena sin usar find ni index
    def encontrar_subcadena(self, texto, subcadena):
        posiciones = []
        largo_sub = len(subcadena)
        if largo_sub == 0:
            return []
        for i in range(len(texto) - largo_sub + 1):
            if texto[i:i + largo_sub] == subcadena:
                posiciones.append(i)
        return posiciones
