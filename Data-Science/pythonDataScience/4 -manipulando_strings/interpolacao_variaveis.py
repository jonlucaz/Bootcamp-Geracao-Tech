#no python há 3 formas de interpolar variáveis: com o sinal %, com o format e por fim com o f strings.

#old style -> %
nome = "Jon"
idade = 25
profissao = "Programador"
linguagem = "Python"

print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s." % (nome, idade, profissao, linguagem))

#método format

print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}." .format(nome, idade, profissao, linguagem))

#f-string

print(f'Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.')

#para restringir o número de casas de um elemento basta colocar dentro das chaves a expressão .1f {idade.2f}
#no exemplo idade vai ser restringida a duas casas após o .