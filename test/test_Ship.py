import pytest
from library.Ship import Ship

def test_is_Ship():
   ListaShip: list[int, int]= [[22, 5],[-1,0],[0,-3],[50,33],['A','_'],[0,0]]
   with pytest.raises(Exception):
      for Ship in ListaShip:
         Ship: Ship=Ship(Ship[0], Ship[1])
         Assert(Ship.is_worth_it()>=20) == True
