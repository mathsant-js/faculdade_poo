from aluno import Aluno
from disciplina import Disciplina

# Criando objeto de aluno
aluno1 = Aluno("Matheus", "20260301", "Ciência da Computação")

# Criando objetos de disciplinas
model_lin = Disciplina("Modelagem Linear", "Rodolfo")
python = Disciplina("Pensamento Computacional em Python", "Russi")

# Matriculando o aluno nas disciplinas
aluno1.matricular(model_lin)
aluno1.matricular(python)

# Adicionando as notas do aluno em Modelagem Linear
aluno1.adicionar_nota(8, model_lin)
aluno1.adicionar_nota(10, model_lin)

# Adicionando as notas do aluno em python
aluno1.adicionar_nota(9, python)
aluno1.adicionar_nota(10, python)

# Exibindo boletim do aluno
aluno1.exibir_boletim()