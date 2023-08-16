class Ship:
    static_cont=0
    def __init__(self, draft, crew):
        self.draft = draft # borrador: peso aprox del barco
        self.crew = crew  # cant de tripulantes a bordo
        self._chequear_()  # llamo a la funcion chequear
        Ship.static_cont+=1 #cuenta cuantos barcos hay

    def _chequear_(self):
        if self.draft < 0 or self.draft == 0:  # draft tiene que ser si o si positivo y distinto a cero
            raise Exception("Error de Borrador")
        if self.crew < 0 or self.crew == 0:  # crew tiene que ser si o si positivo y distinto a cero
            raise Exception("Error de Tripulacion")
        if not self.draft.isdecimal(): # chequea que sea un numero
            raise Exception("Error, el dato no es un numero")
        if not self.crew.isdecimal(): # chequea que sea un numero
            raise Exception("Error, el dato no es un numero")

    def is_worth_it(self):
        self.draft = self.draft - (self.crew * 1.5)
        if self.draft >= 20:
            print("El barco merece ser saqueado!")
            return True
        else:
            raise Exception("Error de cantidad")