#conjuntos = set
#é uma coleção que não contém itens repetidos
#serve justamente para remover itens duplicados de uma lista

lista = [1, 3, 2, 4, 5, 3, 2, 4, 4, 4]
print(set(lista))

#muito útil
#não garante a ordem final
#pode usar parenteses ou chaves 
#conjuntos em python não suportam indexação e fatiamento 
#para acessar os seus valores é necessário converter para uma lista
numeros = {1, 2, 3, 4}
numeros = list(numeros)
print(numeros[1])


#métodos da classe set
#{}.union
conj_a = {1, 2}
conj_b = {3, 4}


print(conj_a.union(conj_b))

#{}.intersection
#o que está no conjunto A e também está no conjunto B

#{}.difference
#o que está no conjunto A mas não está no conjunto B

#{}symmetric_difference
#elementos que não estão na interseção dos dois conjuntos

#{}.issubset
#descobrir se um conjunto é subconjunto de outro - true or false - se for um subconjunto de outro irá apontar true

#{}.issuperset
#aponta exatamente o contrário do item acima, onde um irá dar true o outro irá apontar false

#{}.isdisjoint 
#aponta se um conjunto é totalmente indiferente a outro, quando todos os elementos do conjunto a NÃO estiverem no conjunto B irá apontar true

#{}.add 
#se um elemento não existir no conjunto, com o add ele sera adicionado
conj_a.add(7)
print(conj_a)

#{}.clear - irá limpar o conjunto

#{}.copy - irá fazer uma cópia do conjunto

#{}.discard - descartar um valor

#{}.pop - irá remover o item no indice 0
conj_a.pop()
print(conj_a)

#{}.remove - parecido com o discard, porém se o elemento que passarmos não existir ele irá aponta um erro

#len - apontará o tamanho da lista/conjunto

#in - para se um elemento consta no conjunto

