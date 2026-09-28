from aluno import Aluno
from disciplina import Disciplina

# Criando objeto de aluno
aluno1 = Aluno("Matheus", "20260301", "Ciência da Computação")

# Criando objetos de disciplinas
matematica = Disciplina("Matemática", "Roberto")
python = Disciplina("Python", "Russi")

# Matriculando o aluno nas disciplinas
aluno1.matricular(matematica)
aluno1.matricular(python)

# Adicionando as notas do aluno em matemática
aluno1.adicionar_nota(8, matematica)
aluno1.adicionar_nota(10, matematica)

# Adicionando as notas do aluno em python
aluno1.adicionar_nota(9, python)
aluno1.adicionar_nota(10, python)

# Exibindo boletim do aluno
aluno1.exibir_boletim()