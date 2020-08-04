# Calculadora em Python

print("\n******************* Python Calculator *******************")

print("\n Selecione o numero da operacao desejada:")

print("\n 1 - Soma \n 2 - Subtração \n 3 - Multiplicação \n 4 - Divisão")

opcao = int(input("Digite uma opção (1/2/3/4): "))

def soma():
        numero1 = float(input("Primeiro Número: "))
        numero2 = float(input("Segundo Número: "))
        print("Resultado: ", numero1 + numero2)
    
def subtracao():
        numero1 = float(input("Primeiro Número: "))
        numero2 = float(input("Segundo Número: "))
        print("Resultado: ", numero1 - numero2)

def multiplicacao():
        numero1 = float(input("Primeiro Número: "))
        numero2 = float(input("Segundo Número: "))
        print("Resultado: ", numero1 * numero2)

def divisao():
        numero1 = float(input("Primeiro Número: "))
        numero2 = float(input("Segundo Número: "))
        print("Resultado: ", numero1 % numero2)

if opcao==1:
    soma()

if opcao==2:
    subtracao()

if opcao==3:
    multiplicacao()

if opcao==4:
    divisao()

else:
    print("\nOpcao invalida!")