#Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius. 

print("=== CONVERSOR DE TEMPERATURA ===")
print()

temp_f = int(input("Informe um valor qualquer de temperatura em Farenheit: "))

temp_for_celsius = (5 * (temp_f - 32)) / 9

print(f"Com base na temperatura fornecida, {temp_f} equivale a {temp_for_celsius} em graus Celsius.")
print()