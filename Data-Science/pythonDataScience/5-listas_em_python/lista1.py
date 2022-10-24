#no pyhton podemos fazer listas com todos os tipos de objetos, todos na mesma lista
#formas de declarar listas:
#construtor list
#entre colchetes e separ'ados por virgulas [1,2,3] -> mais usada
frutas = ["limão", "maçã", "uva"]
print(frutas[0])

letras = list("Python")
print(letras[0])

#no python podemos também pegar os últimos itens da lista usando o indíce negativo
print(frutas[-1]) #uva

#listas aninhadas -> listas que armazenam outras listas
matriz = [[1, "a", 2],["b", 3, 4],[6, 5, "c"]]

print(matriz[0]) #primeira linha
print(matriz[0][0]) #primeira linha eprimeiro elemento


#fatiamento
lista = ["p", "y", "t", "h", "o", "n"]
print(lista[1:3])
printou = print(lista[0:3])

#enumerate - enumerando itens de uma lista de acordo com o indice
carros = ["gol", "celta", "palio"]
for indice, carro in enumerate (carros): 
  print(f'{indice}: {carro}')


#compreensão de lista - escolher itens de uma lista para outra de acordo com um filtro
numeros = [2, 4, 55, 39, 5363, 23, 240]
pares = []

for numero in numeros: 
  if numero % 2 == 0:
    pares.append(numero)
print(pares)