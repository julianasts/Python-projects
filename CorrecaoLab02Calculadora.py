print("\n********* Python Calculator **********")

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("\nSelecione o numero da operacao desejada: \n")
print("1 - Soma")
print("2 - Subtracao")
print("3 - Multiplicacao")
print("4 - Divisao")

escolha = input("\nDigite sua opcao (1/2/3/4): ")

num1 = int(input("\nDigite o primeiro numero: "))
num2 = int(input("\nDigite o segundo numero: "))

if escolha == '1':
    print("\n")
    print(num1, "+", num2, "=", add(num1, num2))
    print("\n")

elif escolha == '2':
    print("\n")
    print(num1, "-", num2, "=", subtract(num1, num2))

elif escolha == '3':
    print("\n")
    print(num1, "*", num2, "=", multiply(num1, num2) )
    print("\n")

elif escolha == '4':
    print("\n")
    print(num1, "/", num2, "=", divide(num1, num2))

else:
    print("\nOpcao invalida!")