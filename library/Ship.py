class Ship:
    def __init__(self, draft, crew):
        self.draft = draft # borrador: peso aprox del barco
        self.crew = crew  # cant de tripulantes a bordo
        self._chequear_()  # llamo a la funcion chequear
    def _chequear_(self):
        if self.draft < 0 or self.draft == 0:  # draft tiene que ser si o si positivo y distinto a cero
            raise Exception("Error de Borrador")
        if self.crew < 0 or self.crew == 0:  # crew tiene que ser si o si positivo y distinto a cero
            raise Exception("Error de Tripulacion")

    def is_worth_it(self):
        self.draft = self.draft - (self.crew * 1.5)
        if self.draft > 0:
            print("El barco merece ser saqueado!")
        else:
            raise Exception("Error de cantidad")
