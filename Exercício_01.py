#01, Imprima a frase"Ter sucesso é falhar repetidas vezes, mas sem perder o entusiasmo"
print("Ter sucesso é falhar repetidas vezes, mas sem perder o entusiasmo")

#02, Escreva um programa que receba o salário de um funcionário(float), e retorne o resultado do novo salário com reajuste de 35%.
salario = 1500.00
reajuste = 35 / 100
novo_salario = salario * reajuste
print('O aumento seria de: ',novo_salario)

#03, Faça um programa em linguagem Python que converta metros para centímetros. Obs: 1 metro = 100 centímetros.
metros = 5
centimetros = metros * 100
print('Em centimetros seria ', centimetros)

#03, Faça um programa em linguagem Python que converta metros para centímetros. Obs: 1 metro = 100 centímetros.
metros = 5
centimetros = metros * 100
print('Em centimetros seria ', centimetros)

#05 Faça um programa que leia um número e imprima seu antecessor e sucessor.
numero = int(input('Por favor, digite um numero: '))
print('Antecessor ',numero - 1)
print('Sucessor ', numero + 1)

#06 Faça um programa que leia nome, idade e sexo e imprima na tela.
first_name = str(input('Digite o seu nome: '))
age = int(input('Qual a sua idade: '))
sexo = str(input('Qual gênero você se identifica: '))
print('Olá me chamo', first_name,'tenho ', age, 'anos', 'e me considero do gênero', sexo,'.'   )

#07 Crie um algoritmo que leia dois números e mostre sua soma, subtração e divisão.
num1 = 10
num2 = 2
print('Soma:', num1 + num2)
print('Subtração:', num1 - num2)
print('divisão:', num1/num2)

#08 Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
num = int(input('Qual seria o número:'))
print('O número informado foi', num)

#09 Faça um programa que receba como entrada a altura de uma pessoa e calcule o peso ideal usando a seguinte fórmula:(72.7*altura)-58
altura = float(input('Qual a sua altura: '))
peso_ideal = (72.7*altura)-58
print('O peso ideal seria: ',  peso_ideal)

#10.Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos. Obs: 1 hora = 3600 segundos, 1 minuto = 60 segundos e 1 dia = 86400 segundos.
dias = 20 * 86400
horas = 480 * 3600
minutos = 28.800 * 60
print('Dias seria:',dias,'horas seria:',horas,'minutos seria',minutos)
