# Construa um algoritmo que leia dois números, faça a adição e caso o resultado seja maior que 20,
# apresentá-lo.

numero1 = float(input("Informe um número: "))
numero2 = float(input("Informe outro número: "))

soma = numero1 + numero2

if soma > 20:
    print(soma)
else: 
    print("A soma dos 2 números informados é menor ou igual a 20!")