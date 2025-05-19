from models.aluno import Aluno
from models.curso import Curso

#MAIUSCULO PARA VARIÁVEL GLOBAL
CURSOS = {}
ALUNOS = {}

def criar_aluno(nome, nascimento, nome_curso=None):
    if not nome or not nascimento:
        return "Parâmetros inválidos"
    c = None
    aluno_objeto = Aluno(nome, nascimento)

    if nome_curso:
        c = CURSOS.get(nome_curso)
        #c["alunos"].append(aluno_objeto)
        #c.alunos.append(aluno_objeto)
        c.alunos[aluno_objeto.matricula] = aluno_objeto
    #ALUNOS.append({aluno_objeto.matricula: aluno_objeto})
    ALUNOS[aluno_objeto.matricula] = aluno_objeto

    return {
        "nome_aluno":aluno_objeto.nome,
        "matricula": aluno_objeto.matricula,
        "curso": c.nome or None
        #"curso":c.get("nome_curso")
    }

def listar_alunos():
    resposta=""
    for aluno in ALUNOS.values():
        resposta += (f"\nNome: {aluno.nome} \n"
                     f"Matrícula: {aluno.matricula} \n"
                     f"Curso: {aluno.curso.nome if aluno.curso else "Sem curso no momento"} \n"
                     f"-------------------------\n"
                     f"")
    return resposta

def detalhar_aluno(matricula):
    if not matricula:
        return "Parâmetros Inválidos"

    aluno = ALUNOS.get(matricula)

    if not aluno:
        return "Este aluno não está cadastrado."

    return (f"Nome: {aluno.nome} \n"
            f"Matrícula: {aluno.matricula} \n"
            f"Data de nascimento: {aluno.nascimento} \n"
            f"Data de ingresso: {aluno.ingresso} \n"
            f"Curso: {aluno.curso.nome if aluno.curso else "Sem curso no momento"} \n"
            f"Notas: {aluno.notas}")

def deletar_aluno(matricula):
    if not matricula:
        return "Parâmetros inválidos"

    aluno = ALUNOS.get(matricula)

    if not aluno:
        return "Este aluno não está cadastrado."

    if aluno.curso:
        curso = CURSOS.get(aluno.curso.nome)
        curso.alunos.pop(matricula)

    ALUNOS.pop(matricula)

    return "Aluno excluído com sucesso."

#FIM LÓGICA ALUNO

#INICIO LÓGICA CURSO

def cadastrar_curso(nome, duracao, professor, materias):
    if not nome or not duracao or not professor or not materias:
        return "Não é possível cadastrar curso sem todos os dados."

    curso_objeto = Curso(nome,duracao,professor,materias)
    CURSOS[curso_objeto.nome] = curso_objeto
    return f"Curso {curso_objeto.nome} cadastrado."

def listar_cursos():
    resposta = ""
    for curso in CURSOS.values():
        resposta += (f"\nNome do curso: {curso.nome} \n"
                     f"Duração: {curso.duracao} \n"
                     f"Professor: {curso.professor} \n"
                     f"Matérias: {curso.materias}"
                     f"-------------------------\n"
                     f"")
    return resposta

def detalhar_curso(nome):
    if not nome:
        return "Parâmetros inválidos."

    curso = CURSOS.get(nome)

    if not curso:
        return "Curso não encontrado."


    return (f"\nNome do curso: {curso.nome} \n"
    f"Duração: {curso.duracao} \n"
    f"Professor: {curso.professor} \n"
    f"Matérias: {curso.materias}"
    f"-------------------------\n"
    f"")

def excluir_curso(nome):
    pass
    if not nome:
        return "Curso não informado."
    curso = CURSOS.get(nome)

    if not curso:
        return "Curso não encontrado."

    CURSOS.pop(curso)
    return "Curso excluído com sucesso."