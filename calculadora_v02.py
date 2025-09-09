def calculadora():
    while True:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Erro: você deve digitar números válidos.\n")
            continue  # volta pro início do loop

        print("\nOperações:")
        print("1: adição")
        print("2: subtração")
        print("3: multiplicação")
        print("4: divisão")
        print("0: sair")

        operacao = input("Escolha uma operação: ")

        if operacao == "0":
            print("Saindo da calculadora...")
            break

        if operacao == "1":
            resultado = num1 + num2
        elif operacao == "2":
            resultado = num1 - num2
        elif operacao == "3":
            resultado = num1 * num2
        elif operacao == "4":
            if num2 != 0:
                resultado = num1 / num2
            else:
                print("Erro: divisão por zero!\n")
                continue
        else:
            print("Operação inválida!\n")
            continue

        print(f"Resultado: {resultado}\n")

        continuar = input("Gostaria de realizar outra operação? (S/N): ").upper()
        if continuar != "S":
            print("Encerrando calculadora...")
            break


calculadora()

            
    # Usei try/except para garantir que os inputs são números.