import random
from stats import obter_taxas

def gerar_sinal_jetx():
    previsao = round(random.uniform(1.50, 2.20), 2)
    confianca = random.randint(85, 97)
    
    # Simulação de resultado real
    resultado_real = round(random.uniform(1.00, 3.00), 2)

    acertos, erros, taxa = obter_taxas()
    
    if resultado_real >= previsao:
        acertos += 1
    else:
        erros += 1

    return {
        "previsao": previsao,
        "confianca": confianca,
        "resultado_real": resultado_real,
        "acertos": acertos,
        "erros": erros,
        "taxa_acerto": taxa
    }
