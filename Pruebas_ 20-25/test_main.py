import pytest
from prueba18 import iniciarjuego
from prueba19 import buscarjuegos
from prueba20 import agregarFavoritoSinSesionA
from prueba21 import crearUsuarioFavoritos
from prueba22 import agregarFavoritoSinSesionB
from prueba23 import verResultados

def test_agregarFavoritosSinSesionA():
    assert agregarFavoritoSinSesionA() == True

def test_agregarFavoritosSinSesionB():
    assert agregarFavoritoSinSesionB() == True

def test_iniciarjuego():
    assert iniciarjuego() == False

def test_crearUsuarioFavoritos():
    assert crearUsuarioFavoritos() == False

def test_verResultados():
    assert verResultados() == True

def test_buscarjuegos():
    assert buscarjuegos() == False







