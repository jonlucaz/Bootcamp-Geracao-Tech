#atributos do objeto
#todos objetos nascem com o mesmo número de atributos de classe e instancia.
#atributos de instancia são diferentes para cada objeto
#já os de classe são compartilhados entre objetos
class Estudante:
  escola = "DIO"

  def __init__(self, nome, numero):
    self.nome = nome
    self.numero = numero

  def __str__(self):
    return f'{self.nome} ({self.numero}) - {self.escola}'

jon = Estudante("Jonathan", 128)
lu = Estudante("Luiza", 973)

