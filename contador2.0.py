def conta_caracteres(string):
    """Conta quantas vezes uma letra aparece em uma frase"""
    count = {}
    for i in string:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    print(count)


palavra = input("Digite a palavra desejada: ")
conta_caracteres(palavra)