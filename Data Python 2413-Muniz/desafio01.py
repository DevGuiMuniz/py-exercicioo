#atv 01
nome = input("Digite seu nome:")
print("Olá", nome, 'Prazer em te conhecer!' )
# ou
nome=input("Qual o seu nome")
print("Olá {}. Prazer em te conhecer".format(nome))
#ou
print(f"Ola {nome}. Prazer em te conhecer!")
#atv02

dia = input("Digite o seu dia do seu nascimento: ")
mes = input("Digite o mês do seu nascimento [Escreva em extenso]:")
ano = input("Digite o ano do seu nascimento:")
print(f"Você nasceu em  {dia} de {mes} de {ano}")

#atv03
num_01 = int(input("Digite o primeiro número:"))
num_02 = int(input("Digite o segundo número:"))

print(num_01 + num_02)