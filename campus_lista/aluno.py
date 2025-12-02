class Aluno:
    def __init__(self, matricula: int, nome: str, curso):
        self.matricula = matricula
        self.nome = nome
        self.curso = curso


    def get_matricula(self):
        return self.matricula

    def get_nome(self):
        return self.nome

    def get_curso(self):
        return self.curso

    def __str__(self):
        return f"{self.matricula} - {self.nome} ({self.curso})"
