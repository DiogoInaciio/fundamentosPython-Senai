#exemplo de um vetor 1
medias = [5.5, 8.2, 0.9, 5.5, 10.0]
print(medias)

#exemplo de vetor 2
medias = [5.5, 8.0, 9.5, 10.0]
print("Vetor Completo: ", medias)
print("Cada elemento do Vetor separadamente!")
print("Indice 0: ", medias[0])
print("Indice 1: ", medias[1])
print("Indice 2: ", medias[2])
print("Indice 3: ", medias[3])

#Armazene em um vetor os  dias da semana
#Obs. Para armazenamento de textos, cada elemento deve vir entre aspas (" ")
dias = ["segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo"]
print(dias)

#Mostre o vetor inteiro e separado por elemento
dias = ["segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo"]

print(dias[0])
print(dias[1])
print(dias[2])
print(dias[3])
print(dias[4])
print(dias[5])
print(dias[6])

#Exemplo de Vetor 3
notas = []
print("Digite tres notas separadas por ENTER: ")
n = float(input("Informe a nota: "))
notas.append(n)
n = float(input("Informe a nota: "))
notas.append(n)
n = float(input("Informe a nota: "))
notas.append(n)
print("Notas: ", notas)

#Receba 4 notas, calcule a média, e mostre os valores (Vetor)
notas = []
print("Informe 4 notas separadas por ENTER!")
n = float(input("Digite uma nota: "))
notas.append(n)
n = float(input("Digite uma nota: "))
notas.append(n)
n = float(input("Digite uma nota: "))
notas.append(n)
n = float(input("Digite uma nota: "))
notas.append(n)
media = (notas[0] + notas[1] + notas[2] + notas[3]) / 4
print("Media: ", media)

#Vetor de Temperaturas
t = []
m = 0.0
print("Digite cinco aferições de temperaturas separadas por ENTER!")
for i in range (5):
  n = float(input("Informe a temperatura: "))
  t.append(n)
  m = m + t[i]

print("Media de temperaturas: ", round(m/5,2))


