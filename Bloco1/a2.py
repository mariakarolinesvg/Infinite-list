# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.

print("===CALCULANDO O SEU SALÁRIO===")
print()

valor_hora = float(input("Quanto você ganha por hora? "))
qtd_horas = int(input("Quantas horas você trabalha por mês? "))

valor_mensal = valor_hora * qtd_horas

print(f"Com base nas informações recebidas, seu salário mensal é de {valor_mensal}")

