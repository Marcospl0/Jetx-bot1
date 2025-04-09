import json
import os

CAMINHO = "stats.json"

def carregar_dados():
    if not os.path.exists(CAMINHO):
        with open(CAMINHO, "w") as f:
            json.dump({"acertos": 0, "erros": 0}, f)
    with open(CAMINHO, "r") as f:
        return json.load(f)

def salvar_dados(data):
    with open(CAMINHO, "w") as f:
        json.dump(data, f)

def registrar_resultado(resultado_real):
    data = carregar_dados()
    previsao = 1.80
    if resultado_real >= previsao:
        data["acertos"] += 1
    else:
        data["erros"] += 1
    salvar_dados(data)

def obter_taxas():
    data = carregar_dados()
    total = data["acertos"] + data["erros"]
    taxa = round((data["acertos"] / total) * 100, 2) if total > 0 else 0
    return data["acertos"], data["erros"], taxa
