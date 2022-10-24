class Veiculo:
  def __init__(self, cor, placa, num_rodas):
    self.cor = cor
    self.placa = placa
    self.num_rodas = num_rodas

  def partida(self):
    print("Ligando o motor")

class Moto(Veiculo):
  pass

class Carro(Veiculo):
  pass

class Caminhao(Veiculo):
  pass

moto = Moto("Azul", "123-fff", 2)
moto.partida()

carro = Carro("Preto", "122", 4)
carro.partida()

#herança não te impede de criar coisas específicas para cada classe filha
