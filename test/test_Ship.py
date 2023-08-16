import pytest
from library.Ship import Ship

def test_exception():

   assert Ship(33,-22) == "Error de Tripulacion"
   # with pytest.raises(Exception): Ship.is_worth_it()
