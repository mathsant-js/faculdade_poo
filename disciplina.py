class Disciplina:
    """Representa uma disciplina"""
    def __init__(self, nome: str, professor: str):
        self.nome = nome
        self.professor = professor

    def exibir_informacoes(self):
        """Exibe as informações da disciplina"""
        print(f"Disciplina: {self.nome} | Professor: {self.professor}")