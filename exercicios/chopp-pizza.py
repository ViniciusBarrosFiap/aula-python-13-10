# Em uma pizzaria, cada tulipa de chopp custa
# R$19,80 e uma pizza mista grande custa R$49,00
# mais R$2,50 por tipo de cobertura pedida (queijo,
# presunto, banana, etc.). Uma turma vai à pizzaria e
# pede uma determinada quantidade de "chopps" e
# uma determinada quantidade de pizzas grande com
# uma determinada quantidade de coberturas. FUPQ
# calcule a conta e, sabendo quantas pessoas estão à
# mesa, quanto que cada um deve pagar (não esqueça
# git os 10% do garçom)

# preco dos itens
choppe_preco = 19.8
pizza_preco = 49
preco_corbertura = 2.5

# input da quantidade dos itens e pessoas
choppe = int(input("Quantidade de chopp's pedidos: "))
pizza = int(input("Quantidade de pizza pedida: "))
cobertura = int(input("Quantidade de cobeerturas pedidas: "))
pessoas = int(input("Quantas pessoas estão na mesa: "))
# soma total da conta com os 10% de atendimento
conta = (choppe_preco * choppe) + (pizza_preco * pizza) + \
    (preco_corbertura * cobertura)

conta_total = (conta * 0.1) + conta

# divide a conta
conta_dividida = conta_total / pessoas

print(f"O total da conta foi R${conta_total :.2f}")
print(f"Preço por pessoa: R${conta_dividida :.2f}")
