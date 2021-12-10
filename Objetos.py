class Objeto:
    def __init__(self, nombre, posicion):
        self.nombre = nombre
        self.posicion = posicion

    def posicion_inicial(self):
        #Método vacío
        pass

    def moverse(self):
        #Método vacío
        pass
    
class lápiz(Objeto):
    def posicion_inicial(self):
        pass

class cuaderno(Objeto):
    def posicion_inicial(self):
        pass

class computador(Objeto):
    def posicion_inicial(self):
        pass

class pase_escolar(Objeto):
    def posicion_inicial(self):
        pass    

class persona(Objeto):
    def posicion_inicial(self):
        pass

    def moverse(self):
        pass
        

