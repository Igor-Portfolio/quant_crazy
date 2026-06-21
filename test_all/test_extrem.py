from src.domain.motor import extrem

def test_lista_com_varios_elementos():
    assert extrem([1, 2, 3, 4, 5]) == [1, 5]

def test_lista_com_dois_elementos():
    assert extrem([10, 20]) == [10, 20]

def test_lista_com_um_elemento():
    assert extrem([7]) is None

def test_lista_vazia():
    assert extrem([]) is None