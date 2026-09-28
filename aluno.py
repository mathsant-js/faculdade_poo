from disciplina import Disciplina

class Aluno:
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        self.disciplinas = []
        self.notas_por_disciplinas = {}

    def matricular(self, disciplina: Disciplina):
        if disciplina not in self.disciplinas:
            self.disciplinas.append(disciplina)

        self.notas_por_disciplinas.setdefault(disciplina.nome, [])

    def adicionar_nota(self, nota, disciplina: Disciplina):
        if disciplina.nome not in self.disciplinas:
            self.matricular(disciplina)

        self.notas_por_disciplinas[disciplina.nome].append(nota)