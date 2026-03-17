historico = []

def soma(num1, num2):
    return num1 + num2

def subtrair(num1, num2):
    return num1 - num2

def mult(num1, num2):
    return num1 * num2

def div(num1, num2):
    if num2 == 0:
        return "Erro: divisão por zero"
    return num1 / num2

def registrar(num1, operador, num2, resultado):
    historico.append(f"{num1} {operador} {num2} = {resultado}")

while True:
    num1 = float(input("Insira o primeiro número (ou 'sair'): "))
    num2 = float(input("Insira o segundo número: "))
    operador = input("Insira a operação (+, -, *, /, histórico): ")

    if operador == "historico":
        if not historico:
            print("Nenhuma operação realizada ainda.")
        else:
            print("\n--- Histórico ---")
            for i, op in enumerate(historico, 1):
                print(f"{i}. {op}")
        continue

    if operador == "+":
        resultado = soma(num1, num2)
    elif operador == "-":
        resultado = subtrair(num1, num2)
    elif operador == "*":
        resultado = mult(num1, num2)
    elif operador == "/":
        resultado = div(num1, num2)
    else:
        print("Operação inválida")
        continue

    print(f"Resultado: {resultado}")
    registrar(num1, operador, num2, resultado)
