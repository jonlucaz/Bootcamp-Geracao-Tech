#é um dos conceitos fundamentais de POO
#descreve a ideia de agrupar dados e os métodos que manipulam esses dados em uma unidade
#isso impões restrições ao acesso direto a variáveis e métodos, evitando modificação acidental


#recursos simples e privados
#em python não temos palavras reservadas para definir o nível de acesso aos atributos e metodos
#mas temos convenções usadas no nome do recurso para definir se a variavel é publica ou privada
#_name, assim é usada a convenção

#definição de público e privado
#publico: pode ser acessado de fora da classe
#privado: só pode ser acessado pela classe

#exemplo
class Conta: 
  def __init__(self, saldo=0):
    self._saldo = saldo

  def depositar(self, valor):
    pass

  def sacar(self, valor):
    pass

conta = Conta(100)
print(conta._saldo)