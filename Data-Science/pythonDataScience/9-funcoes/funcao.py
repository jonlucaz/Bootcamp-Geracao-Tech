#Funções são definidas por um bloco de código que pode receber parametros
#torna o código mais legível e possibilita o reaproveitamento do código
#programar baseado em funções é a mesma coisa que dizer programação estruturada
#def é a palavra reservada para função em python

#exibir mensagem
def exibir_mensagem():
  print("Hello world!")
exibir_mensagem()

def exibir_mensagem2(nome):
  print(f'Hello {nome}')
exibir_mensagem2(nome="Jon")

#para retornar um valor usamos o return e no python podemos retornar mais de um valor
#por padrão o python retorna none


#argumentos nomeados - permite que você nomeeie os argumentos e evite erros no código


#args e kwargs - combinar parametros obrigatorios com *args e **kwargs o método recebe o valor como tuplas e dicionário respectivamente
