#python nos obriga a identar o bloco de código ou o programa não vai funcionar
 
saldo = input("Qual seu saldo em R$? ")
saque = input("Quanto você quer sacar em R$? ")

if (saque <= saldo):
  print("É possível fazer seu saque!") 
else:
  print("Seu saldo é inferior ao valor solicidado!")