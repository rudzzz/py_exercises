def calculadora():

    print("-- Bem vindo a Calculadora! --")
    print()
    print('Operações disponiveis: \nSoma(+)\nSubtração(-)\nMultiplicação(*)\nDivisão(/)')

    opcao = input("Qual operação deseja realizar? ")
    num1 = float(input("Qual o primeiro número? "))
    num2 = float(input("Qual o segundo número? "))

    resultado = ''

    if opcao == '+':
        resultado = num1 + num2
    elif opcao == '-':
        resultado = num1 - num2
    elif opcao == '*':
        resultado = num1 - num2
    elif opcao == '/':
        resultado = num1 / num2
    else:
        print('Opção inválida!')

    print(f'O resultado de {num1} {opcao} {num2} é: {resultado}')


calculadora()