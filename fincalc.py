# FinCalc - Sistema de Cálculos Financeiros em Python


def calcular_juros_simples(
    capital: float,
    taxa_anual: float,
    anos: int
) -> float:
    """Calcula o montante final obtido por juros simples."""
    if capital < 0 or anos < 0:
        raise ValueError("Capital e tempo devem ser não negativos.")
    juros = capital * (taxa_anual / 100) * anos
    return capital + juros


def calcular_juros_compostos(
    capital: float,
    taxa_anual: float,
    anos: int
) -> float:
    """Calcula o montante final obtido por juros compostos."""
    if capital < 0 or anos < 0:
        raise ValueError("Capital e tempo devem ser não negativos.")
    montante = capital * ((1 + (taxa_anual / 100)) ** anos)
    return montante


def calcular_aposentadoria(
    patrimonio_atual: float,
    aporte_mensal: float,
    anos: int,
    taxa_anual: float
) -> float:
    """Calcula o patrimônio acumulado para aposentadoria."""
    if patrimonio_atual < 0 or aporte_mensal < 0 or anos < 0:
        raise ValueError("Patrimônio, aporte e tempo devem ser não negativos.")
    meses = anos * 12
    taxa_mensal = (taxa_anual / 100) / 12
    saldo = patrimonio_atual

    for _ in range(meses):
        saldo = (saldo + aporte_mensal) * (1 + taxa_mensal)

    return saldo


def calcular_irrf(salario_bruto: float) -> float:
    """Calcula a alíquota simplificada de Imposto de Renda Retido na Fonte."""
    if salario_bruto < 0:
        raise ValueError("O salário deve ser não negativo.")
    if salario_bruto <= 2259.20:
        return 0.0
    elif salario_bruto <= 2826.65:
        return (salario_bruto * 0.075) - 169.44
    elif salario_bruto <= 3751.05:
        return (salario_bruto * 0.15) - 381.44
    else:
        return (salario_bruto * 0.225) - 662.77


def calcular_parcela_price(
    valor_emprestimo: float,
    taxa_mensal: float,
    meses: int
) -> float:
    """Calcula o valor da parcela fixa em um financiamento pela Tabela Price."""
    if valor_emprestimo < 0 or meses <= 0:
        raise ValueError("Empréstimo e prazo devem ser válidos.")
    if taxa_mensal == 0:
        return valor_emprestimo / meses
    i = taxa_mensal / 100
    parcela = (
        valor_emprestimo
        * (i * ((1 + i) ** meses))
        / (((1 + i) ** meses) - 1)
    )
    return parcela


def calcular_valor_futuro(
    aporte_mensal: float,
    taxa_mensal: float,
    meses: int
) -> float:
    """Calcula o valor futuro acumulado com aportes mensais recorrentes."""
    if aporte_mensal < 0 or meses < 0:
        raise ValueError("Aporte e prazo devem ser não negativos.")
    if meses == 0:
        return 0.0
    if taxa_mensal == 0:
        return aporte_mensal * meses
    i = taxa_mensal / 100
    vf = aporte_mensal * (((1 + i) ** meses - 1) / i)
    return vf


def calcular_depreciacao_linear(
    valor_inicial: float,
    valor_residual: float,
    vida_util_anos: int
) -> float:
    """Calcula o valor de depreciação anual de um ativo corporativo."""
    if vida_util_anos <= 0:
        raise ValueError("A vida útil deve ser maior que zero.")
    if valor_residual > valor_inicial:
        raise ValueError("O valor residual não pode superar o valor inicial.")
    return (valor_inicial - valor_residual) / vida_util_anos


def converter_taxa_anual_para_mensal(taxa_anual: float) -> float:
    """Converte uma taxa de juros anual equivalente para taxa mensal."""
    if taxa_anual <= -100:
        raise ValueError("A taxa anual deve ser maior que -100%.")
    return (((1 + (taxa_anual / 100)) ** (1 / 12)) - 1) * 100


def calcular_margem_liquida(
    receita_total: float,
    custos_totais: float
) -> float:
    """Calcula a margem de lucro líquida percentual de uma operação."""
    if receita_total <= 0 or custos_totais < 0:
        raise ValueError("Receita e custos devem ser válidos.")
    lucro = receita_total - custos_totais
    return (lucro / receita_total) * 100


def calcular_rendimento_real(
    ganho_nominal: float,
    inflacao: float
) -> float:
    """Calcula a taxa de retorno real descontada a inflação do período."""
    if inflacao <= -100:
        raise ValueError("A inflação deve ser maior que -100%.")
    retorno_real = (
        (1 + (ganho_nominal / 100))
        / (1 + (inflacao / 100))
    ) - 1
    return retorno_real * 100
