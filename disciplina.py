class Disciplina:
    """Representa uma disciplina"""
    def __init__(self, nome: str, professor: str) -> None:
        self.nome = nome
        self.professor = professor

    def exibir_informacoes(self) -> None:
        """Exibe as informações da disciplina"""
        print(f"Disciplina: {self.nome} | Professor: {self.professor}")