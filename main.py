from campus_lista.campus import Campus

def criar_campi_ufc():
    campi = []

    # Fortaleza – Campus do Pici
    pici = Campus("Fortaleza - Pici")
    for curso in [
        "Computação", "Engenharia Elétrica", "Engenharia Civil", "Engenharia Mecânica",
        "Engenharia de Produção", "Estatística", "Matemática", "Química"
    ]:
        pici.cadastrar_curso(curso)
    campi.append(pici)

    # Fortaleza – Benfica
    benfica = Campus("Fortaleza - Benfica")
    for curso in [
        "Direito", "Administração", "Ciências Contábeis",
        "Arquitetura", "Biblioteconomia", "Ciências Sociais",
        "Filosofia", "História", "Geografia"
    ]:
        benfica.cadastrar_curso(curso)
    campi.append(benfica)

    # Fortaleza – Porangabuçu
    poranga = Campus("Fortaleza - Porangabuçu")
    for curso in [
        "Medicina", "Enfermagem", "Nutrição", "Odontologia",
        "Fisioterapia", "Educação Física", "Farmácia"
    ]:
        poranga.cadastrar_curso(curso)
    campi.append(poranga)

    # Sobral
    sobral = Campus("Sobral")
    for curso in [
        "Engenharia Elétrica", "Engenharia da Computação",
        "Psicologia", "Odontologia", "Medicina"
    ]:
        sobral.cadastrar_curso(curso)
    campi.append(sobral)

    # Quixadá
    quixada = Campus("Quixadá")
    for curso in [
        "Engenharia de Software", "Ciência da Computação",
        "Sistemas de Informação", "Engenharia de Computação",
        "Design Digital"
    ]:
        quixada.cadastrar_curso(curso)
    campi.append(quixada)

    # Russas
    russas = Campus("Russas")
    for curso in [
        "Engenharia Civil", "Engenharia de Produção",
        "Engenharia Mecânica", "Engenharia de Software"
    ]:
        russas.cadastrar_curso(curso)
    campi.append(russas)

    # Crateús
    crateus = Campus("Crateús")
    for curso in [
        "Engenharia Civil", "Engenharia de Minas",
        "Engenharia de Produção", "Engenharia de Software"
    ]:
        crateus.cadastrar_curso(curso)
    campi.append(crateus)

    # Itapajé
    itapaje = Campus("Itapajé")
    for curso in [
        "Análise e Desenvolvimento de Sistemas",
        "Segurança da Informação",
        "Ciência de Dados"
    ]:
        itapaje.cadastrar_curso(curso)
    campi.append(itapaje)

    return campi


def menu_principal():
    print("\nSISTEMA DE UNIVERSIDADES")
    print("1 - Criar campus")
    print("2 - Selecionar campus")
    print("3 - Listar campi")
    print("0 - Sair")
    return input("Opção: ")


def menu_campus(campus, campi):
    while True:
        print(f"\nCampus: {campus.nome}")
        print("1 - Cadastrar curso")
        print("2 - Listar cursos")
        print("3 - Cadastrar aluno")
        print("4 - Listar alunos")
        print("5 - Remover aluno")
        print("6 - Transferir aluno para outro campus")
        print("7 - Cadastrar um monitor")
        print("8 - Remover um monitor")
        print("9 - Listar todos os monitores do campus")
        print("0 - Voltar")
        opcao = input("Opção: ")

        if opcao == "1":
            nome = input("Nome do curso: ")
            campus.cadastrar_curso(nome)

        elif opcao == "2":
            campus.listar_cursos()

        elif opcao == "3":
            nome = input("Nome do aluno: ")
            print("Cursos disponíveis:")
            campus.listar_cursos()
            curso = input("Curso: ")
            campus.cadastrar_aluno(nome, curso)

        elif opcao == "4":
            campus.listar_alunos()

        elif opcao == "5":
            mat = int(input("Matrícula: "))
            campus.remover_aluno(mat)

        elif opcao == "6":
            mat = int(input("Matrícula do aluno: "))
            print("\nCampi disponíveis:")
            for i, c in enumerate(campi):
                print(f"{i+1} - {c.nome}")
            destino = campi[int(input("Destino: ")) - 1]
            campus.transferir_para(mat, destino)

        elif opcao == "7":
            cursoAsk = input("Para qual curso o aluno será monitor?\n")
            mat = int(input("Matrícula do aluno: "))

            aluno = campus.procurar_aluno(mat)
            curso  = campus.procurar_curso(cursoAsk)

            if aluno is None:
                print("Aluno inexistente")
            elif curso is None:
                print("Curso inexistente")
            else:
                horarioDisponivel = input("Okay, em que momento da semana o monitor está disponível? \n")
                campus.cadastrar_monitor(mat, cursoAsk, horarioDisponivel)


        
        elif opcao == "8":
            mat = int(input("Matrícula: "))
            campus.remover_monitor(mat)

        elif opcao == "9":
            campus.listar_monitores()




        elif opcao == "0":
            break

        else:
            print("Opção inválida.")


def main(campi):
    while True:
        op = menu_principal()

        if op == "1":
            nome = input("Nome do campus: ")
            novo = Campus(nome)
            campi.append(novo)
            print("Campus criado.")

        elif op == "2":
            if not campi:
                print("Nenhum campus cadastrado.")
                continue

            print("\nCampi disponíveis:")
            for i, c in enumerate(campi):
                print(f"{i+1} - {c.nome}")

            escolhido = campi[int(input("Escolha: ")) - 1]
            menu_campus(escolhido, campi)

        elif op == "3":
            for c in campi:
                print(c)

        elif op == "0":
            print("Encerrando...")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    campi = criar_campi_ufc()
    main(campi)
