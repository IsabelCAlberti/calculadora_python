
import math

'''Deve permitir que o usuário escolha e execute pelo menos as operações: (soma, subtração, multiplicação, divisão, potenciação, porcentagem, raiz quadrada e modulo)
'''
def menu_operacoes():
    while True:
        print(""" 
              |      OPERAÇÕES      |  
              |    Soma (+)         |  
              |    Subtração (-)    |  
              |    Multiplicação (*)|  
              |    Divisão (/)      |  
              |    Potência (**)    |
              |    Raiz (r)         |
              |    Módulo (%)       |
              |    Média (m)        |
          """)
        operacoes = input("Escolha a operação: ")

        if operacoes not in ["+", "-", "*", "/", "**", "r", "%", "m"]:
            print("Operação inválida! Digite uma das opções do menu.")
            continue  
        else:
            return operacoes

def realizar_operacoes():
    while True:
        try:     
            escolha_operacoes = menu_operacoes()
            
            if escolha_operacoes == "r":
                num1 = float(input("Digite o número para a raiz quadrada: "))
                if num1 >= 0:
                    resultado = math.sqrt(num1)
                    print(f"A raiz quadrada de {num1} é {resultado}")
                else:
                    print("Erro: não existe raiz quadrada real de número negativo!")
                    continue

            elif escolha_operacoes == "%":
                valor = float(input("Digite o valor base: "))
                porcentagem = float(input("Digite a porcentagem: "))
                resultado = valor * (porcentagem / 100)
                print(f"{porcentagem}% de {valor} é {resultado}")

            elif escolha_operacoes == "m":
                num1 = float(input("Digite o primeiro número (dividendo): "))
                num2 = float(input("Digite o segundo número (divisor): "))
                if num2 != 0:
                    resultado = num1 % num2
                    print(f"O resto da divisão de {num1} por {num2} é {resultado}")
                else:
                    print("Erro: divisão por zero!")
                    continue

            else:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))

                if escolha_operacoes == "+":
                    resultado = num1 + num2
                elif escolha_operacoes == "-":
                    resultado = num1 - num2
                elif escolha_operacoes == "*":
                    resultado = num1 * num2
                elif escolha_operacoes == "/":
                    if num2 != 0:
                        resultado = num1 / num2
                    else:
                        print("Erro: divisão por zero!")
                        continue
                elif escolha_operacoes == "**":
                    resultado = num1 ** num2

                print("Resultado:", resultado)  

        except ValueError:
            print("Erro: você deve digitar números válidos.")
            continue




    
'''O programa deve rodar em loop, exibindo sempre um menu organizado
Realizar operação                                     
Mostrar histórico                                           
Apagar histórico                                          
Desfazer operação              
Refazer operação                                       
Sair                                                                            
'''

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

        match opcao_menu:
            case "1":
                realizar_operacoes()
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
                print("\n Histórico Final:")
                mostrar_historico()
                break
            case _:
                print("Opção inválida. Tente novamente.")
    
        
        
        
        
        
        
        
        
'''Não deve aceitar letras ou caracteres inválidos quando o programa espera números.
   Não deve permitir divisão por zero.
   Deve exibir mensagens claras quando ocorrer erro de entrada.
'''


'''numero01 = float(input("Digite um número"))
numero02 =float(input("Digite outro número"))

if not isinstance(numero01, (int, float)) or not isinstance(numero02, (int, float)):
    print("Número inválido")
    
if type(numero01) not in [int, float] or type(numero02) not in [int, float]:
    print("Número inválido")'''

menu()