# FinCalc

Projeto do Lab. 2 de testes unitários com Pytest.

Aluno: Eduardo Henrque Silva F  
Matrícula: 125111398154

## Execução

```bash
pip install -r requirements.txt
python -m pytest tests/ -v
flake8 fincalc.py tests/
bandit -r fincalc.py
python -m pytest --cov=fincalc --cov-report=term-missing tests/
```

Resultado local: 31 testes aprovados e 94% de cobertura.
