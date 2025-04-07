class StatsManager:
    def __init__(self):
        self.total = 0
        self.acertos = 0
        self.erros = 0

    def registrar_resultado(self, correto: bool):
        self.total += 1
        if correto:
            self.acertos += 1
        else:
            self.erros += 1

    def obter_taxa_acerto(self):
        if self.total == 0:
            return 0.0
        return round((self.acertos / self.total) * 100, 2)

    def gerar_resumo(self):
        return (
            f"Rodadas analisadas: {self.total}\n"
            f"Acertos: {self.acertos}\n"
            f"Erros: {self.erros}\n"
            f"Taxa de acerto: {self.obter_taxa_acerto()}%"
        )
