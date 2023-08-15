
from library.Ship import Ship


class Cruise(Ship):
    def _chequearpassengers_(self):
        if self.passengers < 0:  # chequear que no sea negativo
            raise Exception("Error los pasajeros no pueden ser negativos")

    def _init_(self,passengers,draft,crew):
        Ship._init_(self, draft, crew) # llamo al costructor del padre
        self.passengers = passengers
        self._chequearpassengers_()
    def __is_worth_it(self):
        self.draft = self.draft-(self.crew*1.5) # cada tripulante agrega 1.5
        self.draft = self.draft-(self.passengers*2.25) # cada pasajero agrega 2.25
        if self.draft > 20:
            print("El barco merece ser saqueado!")
        else:
         raise Exception("Error de cantidad")

