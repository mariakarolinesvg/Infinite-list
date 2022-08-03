#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
#Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
#Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total

print("=== CASA DAS TINTAS ===")
print()

preço = 0
qtd_latas = 0
qtd_litros = 0

metros_quadrados = int(input("Por favor, informe em m² o tamanho da área a ser pintada: "))

if metros_quadrados > 0 and metros_quadrados <= 54 :
    qtd_latas = 1
    preço = qtd_latas * 80
    print("===============RECIBO===============")
    print(f"QUANTIDADE DE LATAS -- {qtd_latas}")
    print(f"VALOR A SER PAGO -- {preço}")

elif metros_quadrados > 54:
    qtd_litros = metros_quadrados / 3
    qtd_latas = qtd_litros /18
    preço = qtd_latas * 80

    print("===============RECIBO===============")
    print(f"QUANTIDADE DE LATAS -- {qtd_latas}")
    print(f"VALOR A SER PAGO -- {preço}")

print()