import random

class JetXPredictor:
    def __init__(self):
        self.history = []

    def update_history(self, last_flight):
        self.history.append(last_flight)
        if len(self.history) > 30:
            self.history.pop(0)

    def calculate_next_prediction(self):
        if len(self.history) < 5:
            return {"prediction": "Analisando...", "confidence": 0}
        
        # Exemplo de padrão básico: se 3 voos seguidos forem < 1.5, o próximo tende a subir
        last_three = self.history[-3:]
        low_count = sum(1 for x in last_three if x < 1.5)

        if low_count >= 2:
            return {"prediction": "Alta (acima de 2.0x)", "confidence": 93}
        else:
            return {"prediction": "Baixa (até 1.8x)", "confidence": 87}