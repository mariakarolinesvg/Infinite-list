# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos)

print("=====DOWNSTREAM=====")
print()

tamanho_arquivo = int(input("Por favor, informe o tamanho do arquivo (EM MB): "))
velocidade = float(input("Por favor, informe a velocidade da sua internet (EM Mbps): "))

convert_for_megabytes = velocidade/8
tempo_de_downloaded = tamanho_arquivo/convert_for_megabytes

print(f"De acordo com os dados fornecidos, o tempo de download será de {tempo_de_downloaded} min.")
print()
print("========================")

