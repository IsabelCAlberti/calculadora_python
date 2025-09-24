import math

historico_calculadora = []
operacoes_desfeitas = []

def realizar_operacao():
    while True:
        try:
            menu_operacoes()
            operacao_realizada = input("Escolha a operação: ")
            
            if operacao_realizada not in ["+", "-", "*", "/", "**", "r"]:
                print("Operação inválida! Digite uma das opções do menu.")
                continue
            
            if operacao_realizada == "r":
                num1 = float(input("Digite o número para a raiz quadrada: "))
                if num1 >= 0:
                    resultado = math.sqrt(num1)
                    print(f"A raiz quadrada de {num1} é {resultado}")
                    historico_calculadora.append(f"√{num1} = {resultado}")
                else:
                    print("Erro: não existe raiz quadrada real de número negativo!")
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
                else:
                    print("Operação inválida!")
                    continue

                print("Resultado:", resultado)
                historico_calculadora.append(f"{num1} {operacao_realizada} {num2} = {resultado}")

        except ValueError:
            print("Erro: você deve digitar números válidos.")
            continue

        cont = input("Deseja continuar? (s/n): ")
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
╚══════════════════════════╝
    """)
    
    
        
def mostrar_historico():
    if not historico_calculadora:
        print("Histórico vazio.")
    else:
        print("\n Histórico de Operações:")
        for item in historico_calculadora:
            print(" -", item)

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
        print(f"Operação desfeita: {ultima}")
    else:
        print("Nada a desfazer.")

def refazer_operacao():
    if operacoes_desfeitas:
        refazer = operacoes_desfeitas.pop()
        historico_calculadora.append(refazer)
        print(f"Operação refeita: {refazer}")
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
║ 6. Sair                  ║
╚══════════════════════════╝
""")
        opcao_menu = input("Escolha uma opção: ")

        if opcao_menu == "1":
            realizar_operacao()
        elif opcao_menu == "2":
            mostrar_historico()
        elif opcao_menu == "3":
            apagar_historico()
        elif opcao_menu == "4":
            desfazer_operacao()
        elif opcao_menu == "5":
            refazer_operacao()
        elif opcao_menu == "6":
            print("\nEncerrando programa...")
            print("\n Histórico Final:")
            mostrar_historico()
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()
