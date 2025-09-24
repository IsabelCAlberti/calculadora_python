import math

# Agora vamos guardar operações como tuplas: (operação, num1, num2, resultado)
historico_calculadora = []
operacoes_desfeitas = []

def realizar_operacao():
    while True:
        try:
            menu_operacoes()
            operacao_realizada = input("Escolha a operação: ")

            if operacao_realizada not in ["+", "-", "*", "/", "**", "r", "%", "m"]:
                print("Operação inválida! Digite uma das opções do menu.")
                continue

            if operacao_realizada == "r":
                num = float(input("Digite o número para a raiz quadrada: "))
                if num >= 0:
                    resultado = math.sqrt(num)
                    print(f"A raiz quadrada de {num} é {resultado}")
                    historico_calculadora.append(("r", num, None, resultado))
                else:
                    print("Erro: não existe raiz quadrada real de número negativo!")
                    continue

            elif operacao_realizada == "%":
                valor = float(input("Digite o valor base: "))
                porcentagem = float(input("Digite a porcentagem: "))
                resultado = valor * (porcentagem / 100)
                print(f"{porcentagem}% de {valor} é {resultado}")
                historico_calculadora.append(("%", valor, porcentagem, resultado))

            elif operacao_realizada == "m":
                num1 = float(input("Digite o primeiro número (dividendo): "))
                num2 = float(input("Digite o segundo número (divisor): "))
                if num2 != 0:
                    resultado = num1 % num2
                    print(f"O resto da divisão de {num1} por {num2} é {resultado}")
                    historico_calculadora.append(("m", num1, num2, resultado))
                else:
                    print("Erro: divisão por zero!")
                    continue

            else:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))

                if operacao_realizada == "+":
                    resultado = num1 + num2
                elif operacao_realizada == "-":
                    resultado = num1 - num2
                elif operacao_realizada == "*":
                    resultado = num1 * num2
                elif operacao_realizada == "/":
                    if num2 != 0:
                        resultado = num1 / num2
                    else:
                        print("Erro: divisão por zero!")
                        continue
                elif operacao_realizada == "**":
                    resultado = num1 ** num2

                print(f"Resultado: {resultado}")
                historico_calculadora.append((operacao_realizada, num1, num2, resultado))

            # Limpa refazer se houver nova operação
            operacoes_desfeitas.clear()

        except ValueError:
            print("Erro: você deve digitar números válidos.")
            continue

        cont = input("Deseja continuar com as operações? (s/n): ")
        if cont.lower() != "s":
            break  

def menu_operacoes():
    print("""
Operações disponíveis:
╔══════════════════════════╗
║   CALCULADORA DIGITAL    ║
╠══════════════════════════╣
║ +   Soma                 ║
║ -   Subtração            ║
║ /   Divisão              ║
║ *   Multiplicação        ║
║ **  Potênciação          ║
║ r   Raiz Quadrada        ║
║ %   Porcentagem          ║
║ m   Módulo               ║
╚══════════════════════════╝
    """)

def mostrar_historico():
    if not historico_calculadora:
        print("Histórico vazio.")
    else:
        print("\nHistórico de Operações:")
        for op in historico_calculadora:
            operacao, num1, num2, resultado = op
            if operacao == "r":
                print(f"√{num1} = {resultado}")
            elif operacao == "%":
                print(f"{num2}% de {num1} = {resultado}")
            elif operacao == "m":
                print(f"{num1} % {num2} = {resultado}")
            else:
                print(f"{num1} {operacao} {num2} = {resultado}")

def apagar_historico():
    if historico_calculadora:
        historico_calculadora.clear()
        operacoes_desfeitas.clear()
        print("Histórico apagado com sucesso.")
    else:
        print("Histórico já está vazio.")

def desfazer_operacao():
    if historico_calculadora:
        ultima = historico_calculadora.pop()
        operacoes_desfeitas.append(ultima)
        print("Operação desfeita.")
    else:
        print("Nada a desfazer.")

def refazer_operacao():
    if operacoes_desfeitas:
        operacao, num1, num2, resultado = operacoes_desfeitas.pop()
        # Recalcula o resultado
        if operacao == "+":
            resultado = num1 + num2
        elif operacao == "-":
            resultado = num1 - num2
        elif operacao == "*":
            resultado = num1 * num2
        elif operacao == "/":
            if num2 != 0:
                resultado = num1 / num2
            else:
                print("Erro: divisão por zero!")
                return
        elif operacao == "**":
            resultado = num1 ** num2
        elif operacao == "r":
            resultado = math.sqrt(num1)
        elif operacao == "%":
            resultado = num1 * (num2 / 100)
        elif operacao == "m":
            if num2 != 0:
                resultado = num1 % num2
            else:
                print("Erro: divisão por zero!")
                return
        historico_calculadora.append((operacao, num1, num2, resultado))
        print("Operação refeita.")
    else:
        print("Nada a refazer.")

def menu():
    while True:
        print("""
╔══════════════════════════╗
║   CALCULADORA DIGITAL    ║
╠══════════════════════════╣
║ 1. Realizar operação     ║
║ 2. Mostrar histórico     ║
║ 3. Apagar histórico      ║
║ 4. Desfazer operação     ║
║ 5. Refazer operação      ║
║ 6. Sair                   ║
╚══════════════════════════╝
""")
        opcao_menu = input("Escolha uma opção: ")

        match opcao_menu:
            case "1":
                realizar_operacao()
            case "2":
                mostrar_historico()
            case "3":
                apagar_historico()
            case "4":
                desfazer_operacao()
            case "5":
                refazer_operacao()
            case "6":
                print("\nEncerrando programa...")
                print("\nHistórico Final:")
                mostrar_historico()
                break
            case _:
                print("Opção inválida. Tente novamente.")

menu()
