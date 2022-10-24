#uma classe define as caracteristicas e comportamentos de um objeto, mas sem usá-las diretamente
#já os objetos podemos usar e contém as caracteristicas definidos nas classes

#classe se assemelha a uma planta da casa
#objeto seria como a casa em si com os aspectos definidos na planta

#Desafio Concessionária

class Moto: 
  def __init__(self, cor, modelo, ano, valor):
    self.cor = cor 
    self.modelo = modelo
    self.ano = ano
    self.valor = valor
  
  def buzina(self):
    print("Bi bi kkkkkkkkkkk...")
  
  def parar(self):
    print("Parando moto...")
    print("Moto parada")

  def correr(self):
    print("80 km/h")

  def __str__(self):
    return f'Moto: {self.cor}, {self.modelo}, {self.ano}, {self.valor}'
  

#self é a referencia explicita do objeto

motoca = Moto("preta", "fazer", 2011, 13000)
motoca.buzina()
motoca.correr()
motoca.parar()

print(motoca)