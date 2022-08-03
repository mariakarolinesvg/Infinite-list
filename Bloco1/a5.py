# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. 
# João precisa que você faça um programa que leia a variável peso (peso de peixes) e verifique se há excesso. 
# Se houver, gravar na variável excesso e na variável multa o valor da multa que João deverá pagar.

print("===VERIFICAÇÃO DE EXCESSO ===")
print()

excesso = 0
multa = 0
qtd_peixe = float(input("Informe a quantidade de peixes em Kg: "))

if qtd_peixe > 50:
    excesso = qtd_peixe - 50
    multa = excesso * 4

    print(f"Conforme o regulamento, todo excesso deve ser penalizado com multa.")
    print(f"Sendo assim, o Sr. deverá ser multado em R${multa}, pelo excesso de {excesso}Kgs.")

elif qtd_peixe == 0:
    print("Nenhum peso identificado, por favor insira um valor válido!")

else:
    print("Nenhum excesso identificado no peso descrito.")