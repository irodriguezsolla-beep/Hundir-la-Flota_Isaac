from nave import Nave
class Tablero:
    def __init__(self,casilla,tamanho,max_barco,min_barco):
        self.nave = Nave(nombre,tamanho)
        self.casilla = casilla
        self.tamanho = tamanho
        self.max = max_barco
        self.min = min_barco
        self.AGUA = 0

    def comprobar_impacto(self,x,y):
        print("Estoy comprobado el log")
        if self.casilla == 0:
            return self.AGUA
        else:
            self.nave.recibir_disparo()