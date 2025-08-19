class Conversion:
    def celsius_a_fahrenheit(self, celsius):
        # Fórmula: (C * 9/5) + 32
        return (celsius * 9/5) + 32
    
    def fahrenheit_a_celsius(self, fahrenheit):
        # Fórmula: (F - 32) * 5/9
        return (fahrenheit - 32) * 5/9
    
    def metros_a_pies(self, metros):
        # 1 metro = 3.28084 pies
        return metros * 3.28084
    
    def pies_a_metros(self, pies):
        # 1 pie = 0.3048 metros
        return pies * 0.3048
    
    def decimal_a_binario(self, decimal):
        # Uso bin() y quito el "0b"
        return bin(decimal)[2:]
    
    def binario_a_decimal(self, binario):
        # int con base 2 convierte binario a decimal
        return int(binario, 2)
    
    def decimal_a_romano(self, numero):
        # Tabla de valores romanos
        valores = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]
        resultado = ""
        for valor, simbolo in valores:
            while numero >= valor:
                resultado += simbolo
                numero -= valor
        return resultado
    
    def romano_a_decimal(self, romano):
        # Tabla romana
        valores = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        total = 0
        i = 0
        while i < len(romano):
            if i+1 < len(romano) and valores[romano[i]] < valores[romano[i+1]]:
                total += valores[romano[i+1]] - valores[romano[i]]
                i += 2
            else:
                total += valores[romano[i]]
                i += 1
        return total
    
    def texto_a_morse(self, texto):
        # Diccionario Morse
        morse = {
            "A":".-","B":"-...","C":"-.-.","D":"-..","E":".","F":"..-.",
            "G":"--.","H":"....","I":"..","J":".---","K":"-.-","L":".-..",
            "M":"--","N":"-.","O":"---","P":".--.","Q":"--.-","R":".-.",
            "S":"...","T":"-","U":"..-","V":"...-","W":".--","X":"-..-",
            "Y":"-.--","Z":"--..",
            "0":"-----","1":".----","2":"..---","3":"...--","4":"....-",
            "5":".....","6":"-....","7":"--...","8":"---..","9":"----."
        }
        texto = texto.upper()
        codigo = []
        for letra in texto:
            if letra == " ":
                codigo.append("/")  # espacio entre palabras
            elif letra in morse:
                codigo.append(morse[letra])
        return " ".join(codigo)
    
    def morse_a_texto(self, morse):
        morse_dic = {
            ".-":"A","-...":"B","-.-.":"C","-..":"D",".":"E","..-.":"F",
            "--.":"G","....":"H","..":"I",".---":"J","-.-":"K",".-..":"L",
            "--":"M","-.":"N","---":"O",".--.":"P","--.-":"Q",".-.":"R",
            "...":"S","-":"T","..-":"U","...-":"V",".--":"W","-..-":"X",
            "-.--":"Y","--..":"Z",
            "-----":"0",".----":"1","..---":"2","...--":"3","....-":"4",
            ".....":"5","-....":"6","--...":"7","---..":"8","----.":"9"
        }
        palabras = morse.split(" / ")  # separamos por palabras
        resultado = []
        for palabra in palabras:
            letras = palabra.split()
            palabra_texto = "".join([morse_dic[l] for l in letras if l in morse_dic])
            resultado.append(palabra_texto)
        return " ".join(resultado)
