#tuplas
# "irmã" da lista, porém a tuplas é imutável já na lista o valor passado pode ser mudado
#exemplos
frutas = ('laranja', 'pera', 'uva',)
print(frutas)

letras = tuple('Python')

#como em tuplas usamos parenteses e parenteses é uma regra de precedencia em operações no python, usamos tuplas com números assim:

numeros = tuple([1,2,3,4])

#também pelo mesmo motivo que colocamos uma virgula no final da tupla em parenteses (quando declaramos ela diretamente)


#idexado igual nas listas
print(frutas[0])

#funciona igual com index negativo
#podemos também armazenar tuplas de todos tipos de objetos, inclusive tuplas de tuplas
#fatiamento também funciona do mesmo jeito

#métodos em tuplas
# ().count - quantos objetos tem na tupla
print(numeros.count(2))

# ().index - qual indice do objeto
print(numeros.index(2))

#len - tamanho total, quantidade total de objetos
print(len(numeros))