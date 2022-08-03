# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.

#Menu
print("=== CONVERSOR DE TEMPERATURA ===")
print()

#Entrada
temp_c = int(input("Informe um valor qualquer de temperatura em Celsius: "))

#Processamento
temp_for_farenheit = (temp_c * 1.8) + 32

#Saída
print(f"Com base nas informações fornecidas, {temp_c}, em Farenheit corresponde a {temp_for_farenheit}.")
print()