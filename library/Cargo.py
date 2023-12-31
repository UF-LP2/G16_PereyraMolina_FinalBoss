from library.Ship import Ship


class Cargo(Ship):
    def __init__(self, draft,crew, cargo, quality):
       Ship.__init__(self,draft,crew)  # llamo al constructor de ship padre
       self.cargo = cargo
       self.quality = quality
       self._chequearcargoquality_() #llamo a la funcion chequear

    def _chequearcargoquality_(self):
        if self.cargo < 0 or self.cargo == 0:
            raise Exception("Cargo negativo o igual 0 ")
        if self.quality != 1 and self.quality != 0.5 and self.quality != 0.25:
            # solo pueden ser estas opciones
            raise Exception("Calidad incorrecta")
        if not self.cargo.isdecimal():  # chequea que sea un numero
            raise Exception("Error, el dato no es un numero")

    def __is_worth_it(self):
        self.draft = self.draft-(self.crew*1.5) # cada tripulante agrega 1.5
        if self.quality == 1: # si calidad es 1 se agrega 3.5
            self.draft = self.draft+3.5
        if self.quality == 0.5: # si calidad es 0.5 se agrega 2
            self.draft = self.draft+2
        if self.quality == 0.25: # si calidad es 0.25 se agrega 0.5
            self.draft = self.draft+0.5
        if self.draft >= 20:
            print("El barco merece ser saqueado!")
            return True
        else:
            raise Exception("Error de cantidad")