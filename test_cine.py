import pytest 
from cine import Pelicula

# Pruebas para la venta de entradas
def test_compra_exitosa():
    pelicula = Pelicula("Prueba", 10, 5)
    resultado = pelicula.vender_entradas(5)
    assert resultado == "Has comprado 5 entradas para Prueba. Total: $25"
    assert pelicula.asientos_disponibles == 5

def test_compra_insuficientes_asientos():
    pelicula = Pelicula("Prueba", 3, 5)
    resultado = pelicula.vender_entradas(5)
    assert resultado == "No hay suficientes asientos disponibles. Solo quedan 3 asientos."
    assert pelicula.asientos_disponibles == 3  # No debe cambiar

def test_compra_cero_entradas():
    pelicula = Pelicula("Prueba", 10, 5)
    resultado = pelicula.vender_entradas(0)
    assert resultado == "Has comprado 0 entradas para Prueba. Total: $0"
    assert pelicula.asientos_disponibles == 10  # No debe cambiar
