#01 - Faça um programa que receba quatro números inteiros, calcule e  mostre a soma desses números.
a = 8
b = 17
c = 32
d = 9
soma = a+b+c+d

print('Soma: ', soma)

#02 - Faça um programa que receba três notas, calcule e mostre a  média aritmética entre elas.
nota1 = 8
nota2 = 5
nota3 = 7
media = nota1+nota2+nota3

print('Média da nota: ', media / 3)

#3 - Faça um programa que receba três notas e seus respectivos  pesos, calcule e mostre a média ponderada dessas notas.
nota1 = float(input('Digite a primeira nota: '))
peso1 = float(input('Digite o primeiro peso: '))
nota2 = float(input('Digite a segunda nota: '))
peso2 = float(input('Digite o segundo peso: '))
nota3 = float(input('Digite a terceira nota: '))
peso3 = float(input('Digite o segundo peso: '))
calculo = nota1 * peso1 + nota2 * peso2 + nota3 * peso3
peso = peso1 + peso2 + peso3

print('Media ponderada: ', calculo / peso)

#4 - Faça um programa que receba o salário de um funcionário,  calcule e mostre o novo salário, sabendo-se que este sofreu um  aumento de 25%.
salario = float(input('Digite o seu salário: '))
reajuste = 25 / 100
novo_salario = salario * reajuste
salario_aumento = salario + novo_salario

print('O novo Salário fica: ', salario_aumento)

#05 Faça um programa que receba o salário de um funcionário e o  percentual de aumento, calcule e mostre o valor do aumento e o  novo salário.
salario = float(input('Digite o seu salário: '))
#aumento de 40%
reajuste = 40 / 100
novo_salario = salario * reajuste
salario_novo = salario + novo_salario

print('O reajuste seria de: ', novo_salario)
print('O Salário ficaria: ', salario_novo)


