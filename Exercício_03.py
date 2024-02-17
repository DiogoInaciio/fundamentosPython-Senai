#Exercício 01
# A turma do colégio vai fazer uma excursão na serra e todos os alunos e monitores vão tomar um bondinho para subir até o pico de uma montanha.
# A cabine do bondinho pode levar 50 pessoas no máximo, contando alunos emonitores, durante uma viagem até o pico. 
#Neste problema, dado como entrada o número de alunos A e o número de monitores M, você deve escrever um programa que diga se é possível ou não levar todos os alunos e monitores em apenas uma viagem!

a = int(input('Digite a Quantidade de Alunos: '))
b = int(input('Digite a quantidade de Monitores:'))
c = 50
print('Alunos = ', a)
print('Monitores = ', b)
print('Quantidade máxima na cabine:', c)

if a + b < c:
  print('S, Será possível levar todos os alunos e monitores em apenas uma viagem! ')
else:
  print('N, Não será possível levar todos os alunos e monitores em apenas uma viagem! ')

#Exercício 02
#A nota final de um estudante é calculada a partir de três notas atribuídas respectivamente a um trabalho de laboratório, a uma avaliação semestral e a um exame final.
#A média das três notas mencionadas anteriormente obedece aos pesos a seguir:
#Nota Peso
#Trabalho de laboratório 2
#Avaliação semestral 3
#Exame final 5
#Faça um algoritmo que receba as três notas, calcule e mostre a média ponderada e o conceito segundo mostrado abaixo:
#Média Ponderada Conceito
#8,0 ●---● 10,0 ................................A
#7,0 ●---○ 8,0 ..................................B
#6,0 ●---○ 7,0 ..................................C
#5,0 ●---○ 6,0 ..................................D
#0,0 ●---○ 5,0 ..................................E
  
nota1 = float(input('Qual foi a nota do trabalho laborátorio: '))
peso1 = 2
nota2 = float(input('Qual foi a nota da Avaliação Semestral: '))
peso2 = 3
nota3 = float(input('Qual foi a nota do exame final: '))
peso3 = 5
calculo = (nota1 * peso1) + (nota2 * peso2) + (nota3 * peso3)
peso = peso1 + peso2 + peso3
print('Media ponderada: ', calculo / peso)
media_ponderada = float(calculo / peso)

if media_ponderada < 5:
  print('Você está no conceito E ')
elif media_ponderada <= 6:
  print('Você está no conceito D')
elif media_ponderada <= 7:
  print('Você está no conceito C')
elif media_ponderada <= 8:
  print('Você está no conceito B')
elif media_ponderada >= 9:
  print('Você está no conceito A')

#Exercício 03
#Faça um programa que receba: * o código de um produto comprado, supondo que a digitação do código do produto seja sempre válida, ou seja, um número inteiro entre 1 e 10; * o peso do produto em quilos; * o código do pais de origem, supondo que a digitação do código do pais seja sempre valida, ou seja, um número inteiro entre 1 e 3. Tabelas.
#Código do pais de origem Imposto 1 0% 2 15% 3 25% Código do Produto Preço pro grama 1 a 4 10 5 a 7 25 8 a 10 35 Calcule e mostre: a) O peso do produto convertido em gramas b) o preço total do produto comprado; c) o valor do imposto, sabendo-se que o imposto é cobrado sobre o preço total do produto comprado e que depende do país de origem; d) o valor total, preço total do produto mais imposto.


cod_prod = int(input("Informe o Código do Produto: "))
peso = float(input("Informe o Peso (KG): "))
cod_pais = int(input("Informe o Código do País: "))

#conversão de kg para gramas
peso_grama = peso * 1000
print("Peso do produto em Gramas: ", peso_grama)

#Preço Total do produto comprado
if (cod_prod >= 1) and (cod_prod <= 4):
  pre_grama = 10

if (cod_prod >= 5) and (cod_prod <= 7):
  pre_grama = 25

if (cod_prod >= 8) and (cod_prod <= 10):
  pre_grama = 35

pre_total = peso_grama * pre_grama
print("Preço Total do Produto $: ", pre_total)

#Calculo Imposto
if(cod_pais == 1):
  imposto = 0
if (cod_pais == 2):
  imposto = pre_total * 15/100
if(cod_pais == 3):
  imposto = pre_total * 25/100
print("O imposto será: ", imposto)

#Valor Total
valor_total = pre_total + imposto
print("Valor total da Compra: ", valor_total)

