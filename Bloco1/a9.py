# Faça um Programa para uma loja de tintas. 
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00. 
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

#Entrada
tamanho_m2 = int(input("Por favor, informe em m² o tamanho da área que será pintada: "))

#Processamento
qtd_litros_necessario = tamanho_m2 / 6
#LATAS
qtd_latas = qtd_litros_necessario/18
preço_latas = qtd_latas * 80.0
#GALOES
qtd_galoes = qtd_litros_necessario/3.6
preço_galoes = qtd_litros_necessario*25.0

print()
print("===CASA DAS TINTAS===")
print()

acesso = str(input("Digite **sim** para prosseguir com a compra: ")) 
   
while acesso == "sim" or acesso == "Sim":

    print()
    print("=== MENU DE ESCOLHA ===")
    print("(1) APENAS LATAS DE 18L")
    print("(2) APENAS GALÕES DE 3,6L")

    escolha = int(input("Como deseja realizar a compra? [1, 2]:"))

    if escolha == 1:
        print("===============RECIBO===============")
        print(f"QUANTIDADE DE LATAS -- {qtd_latas:.2f}")
        print(f"VALOR A SER PAGO -- {preço_latas:.2f}")
    elif escolha == 2:
        print("===============RECIBO===============")
        print(f"QUANTIDADE DE GALÕES -- {qtd_galoes:.2f}")
        print(f"VALOR A SER PAGO -- {preço_galoes:.2f}")
    else:
        print("Opção inválida, por favor insira a opção novamente!")

    acesso = str(input("Deseja fazer mais alguma compra? "))

print("Obrigada pela compra! :)")