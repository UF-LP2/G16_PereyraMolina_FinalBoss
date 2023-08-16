import pytest
from library.Cruise import Cruise

def test_is_Cruise():
   ListaCruise: list[int, int, int]= [[33, 22, 5],[9,-1,0],[-33,0,-3],[15,50,33],['W','A','_'],[0,0,0]]
   with pytest.raises(Exception):
      for Cruise in ListaCruise:
         Cruise: Cruise=Cruise(Cruise[0], Cruise[1], Cruise[2])
         Assert(Cruise.is_worth_it()>=20) == True