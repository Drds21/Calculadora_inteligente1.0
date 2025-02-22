#!/bin/bash
from time import sleep

print("Olá, vamos calcular? Digite 2 números para iniciar as operações!\n")
sleep(2)
num1 = int(input("Primeiro número: "))
num2 = int(input("Segundo número: "))
sleep(1)
print("\nPerfeito! Agora, selecione a opção de operação desejada abaixo:\n")
print("Somar(1)\nSubtrair(2)\nDividir(3)")


opcao = int(input(""))
print(f"Sua resposta foi \033[31m{opcao}\033[0;0m")
sleep(1)

if opcao == 1:

  print(f"A soma de {num1} + {num2} é igual a {num1 + num2}!\n")

elif opcao == 2:
  print(f"A subtração dos números {num1} - {num2} é igual a {num1 - num2}!\n")

elif opcao == 3:
  print(f"O resultado da divisão entre os números {num1} e {num2} é igual a {num1 / num2}!\n")
else:
  print("Opção não disponível, digite novamente!")

print("Selecione uma das opções abaixo: \nContinuar(1)\nFinalizar(2)")

opcao_2 = int(input(""))

if opcao_2 == 1:
  for opcao in range(10):

    print("\nVamos novamente então!")
    print("Digite 2 números para iniciar as operações!\n")
    num1 = int(input("Primeiro número: "))
    num2 = int(input("Segundo número: "))
    print("Agora, selecione a opção de operação desejada abaixo:\n")
    print("Somar(1)\nSubtrair(2)\nDividir(3)")
    opcao = int(input(""))
    print(f"Sua resposta foi \033[31m{opcao}\033[0;0m")

    if opcao == 1:

      print(f"A soma de {num1} + {num2} é igual a {num1 + num2}!")

    elif opcao == 2:
      print(f"A subtração dos números {num1} - {num2} é igual a {num1 - num2}!")

    elif opcao == 3:
      print(f"O resultado da divisão entre os números {num1} e {num2} é igual a {num1 / num2}!")
    else:
      print("Opção não disponível, digite novamente!")
      print("Selecione uma das opções abaixo: \nContinuar(1)\nFinalizar(2)")
      if opcao == 1:

        print(f"A soma de {num1} + {num2} é igual a {num1 + num2}!")

      elif opcao == 2:
        print(f"A subtração dos números {num1} - {num2} é igual a {num1 - num2}!")


elif opcao_2 > 2:
    print("Entendi que você deseja finalizar... OK, até mais! FIM.")

else:
    print("Ok, até mais! FIM.")

