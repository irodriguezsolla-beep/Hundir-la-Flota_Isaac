from tablero import Tablero
class Juego:
    def __init__(self):
        self.lanzar_ataque(3,2)

    def lanzar_ataque(self,x,y):
        print(f'Ataque a {x},{y}')
        obj_tablero=Tablero()
        resultado =obj_tablero.comprobar_impacto(x,y)
        self.mostrar_resultado(resultado)
if __name__ =="__main__":
    Juego()