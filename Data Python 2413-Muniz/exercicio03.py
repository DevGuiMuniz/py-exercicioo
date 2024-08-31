#ex01
numInteiro = int(input("Digite o número para descobrir seu antecessor e sucessor"))
numAnt = (numInteiro - 1)
numSucessor = (numInteiro + 1)
print(f"O sucessor é {numSucessor} e o antecessor é {numAnt}")

#ex02

numInt = int(input("Digite um número e descubra seu dobro, triplo e sua raiz quadrada"))
numDobro = (numInt *2)
numTriplo = (numInt * 3)
numRaiz = (numInt **(1/2))

print(f"Pelo número digitado seu dobro é {numDobro} seu triplo é {numTriplo} e a raiz quadrada é {numRaiz}")

#ex03
nomeAluno = input("Digite o Nome do Aluno(a)")
notaUm = int(input("Digite a primeira nota:"))
notaDois = int(input("Digite a segunda nota:"))
media = (notaUm + notaDois)/2
print(f"A média do aluno(a) {nomeAluno} é : {media}" )

#ex04
numMetro = int(input("Digite o Número para fazer a conversão[em metros]"))
numCentimetro = (numMetro * 100)
numMilimetro = (numMetro * 1000)
print(f"O número {numMetro} convertido para Centimetros é {numCentimetro} e para milimetros é {numMilimetro}")
#ex05

numTabuada = int(input("Digite um valor inteiro para fazer a tabuada:"))

tabuadaNum = (numTabuada + 1)
print(f"{numTabuada * 0 }")
print(f"{numTabuada * 1 }")
print(f"{numTabuada * 2 }")
print(f"{numTabuada * 3 }")
print(f"{numTabuada * 4 }")
print(f"{numTabuada * 5 }")
print(f"{numTabuada * 6 }")
print(f"{numTabuada * 7 }")
print(f"{numTabuada * 8 }")
print(f"{numTabuada * 9 }")
print(f"{numTabuada * 10 }")

#ex06

dinheiroReal = float(input("Informe o dinheiro em Real que gostaria de converter"))
dinheiroDolar = (dinheiroReal / 5.61)
print(f"O valor convertido para dolar é: {dinheiroDolar}.")

#ex07

altura = float(input("Digite a altura da parede:"))
larg = float(input("Digite a largura da parede:"))
area = altura * larg
consumo = area /2
print(f"Você utilizará {consumo} litros de tinta")

#ex08

produto = input("Qual é o Produto?")
preco = float(input("Qual é o preço do produto?"))
desconto = preco * 0.05
valorFinal = preco - desconto
print(f"O valor cheio do {produto} e {preco}. foi aplicado um desconto de  {desconto} gereando um valor final de {valorFinal}")
