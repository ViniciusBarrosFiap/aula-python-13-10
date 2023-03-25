# entrada de dados
salario = float(input("Digite seu salario: "))
quant_dependentes = int(input("Digite a quantidades de dependente: "))

salario += salario * 0.2  # aumento de 20%

# descontos
desconto_inss = salario * 0.11
ir = salario * 0.05
desconto_depen = 137.5 * quant_dependentes

salario_liq = salario - (desconto_inss + ir +
                         desconto_depen)  # salario liquido

# salario bruto
print(f"Seu salario bruto é: {salario}")

# salario liquido
print(f"Seu salario liquido é {salario_liq:.2f}")

# info dos descontos
print(f"Total de desconto de INSS: {desconto_inss:.2f}")
print(f"Total de desconto de IR:{ir}")
print(f"Total de desconto de plano de saúde: {desconto_depen}")
