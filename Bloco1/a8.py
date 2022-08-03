# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
# 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# 1. salário bruto.
# 2. quanto pagou ao INSS.
# 3. quanto pagou ao sindicato.
# 4. o salário líquido.


#Entradas

nome = str(input("Por favor, informe seu nome: "))
valor_hora = int(input("Por favor, informe quanto você ganha por hora: "))
n_horas = int(input("Por favor, informe quantas horas você trabalha ao mês: "))

#Processamento
salario_bruto = valor_hora * n_horas
imposto_renda = (salario_bruto * 0.11)
inss = (salario_bruto * 0.08)
sindicato = (salario_bruto * 0.05)

salario_liquido = salario_bruto - (imposto_renda + inss + sindicato)

#Menu de escolha 

acesso = str(input("Deseja acessar aos dados? ")) 
   
while acesso == "sim" or acesso == "Sim":

    print("=====CONSULTA DE DADOS=====")
    print("(1)CONSULTAR SALÁRIO BRUTO")
    print("(2)CONSULTAR DESCONTO POR IMPOSTO DE RENDA")
    print("(3)CONSULTAR DESCONTO POR INSS")
    print("(4)CONSULTAR DESCONTO AO SINDICATO")
    print("(5)CONSULTAR SALÁRIO LÍQUIDO")
    print("(6)CONSULTAR LISTA COM TODAS AS INFOS")
        
    escolha = int(input("---Escolha a opção desejada (1, 2, 3, 4, 5, 6)---:  "))

    #Saídas
    if escolha == 1:
        print(f"O salário bruto do servidor {nome} é de R${salario_bruto}.")
    elif escolha == 2:
        print(f"O desconto por imposto de renda é dado em 11%.")
        print(f"Sendo assim, para o servidor informado o desconto é de R${imposto_renda}.")
    elif escolha == 3:
        print(f"O desconto por INSS é dado em 8%.")
        print(f"Sendo assim, para o servidor informado o desconto é de R${inss:.2f}.")
    elif escolha == 4:
        print(f"O desconto ao sindicato é dado em 5%.")
        print(f"Sendo assim, para o servidor informado o desconto é de R${sindicato:.2f}.")
    elif escolha == 5:
        print(f"O salário líquido do servidor {nome} é de R${salario_liquido}.")
    elif escolha == 6:
        print("=====DADOS DISPONÍVEIS NO SISTEMA=====")
        print(f"SERVIDOR ***{nome}***")
        print(f"SALÁRIO BRUTO --- {salario_bruto}")
        print(f"IMPOSTO DE RENDA --- {imposto_renda}")
        print(f"INSS --- {inss:.2f}")
        print(f"SINDICATO --- {sindicato:.2f}")
        print(f"SALÁRIO LÍQUIDO {salario_liquido}")
            
    else:
            print("Opção inválida, por favor informe a opção novamente.")

    acesso = str(input("Deseja acessar mais algum dado? "))



