

def menu():

    while True:

        print("\n\n[1] Multiplicação\n\n[2] Divisão\n\n[3] Soma\n\n[4] Subtração\n\n")

        menu1 = int(input("\n\n Choose your fighter:\n\n--> "))

        match menu1:

            case 1:
                Mult()
                break
            case 2:
                Divs()
                break
            case 3:
                Soma()
                break
            case 4:
                Subs()
                break
            case 5:
                Nots()
                break
            case _:
                print("Função inválida")
                continue

def Mult():
    try:
        lett = int(input("Digite uma [letra] se quiser sair!\n\n\nDigite os valores:\n\n--> "))
    except (ValueError):
        menu()

    else:
        return 0



def Divs():
    return 0

def Soma():
    return 0

def Subs():
    return 0

def Nots():
    return 0


print("---------------------------\n      QUER COMEÇAR?\n---------------------------")

começo = int(input("[1] Sim\n\n[2] Não\n\n--> "))

match começo:

    case 1:
         menu()

    case 2:
        print("Acabou")