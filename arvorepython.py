



# class arvore:
#     def __init__(self, valor):
#       self.valor = valor
#       self.esquerda = None
#       self.direita = None
  
#     def inserir(self, valor):
#       if self.valor:
#         if valor < self.valor:
#           if self.esquerda is None:
#             self.esquerda = arvore(valor)
#           else:
#             self.esquerda.inserir(valor)
#         else:
#           if self.direita is None:
#             self.direita = arvore(valor)
#           else:
#             self.direita.inserir(valor)
#       else:
#         self.valor = valor
  
#     def buscar(self, valor):
#       if valor == self.valor:
#         return True
#       elif valor < self.valor:
#         if self.esquerda:
#           return self.esquerda.buscar(valor)
#       else:
#         if self.direita:
#           return self.direita.buscar(valor)
#       return False
  
#     def imprimir1(self):
#       if self.esquerda:
#         self.esquerda.imprimir1()
#       print(self.valor)
#       if self.direita:
#         self.direita.imprimir1()
  
#     def imprimir2(self):
#       if self.direita:
#         self.direita.imprimir2()
#       print(self.valor)
#       if self.esquerda:
#         self.esquerda.imprimir2()
  


# arvore_raiz = arvore(None)

  
# a = int(input("\n\nEscolha a operção que deseja efetuar:\n\n[1] Para digitar um valor\n\n[2] Para mostrar os numeros inseridos na arvore\n\n[3] Para buscar um valor\n\n[4] Para encerra a sessão:\n\n--> "))
    
# match(a):
    
#        case 1: 
#         print("\n-------------Digite 0 se desejar voltar para o menu-------------\n")
#         while True:
#           b = int(input("\nDigite o valor que deseja inserir na arvore:\n\n--> "))
#           arvore_raiz.inserir(b)
#           if b == 0:
#             break
#        case 2:
    
#            c = int(input("Choose your fighter:\n\n[1] Decrescente\n\n[2] Crescente\n\n--> "))
#            if c == 1:
#              arvore_raiz.imprimir2()
    
#            elif c == 2: 
#              arvore_raiz.imprimir1()
    
#            else:
#              print("Erro no valor")
    
#        case 3:
    
#          print("\n-------------Digite 0 se desejar voltar para o menu-------------\n")
#          while True:
#               c = int(input("\n\nDigite o valor que deseja buscar na arvore:\n\n--> "))
    
#               if arvore_raiz.buscar(c):
#                   print("\nO valor está na arvore")
    
#               else:
#                  print("\nO valor não está na arvore")
    
#               if c == 0:
#                   break
    
#        case 4:
         
#               print("\nSessão encerrando...")
#               for i in range(10000000):
#                 k = 0
#                 if i == 9999999:
#                   print("\n------------Sessão encerrada------------\n")
#                   break
                
          

while True:
  a = input("\nTinha o pet e o repete, o pete morreu, quem sobrou?\n\n--> ").lower()
  
  if a == "repete":
    continue
  elif a == "vou me matar":
    print("Ok, parei")
    break
  else:
    print("\nNão, vou repetir\n")
    







