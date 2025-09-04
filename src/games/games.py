import random

class Games:
    # metodo para determinar el ganador en piedra papel tijera
    def piedra_papel_tijera(self, jugador1, jugador2):
        reglas = {
            "piedra": "tijera",
            "tijera": "papel",
            "papel": "piedra"
        }
        jugador1 = jugador1.lower()
        jugador2 = jugador2.lower()
        if jugador1 not in reglas or jugador2 not in reglas:
            return "invalid"
        if jugador1 == jugador2:
            return "empate"
        elif reglas[jugador1] == jugador2:
            return "jugador1"
        else:
            return "jugador2"

    # metodo para dar pistas en juego de adivinar numero
        # metodo para dar pistas en juego de adivinar numero
    def adivinar_numero_pista(self, numero_secreto, intento):
        if intento == numero_secreto:
            return "correcto"
        elif intento > numero_secreto:
            return "muy alto"
        else:
            return "muy bajo"


    # metodo para verificar ganador en ta te ti
    def ta_te_ti_ganador(self, tablero):
        lineas = []

        # filas
        lineas.extend(tablero)

        # columnas
        for col in range(3):
            lineas.append([tablero[fila][col] for fila in range(3)])

        # diagonales
        lineas.append([tablero[i][i] for i in range(3)])
        lineas.append([tablero[i][2 - i] for i in range(3)])

        for linea in lineas:
            if linea[0] != " " and linea.count(linea[0]) == 3:
                return linea[0]

        # verificar si hay espacios vacios
        for fila in tablero:
            if " " in fila:
                return "continua"

        return "empate"

    # metodo para generar combinacion aleatoria de colores para mastermind
      # metodo para generar combinacion aleatoria de colores para mastermind
    def generar_combinacion_mastermind(self, longitud, colores_disponibles):
        resultado = []
        for _ in range(longitud):
            resultado.append(random.choice(colores_disponibles))
        return resultado


    # metodo para validar movimiento de torre en ajedrez
    def validar_movimiento_torre_ajedrez(self, desde_fila, desde_col, hasta_fila, hasta_col, tablero):
        # verificar limites del tablero
        if not (0 <= desde_fila < 8 and 0 <= desde_col < 8 and 0 <= hasta_fila < 8 and 0 <= hasta_col < 8):
            return False

        # no se puede quedar en la misma posicion
        if desde_fila == hasta_fila and desde_col == hasta_col:
            return False

        # movimiento horizontal
        if desde_fila == hasta_fila:
            paso = 1 if hasta_col > desde_col else -1
            for col in range(desde_col + paso, hasta_col, paso):
                if tablero[desde_fila][col] != " ":
                    return False
            return True

        # movimiento vertical
        if desde_col == hasta_col:
            paso = 1 if hasta_fila > desde_fila else -1
            for fila in range(desde_fila + paso, hasta_fila, paso):
                if tablero[fila][desde_col] != " ":
                    return False
            return True

        # si no es horizontal ni vertical, no es valido
        return False
