alunos = []


def adicionar_notas():
    while True:
        notas = {}
        for j in range(3):  # Pode mudar a quantidade de notas
            nota = float(input(f"Nota {j+1} --> "))
            notas[j+1] = nota

        print("\nNotas digitadas:")
        for k, v in notas.items():
            print(f"Nota {k}: {v}")

        conf = input("\n\nAs notas estão corretas? (s/n)\n\n--> ").lower()
        if conf == "s":
            return notas
        else:
            print("\nDigite novamente\n")


def listar_alunos():

    if not alunos:
        print("\n\nNão há alunos cadastrados\n")
        return

    while True:
        print("\nAlunos cadastrados:\n")
        for i, (nome, _) in enumerate(alunos):
            print(f"{i}) {nome}")

        esc = input("\n\nDigite o número do aluno para ver suas notas ou 'sair' para voltar\n\n--> ")
        if esc.lower() == "sair":
            break
        else:
            esc = int(esc)
            if 0 <= esc < len(alunos):
                nome, notas = alunos[esc]
                print(f"\n{nome} - Notas:")
                if notas:
                    for k, v in notas.items():
                        print(f"Nota {k}: {v}")
                else:
                    print("Sem notas cadastradas")
                input("\n\nPressione ENTER para voltar à lista\n")
            else:
                print("\nNúmero inválido")


def menu():
    while True:

        try:
         escolha = int(input("__________________________\n\n1) Alunos\n\n2) Notas\n\n3) Buscar aluno\n\n4) Médias\n\n0) SAIR\n\n--> "))

        except ValueError:
            print("\nDigite um número válido\n")
            continue

        
        if escolha == 1:
            
            while True:
                listar_alunos()

                print("Digite '0' para sair\nDigite 'apagar' para deletar um aluno")
                nome = input("\n\nDigite o nome do novo aluno\n\n--> ")

                if nome == "0":
                    break

                elif nome.lower() == "apagar":
                    if not alunos:
                        print("\n\nNão há alunos para apagar\n")
                        continue

                    for i, (nome, _) in enumerate(alunos):
                        print(f"{i}) {nome}")

                    esc = int(input("\n\nQual número deseja apagar?\n\n--> "))

                    if 0 <= esc < len(alunos):
                        alunos.pop(esc)

                else:
                    alunos.append((nome, {}))  # Notas vazias no início
                    

        elif escolha == 2:

            if not alunos:
                print("\n\nNão há alunos cadastrados\n")
                continue

            print("\n\nAlunos:\n")

            for i, (nome, notas) in enumerate(alunos):
                print(f"{i}) {nome} - Notas: {notas if notas else 'Sem notas'}")

            esc = input("\n\nDigite o número do aluno para adicionar/alterar notas ou 'sair' para voltar\n\n--> ")
            if esc != "sair":
                esc = int(esc)

                if 0 <= esc < len(alunos):
                    novas_notas = adicionar_notas()
                    nome_antigo = alunos[esc][0]
                    alunos[esc] = (nome_antigo, novas_notas)
                    print(f"\nNotas de {nome_antigo} atualizadas com sucesso!\n")

                else:
                    print("\nAluno inválido\n")


        elif escolha == 3:

            if not alunos:
                print("\n\nNão há alunos cadastrados\n")
                continue

            busca = input("\n\nDigite o nome do aluno que deseja buscar\n\n--> ").lower()
            achou = False
            for nome, notas in alunos:
                if nome.lower() == busca:
                    print(f"\n{nome} - Notas: {notas if notas else 'Sem notas'}")
                    achou = True
            if not achou:
                print("\n\nAluno não encontrado\n")


        elif escolha == 4:

            if not alunos:
                print("\n\nNão há alunos cadastrados\n")
                continue

            print("\n\nMédias dos alunos:\n")

            for nome, notas in alunos:

                if notas:
                    media = sum(notas.values()) / len(notas)
                    print(f"{nome} - Média: {media:.2f}")

                else:
                    print(f"{nome} - Sem notas")
            input("\n\nPressione ENTER para voltar ao menu\n")


        elif escolha == 0:

            break

menu()
