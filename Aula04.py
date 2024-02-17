#teste de repetição 1
n = 0
while  (n < 10):
  print(n)
  n = n + 1

#Repetiçao 2
soma = 0.0
print('\n Somador - para encerrar digite o valor 0 (zero) \n ')
n = float(input('Digite um valor: '))
while (n != 0):
  soma = soma + n
  print('Total: ', soma)
  n = float(input('Digite um valor: '))
print('--FIM--[]')

#Repetição com laço for 1
for i in range (10):
  print(i)

#Repetiçaõ com laço for 2
for i in range (-10, 10):
 print(i)

#Repetição com laço for 3
for i in range (10, 21, 2):
 print(i) 

#Crie um programa que exiba todos os números ímpares entre 10 e 20
for i in range (11, 21, 2):
  print(i)

#Crie um programa para exibir todos os números múltiplos de 5 entre 5 e 50, incluindo 50
for i in range (5, 51, 5):
  print(i)

