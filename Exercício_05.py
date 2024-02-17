#Exercício 01
# Faça um programa que carregue um vetor de nove elementos númericos inteiros, calcule e mostre os números primos e suas respectivas posições.

num = []
i = 1
j = 0

for i in range (8):
   n = int(input('Digite um valor: '))
   num.append(n)
   cont = 0
   for j in range (1, n + 1):

    if n % j ==0:
      cont = cont + 1

   if cont <= 2:
      print(num[i])
      print(i)