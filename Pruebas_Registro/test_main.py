import pytest
from prueba1 import registroCorreo
from prueba2 import registroCorreoFormatoInvalido
from prueba3 import registroCorreoVacio
from prueba4 import registroCorreoDuplicado
from prueba5 import registroUsuario
from prueba6 import registroUsuarioNumerico
from prueba7 import registroUsuarioVacio
from prueba8 import registroPassword
from prueba9 import registroPasswordCorto
from prueba10 import registroPasswordVacio

#print (registroCorreo())
def test_registroCorreo():
    assert registroCorreo() == True

def test_registroCorreoFormatoInvalido():
    assert registroCorreoFormatoInvalido() == False

def test_registroCorreoVacio():
    assert registroCorreoVacio() == True

def test_registroCorreoDuplicado():
    assert registroCorreoDuplicado() == True

def test_registroUsuario():
    assert registroUsuario() == True

def test_registroUsuarioNumerico():
    assert registroUsuarioNumerico() == True

def test_registroUsuarioVacio():
    assert registroUsuarioVacio() == True

def test_registroPassword():
    assert registroPassword() == True

def test_registroPasswordCorto():
    assert registroPasswordCorto() == True

def test_registroPasswordVacio():
    assert registroPasswordVacio() == True