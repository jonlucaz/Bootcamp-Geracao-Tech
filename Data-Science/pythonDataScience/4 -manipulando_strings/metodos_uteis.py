curso = "PythOn"

#caixa alta
print(curso.upper())

#caixa baixa
print(curso.lower())

#inicial maiúscula
print(curso.title())


#também é possível remover espaços em branco nas strings
curso = "     Python         "

#remover todos espaços
print(curso.strip())

#remover espaços da esquerda 
print(curso.lstrip())

#remover espaços da direita
print(curso.rstrip())

#junções e centralização
curso = "Python"

#centralização -> podemos colocar quantos caracteres vamos ocupar e qual caracter vai ocupa os espaços vagos, mas é opcional
print(curso.center(10, "#"))

#junções -> juntar um elemento com a string da variável
print(".".join(curso))

