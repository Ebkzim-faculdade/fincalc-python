import pytest

from fincalc import calcular_juros_compostos


def test_juros_compostos_valido():
    resultado = calcular_juros_compostos(1000.0, 5.0, 2)
    assert round(resultado, 2) == 1102.50


def test_juros_compostos_tempo_zero():
    resultado = calcular_juros_compostos(1000.0, 5.0, 0)
    assert round(resultado, 2) == 1000.00


def test_juros_compostos_capital_negativo():
    with pytest.raises(ValueError):
        calcular_juros_compostos(-500.0, 5.0, 2)


def test_juros_compostos_tempo_negativo():
    with pytest.raises(ValueError):
        calcular_juros_compostos(1000.0, 5.0, -1)
