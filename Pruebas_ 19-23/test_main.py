import pytest
from prueba19 import registroTablaPosiciones
from prueba20 import registroJugadores
from prueba21 import registroLogros
from prueba22 import registroDescargarContenido
from prueba23 import CerrarSesion_Correcto

def test_registroTablaPosiciones():
    assert registroTablaPosiciones() == True

def test_registroJugadores():
    assert registroJugadores() == True

def test_registroLogros():
    assert registroLogros() == True

def test_registroDescargarContenido():
    assert registroDescargarContenido() == True
    
def test_CerrarSesion_Correcto():
    assert CerrarSesion_Correcto() == True
