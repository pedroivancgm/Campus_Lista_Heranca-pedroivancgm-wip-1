from .aluno import Aluno
from .curso import Curso
from .monitor import Monitor

class Campus:
    _id_aluno = 1  #matrícula crescente para o sistema inteiro

    def __init__(self, nome: str):
        self.nome = nome
        self.alunos = []
        self.cursos = []
        self.monitores = []

    def cadastrar_curso(self, nome: str):
        if any(c.nome == nome for c in self.cursos):
            print("Este curso já existe.")
            return
        novo = Curso(nome)
        self.cursos.append(novo)
        print(f"Curso '{nome}' cadastrado com sucesso.")

    def listar_cursos(self):
        if not self.cursos:
            print("Nenhum curso cadastrado.")
            return
        for c in self.cursos:
            print(f"- {c.nome}")

    def cadastrar_aluno(self, nome: str, nome_curso: str):
        curso = None
        for c in self.cursos:
            if c.nome == nome_curso:
                curso = c
                break

        if curso is None:
            print("Curso não encontrado.")
            return

        aluno = Aluno(Campus._id_aluno, nome, curso)
        self.alunos.append(aluno)
        Campus._id_aluno += 1
        print(f"Aluno cadastrado: {aluno}")

    def cadastrar_monitor(self, matricula, disciplina, horarios):
        aluno = self.procurar_aluno(matricula)
        indice = self.alunos.index(aluno)

        if aluno is None:
            print("Aluno não encontrado.")
            return

        monitor = Monitor(aluno, disciplina, horarios)
        self.alunos.pop(indice)
        self.alunos.insert(indice, monitor)

        print(f"Monitor {monitor.nome} cadastrado com sucesso!\n")



    def listar_monitores(self):
        if not self.monitores:
            print("Nenhum monitor cadastrado.")
            return
        
        for monitor in self.monitores:
            print(f"{monitor.matricula} - {monitor.nome} / {monitor.disciplinaEnsinada} / {monitor.horarioDeEnsino}")


    
    def remover_monitor(self, matricula):
        for monitor in self.monitores:
            if monitor.matricula == matricula:
                self.monitores.remove(monitor)
                print("Monitor removido!")
                return
        print("Monitor não encontrado.")

    def procurar_aluno(self, matricula):
        for aluno in self.alunos:
            if aluno.matricula == matricula:
                return aluno
        return None



    def procurar_curso(self,cursoProcurado):
        for curso in self.cursos:
            if curso.nome == cursoProcurado:
                return (curso)
        return None

    def remover_aluno(self, matricula: int):
        aluno = self.procurar_aluno(matricula)
        if not aluno:
            print("Aluno não encontrado.")
            return
        self.alunos.remove(aluno)
        print("Aluno removido.")

    def listar_alunos(self):
        i = 0
        if not self.alunos:
            print("Nenhum aluno cadastrado.")
            return

        for aluno in self.alunos:
            if isinstance(aluno,Monitor):
                print(f"Matrícula: {aluno.matricula} /  Nome: {aluno.nome} / Curso: {aluno.curso} / Monitoria: {aluno.disciplinaEnsinada}")
                i+=1

            else:

                print(f"Matrícula: {aluno.matricula} / Nome: {aluno.nome} / Curso: {aluno.curso}")


    def transferir_para(self, matricula: int, destino):
        aluno = self.procurar_aluno(matricula)
        if not aluno:
            print("Aluno não encontrado.")
            return
        self.alunos.remove(aluno)
        destino.alunos.append(aluno)
        print(f"Aluno {matricula} transferido para {destino.nome}.")

    def __str__(self):
        return f"Campus {self.nome} | {len(self.alunos)} alunos"



