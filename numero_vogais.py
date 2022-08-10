def checa_vogal():
    palavra = input("Digite a palavra: ").lower()
    contador = 0
    vogais = set('AEIOUaeiou')

    for i in palavra:
        if i in vogais:
            contador = contador + 1

    print(f"Número de vogais na frase '{palavra}': {contador}")


checa_vogal()