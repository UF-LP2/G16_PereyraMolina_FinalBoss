import pytest
from library.Cargo import Cargo

def test_is_Cargo():
   ListaCargo: list[int, int, int, int]= [[44, 1, 22, 5],[2, 0.25,-1,0],[-33,0,-3,22],[15,0.5,33,9],['W','A','_','!'],[0,0,0,0]]
   with pytest.raises(Exception):
      for Cargo in ListaCargo:
         Cargo: Cargo=Cargo(Cargo[0], Cargo[1], Cargo[2], Cargo[3])
         Assert(Cargo.is_worth_it()>=20) == True