import pytest

from fincalc import calcular_aposentadoria, calcular_juros_simples


def test_juros_simples_valido():
    assert calcular_juros_simples(1000.0, 5.0, 2) == 1100.0


def test_juros_simples_tempo_zero():
    assert calcular_juros_simples(1000.0, 5.0, 0) == 1000.0


def test_juros_simples_capital_negativo():
    with pytest.raises(ValueError):
        calcular_juros_simples(-1000.0, 5.0, 2)


def test_aposentadoria_valida():
    resultado = calcular_aposentadoria(10000.0, 500.0, 1, 6.0)
    assert round(resultado, 2) == 16815.40


def test_aposentadoria_tempo_zero():
    resultado = calcular_aposentadoria(10000.0, 500.0, 0, 6.0)
    assert resultado == 10000.0


def test_aposentadoria_aporte_negativo():
    with pytest.raises(ValueError):
        calcular_aposentadoria(10000.0, -500.0, 20, 6.0)
