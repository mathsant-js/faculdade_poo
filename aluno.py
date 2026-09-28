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

    def media_em(self, disciplina: Disciplina) -> float:
        notas = self.notas_por_disciplinas.get(disciplina.nome, [])

        if not notas:
            return 0.0

        return sum(notas) / len(notas)

    def media_geral(self) -> float:
        medias = []

        for disc in self.disciplinas:
            m = self.media_em(disc)

            if m > 0:
                medias.append(m)

        if not medias:
            return 0.0

        return sum(medias) / len(medias)

    def exibir_boletim(self):
        print(f"\nAluno: {self.nome} | Matrícula : {self.matricula} | Curso: {self.curso}")

        if not self.disciplinas:
            print("Sem disciplinas matriculadas.")
            return

        for disciplina in self.disciplinas:
            notas = self.notas_por_disciplinas.get(disciplina.nome, [])
            media = self.media_em(disciplina)
            disciplina.exibir_informacoes()
            print(f"    Notas do aluno em {disciplina.nome}: {notas if notas else '-'}")
            print(f"    Média do aluno em {disciplina.nome}: {media:.1f}")
        print(f"MÉDIA GERAL: {self.media_geral():.1f}")