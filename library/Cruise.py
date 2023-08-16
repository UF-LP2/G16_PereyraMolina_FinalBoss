from library.Ship import Ship


class Cruise(Ship):
    def __init__(self, draft, crew, passengers):
        Ship.__init__(self, draft, crew) # llamo al constructor del padre
        self.passengers = passengers
        self._chequearpassengers_()

    def _chequearpassengers_(self):
        if self.passengers < 0:  # chequear que no sea negativo
            raise Exception("Error los pasajeros no pueden ser negativos")
        if not self.passengers.isdecimal(): # chequea que sea un numero
            raise Exception("Error, el dato no es un numero")

    def __is_worth_it(self):
        self.draft = self.draft-(self.crew*1.5) # cada tripulante agrega 1.5
        self.draft = self.draft-(self.passengers*2.25) # cada pasajero agrega 2.25
        if self.draft >= 20:
            print("El barco merece ser saqueado!")
            return True
        else:
            raise Exception("Error de cantidad")