import datetime
from uuid import uuid4

from models.curso import Curso


class Aluno:
#Construtor com atributos.
    def __init__(self, nome, nascimento):
        self.nome = nome
        self.nascimento = nascimento
        self.matricula = str(uuid4())
        self.ingresso = datetime.timezone
        self.curso = None
        self.notas = []

#Comportamentos
    def marcar_prova(self, data_prova, nome_prova):
        provas = {}
        prova = provas.get(nome_prova)

        if not prova:
            raise Exception

        prova["data"] = data_prova
        prova["aluno"] = self.matricula

        return f"Sua prova foi marcada para o dia {data_prova} com sucesso"

    def fazer_media(self):
        if not self.notas:
            return "Nenhuma nota foi encontrada."

        media = sum(self.notas) / len(self.notas)

        return f"Sua média é de {media}"

    def repor_aula(self, nome_aula, data_reposicao):
        aulas_perdidas = {}
        aula = aulas_perdidas.get(nome_aula)

        if not aula:
            return "Você já fez esta aula"

        aula["data_reposicao"] = data_reposicao
        aula["aluno"] = self.matricula

        return f"Sua aula foi marcada para o dia {data_reposicao}"


