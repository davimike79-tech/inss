dados = {
    "nome": ["Ana", "Bruno", "Carlos", "Diego", "Eduardo"],
    "salario_bruto": [2000, 3000, 4000, 5000, 6000]
}

#desconto INSS
def calcular_inss(salario_bruto):
   
    if salario_bruto <= 1320.00:
        return (salario_bruto * 7.5) / 100
    elif salario_bruto <= 2571.29:
        return (salario_bruto * 9) / 100 - 19.80
    elif salario_bruto <= 3856.94:
        return (salario_bruto * 12) / 100 - 96.94
    elif salario_bruto <= 7507.49:
        return (salario_bruto * 14) / 100 - 174.08
    else:
        return 876.97

#desconto IRPF
def calcular_irpf(salario_bruto, desconto_inss):
   
    base_calculo = salario_bruto - desconto_inss
    
    if salario_bruto <= 2259.20:
        return 0
    elif salario_bruto <= 2826.65:
        return (salario_bruto * 7.5 / 100) - 169.44
    elif salario_bruto <= 3751.05:
        return (salario_bruto * 15 / 100) - 381.44
    elif salario_bruto <= 4664.68:
        return (salario_bruto * 22.5 / 100) - 662.77
    else:
        return (salario_bruto * 27.5 / 100) - 896.00

#desconto vale transporte
def calcular_vale_transporte(salario_bruto):
    if salario_bruto <= 2000:
        return salario_bruto * 0.06
    else:
        return 0

# Cálculo do salário líquido
def calcular_salario_liquido(salario_bruto):
    inss = calcular_inss(salario_bruto)
    irpf = calcular_irpf(salario_bruto, inss)
    vale = calcular_vale_transporte(salario_bruto)
    
    salario_liquido = salario_bruto - inss - irpf - vale
    
    return {
        "salario_bruto": salario_bruto,
        "inss": inss,
        "irpf": irpf,
        "vale_transporte": vale,
        "salario_liquido": salario_liquido
    }

# Processando dados
print("=" * 70)
print("FOLHA DE PAGAMENTO")
print("=" * 70)

for nome, salario_bruto in zip(dados["nome"], dados["salario_bruto"]):
    resultado = calcular_salario_liquido(salario_bruto)
    
    print(f"\nFuncionário: {nome}")
    print(f"Salário Bruto:     R$ {resultado['salario_bruto']:>10.2f}")
    print(f"Desconto INSS:     R$ {resultado['inss']:>10.2f}")
    print(f"Desconto IRPF:     R$ {resultado['irpf']:>10.2f}")
    print(f"Vale Transporte:   R$ {resultado['vale_transporte']:>10.2f}")
    print("-" * 70)
    print(f"Salário Líquido:   R$ {resultado['salario_liquido']:>10.2f}")
    print("=" * 70)
