from .aluno import Aluno

class Monitor(Aluno):
    def __init__(self, aluno: Aluno, disciplinaEnsinada: str, horarioDeEnsino: str):
        super().__init__(aluno.matricula, aluno.nome, aluno.curso)
        self.disciplinaEnsinada = disciplinaEnsinada
        self.horarioDeEnsino = horarioDeEnsino

    def get_disciplinaEnsinada(self):
        return self.disciplinaEnsinada

    def get_horarioDeEnsino(self):
        return self.horarioDeEnsino
    def __str__(self):
        return f"Monitor {self.nome} ({self.curso}) - Disciplina: {self.disciplinaEnsinada} - Horário: {self.horarioDeEnsino}"
