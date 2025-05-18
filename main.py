from app.logica_sistema import criar_aluno, listar_alunos, detalhar_aluno, deletar_aluno

comando=""
while comando != "sair":
    comando = input(f"Escolha uma opção: \n"
                    f"1) Cadastrar Aluno \n"
                    f"2) Listar Alunos \n"
                    f"3) Detalhar Aluno \n"
                    f"4) Deletar Aluno \n"
                    f"Digita 'sair' para sair do sistema \n")

    match comando:
        case "1":
            nome = input("Informe o nome do aluno:")
            nascimento = input("Informe a data de nascimento do aluno:")
            curso = input("Informe o curso do aluno se tiver, se não, deixe vazio.")
            print(criar_aluno(nome, nascimento, curso))

        case "2":
            print(listar_alunos())
        case "3":
            matricula = input("Informe a matrícula do aluno:")
            print(detalhar_aluno(matricula))
        case "4":
            matricula = input("Informe a matrícula do aluno:")
            print(deletar_aluno(matricula))

        case "sair":
            print("Saindo do sistema...")


            #teste pull.