#Exercício 1

#Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de
#trânsito. Foram obtidos os seguintes dados:
#	a.Código da cidade;
#	b.Número de veículos de passeio (em 1999);
#	c.Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
#	d.Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
#	e.Qual a média de veículos nas cinco cidades juntas;
#	f.Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

soma_veic = 0
soma_acid = 0
cont_acid = 0
maior_ind = 0
menor_ind = 0
#cont = contador
for cont in range (5):
  cod = int(input('Informe o Código da Cidade: '))
  num_veic = int(input('Informe o N° de veículos: '))
  num_acid = int(input('Informe o N° de acidentes: '))

  if cont == 1:
    maior_ind = num_acid
    cid_maiorind = cod
    menor_ind = num_acid
    cid_menorind = cod
else:
    if num_acid > maior_ind:
      maior_ind = num_acid
      cid_maiorind = cod
    if num_acid < menor_ind:
      menor_ind = num_acid
      cid_menorind = cod

soma_veic = soma_veic + num_veic
if num_veic < 2000:
  soma_acid = soma_acid + num_acid
  cont_acid = cont_acid + 1

print('/n/n')
print('Maior Indice: ', maior_ind,'Cidade: ', cid_maiorind)
print('Menor I?ndice: ', menor_ind, 'Cidade: ', cid_menorind)
print('/n/n')

media_veic = soma_veic / 5
print('Média de Veículos nas cinco cidades: ', media_veic)

if cont_acid == 0:
  print('Não foi digitado nenhuma cidade com menos de 2000 veiculos ')
else:
  media_acid = soma_acid / cont_acid
  print('Media de Acidentes: ', media_acid)

#Exercicio 2 
  
#Uma empresa possui dez funcionários com as seguintes características: código, número de horas trabalhadas no mês, turno de trabalho // (M – matutino; V – vespertino; N – noturno), categoria (O – operário; ou G – gerente), valor da hora trabalhada. Sabendo-se que 
#essa empresa deseja informatizar sua folha de pagamento, faça um programa que: a) Leia as informações dos funcionários, exceto o 
#valor da hora trabalhada, não permitindo que sejam informações dos turnos e nem categorias inexistentes. Trabalhe sempre com a 
#digitação de letras maiúsculas; b) Calcule o valor da hora trabalhada, conforme a tabela 1. Adote o valor de R$1412,00 para o 
#salário mínimo; c) Calcule o salário inicial dos funcionários com base no valor da hora trabalhada e no número de horas 
#trabalhadas; d) Calcule o valor do auxílio alimentação recebido pelo funcionário de acordo com seu salário inicial, conforme a 
#tabela 2; e) Mostre o código, número de horas trabalhadas, valor da hora trabalhada, salário inicial, auxílio alimentação e salário 
#final (salário inicial + auxílio alimentação).

sal_min = 1412
cont = 1

sal_min = 1412

for cont in range(10):
    cod = int(input("Informe o código do funcionário: "))
    nht = int(input("Informe o N° de Horas Trabalhadas: "))
    turno = input("Informe o Turno (M - V - N): ")
    cat = input("Informe a Categoria (O - G): ")
    while turno != 'M' and turno != 'V' and turno != 'N':
        turno = input("Informe o Turno (M - V - N): ")
    while cat != 'G' and cat != 'O':
        cat = input("Informe a Categoria (O - G): ")

    if cat == 'G':
        if turno == 'N':
            valor_ht = sal_min * 18/100
        else:
            valor_ht = sal_min * 15/100
    else:
        if turno == 'N':
            valor_ht = sal_min * 13/100
        else:
            valor_ht = sal_min * 10/100

    sal_inicial = nht * valor_ht

    if sal_inicial <= 600:
        aux_ali = sal_inicial * 20/100
    elif sal_inicial <= 1200:
        aux_ali = sal_inicial * 15/100
    else:
        aux_ali = sal_inicial * 5/100

    sal_final = sal_inicial + aux_ali

    print("Código do Funcionario: ", cod)
    print("Nº de Horas Trabalhadas: ", nht)
    print("Salário Inicial: R$", sal_inicial)
    print("Auxílio Alimentação: R$", aux_ali)
    print("Salário Final: R$", sal_final)

    cont = cont+1


    









