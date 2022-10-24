#conhecendo os metodos __init__ e __del__

#o método construtor é executado quando uma nova instância da classe é criada
#para declarar: __init__

class Cachorro:
  def __init__(self, nome, cor, acordado=True):
    self.nome = nome
    self.cor = cor
    self.acordado = acordado
  
c1 = Cachorro("Sirius", "preto", True)

#metodo destrutor
#é executado quando uma instância(objeto) é destruida
#__del__