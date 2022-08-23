import pyshorteners

url_grande = input("Digite a url para ser encurtada: ")

type_tiny = pyshorteners.Shortener()
url_encurtada = type_tiny.tinyurl.short(url_grande)

print(f"Sua nova url: {url_encurtada}")
