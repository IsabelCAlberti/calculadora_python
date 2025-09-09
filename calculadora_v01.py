def calculadora():
    print("=== CALCULADORA ===")
    print("Operações: +  -  *  /  ** (potência)")

    while True:
        n1 = float(input("Digite o primeiro número: "))
        op = input("Digite a operação: ")
        n2 = float(input("Digite o segundo número: "))

        if op == "+":
            print("Resultado:", n1 + n2)
        elif op == "-":
            print("Resultado:", n1 - n2)
        elif op == "*":
            print("Resultado:", n1 * n2)
        elif op == "/":
            if n2 != 0:
                print("Resultado:", n1 / n2)
            else:
                print("Erro: divisão por zero!")
        elif op == "**":
            print("Resultado:", n1 ** n2)
        else:
            print("Operação inválida!")

        cont = input("Deseja continuar? (s/n): ")
        if cont.lower() != "s":
            break

calculadora()
