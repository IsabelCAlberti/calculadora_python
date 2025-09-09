def calculadora():
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Erro: você deve digitar números válidos.")
        return

    print("Operações")
    print("1: adição")
    print("2: subtração")
    print("3: multiplicação")
    print("4: divisão")

    operacao = input("Escolha uma operação: ")

    operacoes = {
        #lambda argumentos: expressão
        "1": lambda x, y: x + y,
        "2": lambda x, y: x - y,
        "3": lambda x, y: x * y,
        "4": lambda x, y: x / y if y != 0 else "Erro: divisão por zero!"
    }

    if operacao in operacoes:
        resultado = operacoes[operacao](num1, num2)
        print("Resultado:", resultado)
    else:
        print("Operação inválida!")

calculadora()
