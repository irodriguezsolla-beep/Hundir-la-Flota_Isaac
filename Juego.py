from tablero import Tablero
class Juego:
    def __init__(self):
        resultado  = self.lanzar_ataque(3,2)
        self.mostrar_resultado(resultado)
    def lanzar_ataque(self,x,y):
        print(f'Ataque a {x},{y}')
        obj_tablero=Tablero()
        obj_tablero.comprobar_impacto(x,y)

if __name__ =="__main__":
    Juego()