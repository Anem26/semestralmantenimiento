import pytest
from prueba1 import iniciaSesion_Correcto
from prueba2 import iniciaSesion_ContraseñaInvalida
from prueba3 import iniciaSesion_emailInvalido
from prueba4 import iniciaSesion_vacio


#print (registroCorreo())
def test_iniciaSesion_Correcto():
    assert iniciaSesion_Correcto() == True

def test_iniciaSesion_ContraseñaInvalida():
    assert iniciaSesion_ContraseñaInvalida() == False
    
def test_iniciaSesion_emailInvalido():
    assert iniciaSesion_emailInvalido() == False
    
def test_iniciaSesion_vacio():
    assert iniciaSesion_vacio() == False