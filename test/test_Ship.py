import pytest
from library.Ship import Ship

def test_exception():
    #Ship(33,22)
    with pytest.raises(Exception):
        Ship.is_worth_it()
