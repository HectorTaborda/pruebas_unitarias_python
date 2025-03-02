import pytest
from biblioteca import Libro, Biblioteca

# Pruebas para la clase Libro
def test_libro_atributos():
    libro = Libro("1984", "George Orwell", 1949)
    assert libro.titulo == "1984"
    assert libro.autor == "George Orwell"
    assert libro.anio == 1949
    assert libro.prestado is False

def test_libro_str():
    libro = Libro("1984", "George Orwell", 1949)
    assert str(libro) == "1984 de George Orwell (1949) - disponible"
    libro.prestado = True
    assert str(libro) == "1984 de George Orwell (1949) - prestado"

# Pruebas para la clase Biblioteca
def test_agregar_libro():
    biblioteca = Biblioteca()
    libro = Libro("1984", "George Orwell", 1949)
    biblioteca.agregar_libro(libro)
    assert libro in biblioteca.libros

def test_eliminar_libro():
    biblioteca = Biblioteca()
    libro = Libro("1984", "George Orwell", 1949)
    biblioteca.agregar_libro(libro)
    biblioteca.eliminar_libro("1984")
    assert libro not in biblioteca.libros

def test_eliminar_libro_no_existente():
    biblioteca = Biblioteca()
    libro = Libro("1984", "George Orwell", 1949)
    biblioteca.agregar_libro(libro)
    biblioteca.eliminar_libro("Brave New World")
    assert len(biblioteca.libros) == 1

def test_buscar_libro_existente():
    biblioteca = Biblioteca()
    libro = Libro("1984", "George Orwell", 1949)
    biblioteca.agregar_libro(libro)
    assert biblioteca.buscar_libro("1984") == libro

def test_buscar_libro_no_existente():
    biblioteca = Biblioteca()
    assert biblioteca.buscar_libro("1984") is None

def test_listar_libros():
    biblioteca = Biblioteca()
    libro1 = Libro("1984", "George Orwell", 1949)
    libro2 = Libro("Brave New World", "Aldous Huxley", 1932)
    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)
    assert biblioteca.listar_libros() == ["1984 de George Orwell (1949) - disponible", "Brave New World de Aldous Huxley (1932) - disponible"]

def test_prestar_libro_disponible():
    biblioteca = Biblioteca()
    libro = Libro("1984", "George Orwell", 1949)
    biblioteca.agregar_libro(libro)
    resultado = biblioteca.prestar_libro("1984")
    assert resultado == "Has pedido prestado el libro '1984'."
    assert libro.prestado is True

def test_prestar_libro_prestado():
    biblioteca = Biblioteca()
    libro = Libro("1984", "George Orwell", 1949)
    biblioteca.agregar_libro(libro)
    biblioteca.prestar_libro("1984")
    resultado = biblioteca.prestar_libro("1984")
    assert resultado == "El libro '1984' ya está prestado."

def test_prestar_libro_no_existente():
    biblioteca = Biblioteca()
    resultado = biblioteca.prestar_libro("1984")
    assert resultado == "El libro '1984' no se encuentra en la biblioteca."

def test_devolver_libro_prestado():
    biblioteca = Biblioteca()
    libro = Libro("1984", "George Orwell", 1949)
    biblioteca.agregar_libro(libro)
    biblioteca.prestar_libro("1984")
    resultado = biblioteca.devolver_libro("1984")
    assert resultado == "Has devuelto el libro '1984'."
    assert libro.prestado is False

def test_devolver_libro_no_prestado():
    biblioteca = Biblioteca()
    libro = Libro("1984", "George Orwell", 1949)
    biblioteca.agregar_libro(libro)
    resultado = biblioteca.devolver_libro("1984")
    assert resultado == "El libro '1984' no estaba prestado."

def test_devolver_libro_no_existente():
    biblioteca = Biblioteca()
    resultado = biblioteca.devolver_libro("1984")
    assert resultado == "El libro '1984' no se encuentra en la biblioteca."
