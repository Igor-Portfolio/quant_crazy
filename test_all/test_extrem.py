from src.domain.motor import extrem, divide_interval, maximuns_minumus
import numpy as np
import pytest

def test_lista_com_varios_elementos():
    assert extrem([1, 2, 3, 4, 5]) == [1, 5]

def test_lista_com_dois_elementos():
    assert extrem([10, 20]) == [10, 20]

def test_lista_com_um_elemento():
    assert extrem([7]) is None

def test_lista_vazia():
    assert extrem([]) is None


def test_divisao_exata():
    assert divide_interval([1, 2, 3, 4, 5, 6], 2) == [[1, 2], [3, 4], [5, 6]]

def test_divisao_com_sobra():
    assert divide_interval([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 5) == [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10],
                                                                           [11, 12]]

def test_lista_menor_que_n():
    assert divide_interval([1, 2, 3], 5) is None

def test_com_numpy_array():
    # Convertendo o resultado para lista para o assert funcionar direto
    resultado = divide_interval(np.array([10, 20, 30, 40]), 2)
    resultado_lista = [list(x) for x in resultado]

    assert resultado_lista == [[10, 20], [30, 40]]


def test_maximuns_minumus_com_dez_elementos_x_e_y():
    # y vai ditar onde estão os picos e vales
    # Bloco 1: [10, 50, 20] -> Pico no 50 (índice 1) -> Deve pegar x[1] que é 99
    # Bloco 2: [30,  5, 40] -> Vale no 5   (índice 1) -> Deve pegar x[4] que é -50
    # Bloco 3: [15, 60, 25] -> Pico no 60 (índice 1) -> Deve pegar x[7] que é 88
    # Bloco 4: [100]        -> Sem extremos

    y = np.array([10, 50, 20, 30, 5, 40, 15, 60, 25, 100])
    x = np.array([0, 99, 0, 0, -50, 0, 0, 88, 0, 999])

    assert maximuns_minumus(x, y, 3) == [99, -50, 88]


def test_maximuns_minumus_tamanhos_diferentes_dispara_erro():
    x = np.array([1, 2, 3])
    y = np.array([1, 2])  # Tamanho diferente de x

    # O pytest valida se o ValueError realmente acontece
    with pytest.raises(ValueError, match="x and y must have same length, dont be dumy"):
        maximuns_minumus(x, y, 3)


def test_maximuns_minumus_lista_menor_que_n():
    x = np.array([1, 2])
    y = np.array([1, 2])

    assert maximuns_minumus(x, y, 5) is None