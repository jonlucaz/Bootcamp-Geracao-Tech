#o que é?
#é a capacidade de uma classe filha herdar características e comportamentos da classe pai(base)
#fornece reutilização do código

#sintaxe:
class A:
  pass
class B(A):
  pass


#herança simples e herança multipla

#herança simples:
#quando a classe filha herda de apenas uma classe pai

#herança multipla:
#quando uma classe filha herda de várias classes pai
#nem toda lp suporta herança multipla
class A:
  pass
class B:
  pass
class C(A, B):
  pass