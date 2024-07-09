# def hrs():
#   while True:
#       print("digite as horas no padrão hh/mm:")
#       horas = input("---> ") 

#       horas1 = horas.split(":")

#       horas2 = horas.isnumeric()


#       if int(horas[:2]) > 12 and int(horas1[0]) >= 0 and int(horas[:2]) <= 24:
#           horario = int(horas[:2]) - 12
#           hora2 = ("{}{} pm".format(horario, horas[2:]))
#           if int(horas1[1]) >= 60:
#               horario = int(horas1[0]) - 12
#               min1 = int(horas1[1]) % 60
#               hr1 = int(horas1[1]) // 60
#               hr2 = horario + hr1
#               if int(hr2) >= 12:
#                   h = "pm"
#                   hora2 = ("{}:{} {}".format(hr2, min1, h))
#                   return hora2
#               elif int(hr2) < 12:
#                   h = "am"
#                   hora2 = ("{}:{} {}".format(hr2, min1, h))
#                   return hora2
#           return hora2

#       elif int(horas[:2]) == 12 and int(horas1[0]) >= 0 and int(horas[:2]) <= 24:
#           horario = ("{} pm".format(horas))
#           if int(horas1[1]) >= 60:
#               horario = int(horas1[0])
#               min1 = int(horas1[1]) % 60
#               hr1 = int(horas1[1]) // 60
#               hr2 = horario+hr1
#               if int(hr2) >= 12:
#                   h = "pm"
#                   hora2 = ("{}:{} {}".format(hr2, min1, h))
#                   return hora2
#               elif int(hr2) < 12:
#                   h = "am"
#                   hora2 = ("{}:{} {}".format(hr2, min1, h))
#                   return hora2

#       elif int(horas1[0]) >= 0 and int(horas[:2]) <= 24 and int(horas[:2]) <= 12:
#           horario = ("{} am".format(horas))
#           if int(horas1[1]) >= 60:
#               horario = int(horas1[0])
#               min1 = int(horas1[1]) % 60
#               hr1 = int(horas1[1]) // 60
#               hr2 = horario+hr1
#               if int(hr2) >= 12:
#                   h = "pm"
#                   hora2 = ("{}:{} {}".format(hr2, min1, h))
#                   return hora2
#               elif int(hr2) < 12:
#                   h = "am"
#                   hora2 = ("{}:{} {}".format(hr2, min1, h))
#                   return hora2
#           return horario 

#       elif int(horas1[0]) >= 24 or int(horas1[0]) < 0 or horas2 == False :
#           print("valor não dá.\n")
#           continue


# horas = hrs()
# print("--->", horas)


# Calculadora #

#  a = print(a) if a == 0 else print("Continue")



   

class arvore:
  def __init__(self, valor):
    self.valor = valor
    self.esquerda = None
    self.direita = None

  def inserir(self, valor):
    if self.valor:
      if valor < self.valor:
        if self.esquerda is None:
          self.esquerda = arvore(valor)
        else:
          self.esquerda.inserir(valor)
      else:
        if self.direita is None:
          self.direita = arvore(valor)
        else:
          self.direita.inserir(valor)
    else:
      self.valor = valor

  def buscar(self, valor):
    if valor == self.valor:
      return True
    elif valor < self.valor:
      if self.esquerda:
        return self.esquerda.buscar(valor)
    else:
      if self.direita:
        return self.direita.buscar(valor)
    return False

  def imprimir1(self):
    if self.esquerda:
      self.esquerda.imprimir1()
    print(self.valor)
    if self.direita:
      self.direita.imprimir1()
      
  def imprimir2(self):
    if self.direita:
      self.direita.imprimir2()
    print(self.valor)
    if self.esquerda:
      self.esquerda.imprimir2()

arvore_raiz = arvore(None)

def print_ellipses(num_ellipses):
  for _ in range(num_ellipses):
    print("...", end="")
while True:
  
  a = int(input("\n\nEscolha a operção que deseja efetuar:\n\n[1] Para digitar um valor\n\n[2] Para mostrar os numeros inseridos na arvore\n\n[3] Para buscar um valor\n\n[4] Para encerra a sessão:\n\n--> "))
  
  match(a):

   case 1: 
    print("\n-------------Digite 0 se desejar voltar para o menu-------------\n")
    while True:
      b = int(input("\nDigite o valor que deseja inserir na arvore: "))
      arvore_raiz.inserir(b)
      if b == 0:
        break
   case 2:
     
       c = int(input("Choose your fighter:\n\n[1] Decrescente\n\n[2] Crescente\n\n--> "))
       if c == 1:
         arvore_raiz.imprimir2()
              
       elif c == 2: 
         arvore_raiz.imprimir1()
             
       else:
         print("Erro no valor")
               
   case 3:

     print("\n-------------Digite 0 se desejar voltar para o menu-------------\n")
     while True:
          c = int(input("\n\nDigite o valor que deseja buscar na arvore: "))
       
          if arvore_raiz.buscar(c):
              print("\nO valor está na arvore")
            
          else:
             print("\nO valor não está na arvore")
            
          if c == 0:
              break

   case 4:
        print("\n\nSessão encerrando...")
        j = 0
        for j in range (10090000):
              k = 0
              print_ellipses(3)  # Call the function to print ellipses
        if j != 0:
              print("------------Seção encerrada------------")
              break
        else:
            print("\n\nOperação inválida\n\n")

















