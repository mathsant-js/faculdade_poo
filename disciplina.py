class Disciplina:
    def __init__(self, nome, professor):
        self.nome = nome,
        self.professor = professor

    def exibir_informações(self):
        print(f"Disciplina: {self.nome} | Professor: {self.professor}")