# Faça um Programa que converta metros para centímetros. Leia o valor em metros do usuário.

print("======CONVERSOR DE MEDIDAS======")
print("-----METROS ->> CENTÍMETROS-----")
print()
metros = float(input("Informe o valor em metros: "))

convert_for_centimeter = metros * 100

print(f"O valor digitado em metros: {metros}, equivale a {convert_for_centimeter} em centímetros.")
