#Exercício 1 
#Um funcionário de uma empresa recebe aumento salarial anualmente.
#Sabe-se que:
#Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
#Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
#A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao
#dobro do percentual do ano anterior.
#Faça um programa que determine o salário atual desse funcionário.
#Após concluir isto, altere o programa permitindo que o usuário digite o salário
#inicial do funcionário.

ano_atual = int(input("Digite o Ano Atual: "))
sal_ini = 1000 #1995
perc = 1.5/100 #1996
novo_sal = sal_ini + perc*sal_ini

i = 1997
while i <= ano_atual:
  perc = 2 * perc
  novo_sal = novo_sal + perc * novo_sal
  i = i + 1

print("Salário Atual: R$  ", round(novo_sal, 2))

#Exercício 02
#Faça um programa que leia um valor N inteiro e positivo, calcule e mostre o valor de E, conforme a fórmula a seguir:
#E=1+1/1!+1/2!+1/3!+...1/N!

n = int(input("Digite o valor de n: "))
soma = 0
i = 1
while i <= n:
  soma = soma + i
  i = i + 1
  print("A soma dos", n, "primeiros inteiros positivos é", soma)

#Exercício 03
#Faça um programa que leia um número N e que indique quantos valores inteiros e positivos devem ser lidos a seguir. 
#Para cada número lido, mostre uma tabela contendo o valor lido e o fatorial desse valor.

n = int(input("Digite o valor de n: "))

for i in range(1, n + 1):
    num = int(input(f"Digite o {i}º número: "))
    fat = 1
    for j in range(1, num + 1):
        fat *= j
    print(f"O fatorial de {num} é: {fat}")