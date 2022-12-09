import pytest
from prueba1 import fecha1
from prueba2 import fecha2
from prueba3 import fecha3
from prueba4 import fecha4

def test_fecha1():
    assert fecha1() == True
    
def test_fecha2():
    assert fecha2() == True
    
def test_fecha3():
    assert fecha3() == True

def test_fecha4():
    assert fecha4() == True