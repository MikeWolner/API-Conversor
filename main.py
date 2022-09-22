import requests

def obter_produtos():
    URL = "https://api.hgbrasil.com/finance?key=fd7ccfbb"
    resposta = requests.get(URL)
    dolar = resposta.json()['results']['currencies']['USD']['buy']
    euro = resposta.json()['results']['currencies']['EUR']['buy']
    real = float(input('Informe o valor em real'))
    convertido_dolar = real / dolar
    convertido_euro = real / euro
    return f"Dolar: US${convertido_dolar:.2f}\nEuro: EU${convertido_euro:.2f}"
print(obter_produtos())



