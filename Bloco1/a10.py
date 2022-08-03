# Oswaldo irá receber um aumento salarial de 33%. 
# Faça um programa que pergunte o salário do usuário e calcule o salário aumentado 33%.

import time

print("\o/ ===AUMENTO DE SALÁRIO=== \o/")
print()

nome = str(input("Qual seu nome? "))
salario_atual = float(input("Por favor, informe quanto você ganha atualmente: "))
print("Fazendo juste salarial...")
time.sleep(1.0)
print("....")
time.sleep(2.0)

salario_ajustado = salario_atual + (salario_atual * 0.33)

print(f"Parabéns {nome}, o seu salário aumentou em 33% e agora você receberá R${salario_ajustado}")