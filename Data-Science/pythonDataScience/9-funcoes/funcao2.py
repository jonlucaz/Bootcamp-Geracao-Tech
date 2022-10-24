#parametros especiais
#parametros é aquilo que fica dentro de parenteses na função
#podem ser nomeada e locais, mas com os parametros especiais podemos forçar isso e obrigar que seja de uma classe
#seja por posiçao, por nome ou pelos dois
#quando se diz que é passado por posição, está se referindo ao indice

def criar_carro( modelo, ano, placa, /, marca, motor, combustivel):
  print(modelo, ano, placa, marca, motor, combustivel)

#antes da barra tudo precisa ser definido por posição, depois da barra não precisa, mas se for por posição ainda assim funciona

#criar_carro("Civic", "2008", "CIV-2343", marca="Honda", motor="1.8", combustivel="gasolina") #funciona
#criar_carro("Civic", "2008", "CIV-2343", "Honda", "1.8", "gasolina") #funciona
#criar_carro(modelo="Civic", ano="2008", placa="CIV-2343", marca="Honda", motor="1.8", combustivel="gasolina") #erro

#já para todos os parametros serem obrigatoriamente nomeados colocamos o * na após o primeiro parentese (*...)

def criar_carro(*, modelo, ano, placa, marca, motor, combustivel):
  print(modelo, ano, placa, marca, motor, combustivel)

criar_carro(modelo="Civic", ano="2008", placa="CIV-2343", marca="Honda", motor="1.8", combustivel="gasolina") #agora funciona

#para hibrido colocamos os dois símbolos  /*


#objetos de primeira classe 
#em python tudo é objeto, sendo assim a função tambem é um objeto e isso a faz objeto de primeira classe
#com isso podemos atribuir funções a uma variável e até mesmo passar como parametro para outra função
def somar(a, b):
  return a + b

def exibir_resultado(a, b, funcao):
  resultado = funcao(a, b)
  print(f'O resultado da operação {a} + {b} = {resultado}')

exibir_resultado(10, 10, somar) 
