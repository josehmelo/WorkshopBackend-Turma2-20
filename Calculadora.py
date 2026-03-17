def soma(num1,num2):
    return num1 + num2

def subtrair(num1,num2):
    return num1 - num2

def mult(num1,num2):
    return num1 * num2

def div(num1,num2):
    return num1 / num2

num1 = int (input("insira o primeiro numero: "))
num2 = float (input("insira o segundo numero: "))
operador = (input("insira a operação matematica: "))

if operador == "+":
    print(soma(num1,num2))
elif operador == "-":
    print(subtrair(num1,num2))
elif operador =="*":
    print(mult(num1,num2))
elif operador =="/":
    print(div(num1,num2))
else:
    print("Operação invalida")