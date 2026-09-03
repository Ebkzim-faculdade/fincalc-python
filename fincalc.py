# FinCalc - Sistema de Cálculos Financeiros em Python


def calcular_juros_simples(
    capital: float,
    taxa_anual: float,
    anos: int
) -> float:
    """Calcula o montante final obtido por juros simples."""
    juros = capital * (taxa_anual / 100) * anos
    return capital + juros


if __name__ == "__main__":
    print("Iniciando o sistema FinCalc...")

    patrimonio = calcular_aposentadoria(
        10000.0,
        500.0,
        20,
        6.0
    )

    print(
        f"Patrimônio Estimado para Aposentadoria: "
        f"R$ {patrimonio:.2f}"
    )

    montante = calcular_juros_simples(1000.0, 5.0, 2)
    print(f"Juros Simples: R$ {montante:.2f}")

    montante_comp = calcular_juros_compostos(1000.0, 5.0, 2)
    print(f"Juros Compostos: R$ {montante_comp:.2f}")