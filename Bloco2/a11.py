# Faça um programa para calcular o custo total de uma feira. 
# Considere que o feirante tem 3 produtos para vender. Cada produto tem um custo diferente. 
# Faça um programa no qual o usuário possa dizer o custo de seus produtos e o quanto de cada um ele vendeu e obtenha como resposta:
# O valor total da venda.
# Para cada item imprima: número de itens vendidos e lucro total daquele item.



print("===CALCULADORA DE LUCROS===")

custo_item1 = float(input("Por favor, informe o custo do produto número 1: "))
custo_item2 = float(input("Por favor, informe o custo do produto número 2: "))
custo_item3 = float(input("Por favor, informe o custo do produto número 3: "))

qtd_item1 = int(input("Quanto você vendeu do item 1? "))
qtd_item2 = int(input("Quanto você vendeu do item 2? "))
qtd_item3 = int(input("Quanto você vendeu do item 3? "))

valor_total = (custo_item1*qtd_item1) + (custo_item2*qtd_item2) + (custo_item3*qtd_item3)
lucro_item1 = custo_item1*qtd_item1
lucro_item2 = custo_item2*qtd_item2
lucro_item3 = custo_item3*qtd_item3
itens_vendidos = qtd_item1 + 

print("==========RECIBO==========")
print(f"VALOR TOTAL DA VENDA: {valor_total}")
print(f"NÚMERO DE ITENS VENDIDOS: {}")
print()
print()
print()


