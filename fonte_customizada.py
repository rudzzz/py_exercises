import  pyfiglet

palavra = input("Qual frase deseja customizar? ")
customizada = ""
opcao = ""

customizada = pyfiglet.figlet_format(palavra)

print(customizada)