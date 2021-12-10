class tablero():
    def __init__(self,num_filas,num_columnas,estado_celda):
        self.__num_filas= num_filas
        self.__num_columnas= num_columnas
        self.estado_celda= estado_celda

    def init_tablero(self):
        Tablero = [[0 for x in range(self.__num_filas)] for y in range(self.__num_columnas)]
        coord_y = 0
        coord_x = 0

    def estado_celda(self):
        for y in Tablero[]:
            for x in Tablero[y][]:
                if Tablero[y][x] == 0:
                    self.estado_celda = "Vacia"
                elif Tablero[y][x] == 1:
                    self.estado_celda = "Jugador"

    
    def imprimir_tablero(self):
        print()
t1=tablero(3,4)
t1.init_tablero()