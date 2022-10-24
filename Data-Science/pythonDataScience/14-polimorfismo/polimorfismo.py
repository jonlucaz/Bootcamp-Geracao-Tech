# O que é:
#polimorfismo significa ter muitas formas, na programação significa o mesmo nome de função
#mas com assinaturas diferentes e usados para tipos diferentes


#polimorfismo com herança
#mesmo método com comportamento diferente
class Passaro:
  def voar(self): pass

class Pardal(Passaro):
  def voar(self):
    print("Pardal voa")

class Avestruz(Passaro):
  def voar(self):
    print("Avestruz não voa")

def plano_de_voo(passaro):
  passaro.voar()

plano_de_voo(Pardal())
plano_de_voo(Avestruz())

