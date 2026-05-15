class Praca:
    def __init__(self, localizacao, catraca):
        self.localizacao = localizacao
        self.catraca = catraca

    def girar_catraca(self, girar):
        if girar not in ["liberada", "bloqueada"]:
            raise Exception("travada")
        self.catraca = girar
        print(f"catraca esta {self.catraca}")

olveira = Praca("rua", "bloqueada")
santos = Praca("entrada", "liberada")

olveira.girar_catraca("liberada")
santos.girar_catraca("bloqueada")