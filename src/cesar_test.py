from codificacion import cifra_cesar

def test_cifra_cesar():
    assert cifra_cesar("abc",1) == "bcd"
    print("¡Todas las pruebas pasaron exitosamente!")

test_cifra_cesar()

