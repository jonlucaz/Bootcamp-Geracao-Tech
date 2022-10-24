#metodos da classe list em python 

#append - adiciona novos elementos à uma lista

lista = ["Python"]
lista.append(1)
lista.append([3,4,5])
print(lista)

#copy - faz uma cópia da lista e as mudanças nesse novo arquivo não interfere na lista original

#clear - limpar a lista
lista.clear()
print(lista)

#extend - adiciona novos objetos em uma lista

linguagens = ["python", "js", "java"]
print(linguagens)
linguagens.extend(["csharp", "r"])
print(linguagens)

#index - saber onde aparece o objeto no indice pela primeira vez
print(linguagens.index("python")) #0

#pop - quando padrão remove o último item adicionado na lista -> exemplo da pilha de pratos
linguagens.pop()
print(linguagens)

#remove - funciona como o pop mas invés de colocar o indice a ser removido colocamos o elemento em si 
linguagens.remove("js")
print(linguagens)

#reverse - reverte a ordem do indice da lista
linguagens.reverse()
print(linguagens)

#sort - ordena a lista, por padrão em ordem alfabetica
linguagens.sort()
print(linguagens)