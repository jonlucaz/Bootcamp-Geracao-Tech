#if; if else; if ternário


#if simples:
#saldo = float(input("Qual seu saldo em R$? "))
#saque = float(input("Quanto você quer sacar em R$? "))

#if (saque <= saldo):
#  print("É possível fazer seu saque!") 
#if (saque >= saldo):
#  print("Seu saldo é inferior ao valor solicidado!")


#if else
#saldo = float(input("Qual seu saldo em R$? "))
#saque = float(input("Quanto você quer sacar em R$? "))

#if (saque <= saldo):
 # print("É possível fazer seu saque!") 
#else:
  #print("Seu saldo é inferior ao valor solicidado!")


#if; elif; else
#import sys


#opcao = int(input("Informe uma opção:\n [1] Extrato \n[2] Saque"))

#if opcao == 1:
#  print("Exibindo extrato...")
#elif opcao ==2:
 # valor = float(input("Informe o valor para o saque:"))
  #print(f'R${valor}')
#else:
 # sys.exit("Opção invalida")


#if aninhado = if dentro de if


#if ternário
saldo = float(input("Qual seu saldo em R$? "))
saque = float(input("Quanto você quer sacar em R$? "))

status = "Sucesso" if saldo >= saque else "Falha"

print(f'{status} ao realizar o saque')