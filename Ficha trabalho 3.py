#-------------------------------------------------------------------------------
#                       Ficha de Trabalho nº 3
#
# Curso: Fundamentos de Python
# UFCD/Módulo/Temática: UFCD: 10793 - Fundamentos de Python
# Ação: 10793_02/L
#
# Nome do Formando: Ulisses Miguel Loureiro Alvarinho
#
#-------------------------------------------------------------------------------

#inicio do programa


lista_personagens = []            #lista que vai contem os dicionarios de cada personagem

def adicionar_personagem():       #função para adicionar personagem, pedindo nome, idade, profissão, hobbies e descrição
    nome = input("Digite o nome do personagem: ")
    try:
        idade = int(input("Digite a idade do personagem: "))
    except:
        print("Erro. Digite numero inteiro")
        idade = int(input("Digite a idade do personagem: "))
    try:
        profissao = (input("Digite a profissão do personagem: "))
    except:
        print("Erro. Profissão inválida.")
        profissao= int(input("Digite a idade do personagem: "))
    hobbies = input("Digite os hobbies do personagem, separados por vírgula: ").split(",")
    descricao = input("Digite uma breve descrição do personagem: ")
    
   
    personagem = {                #definção do dicionario personagem e suas informações
        "nome": nome,
        "idade": idade,
        "profissão": profissao,
        "hobbies": hobbies,
        "descrição": descricao,
        }
    lista_personagens.append(personagem)  #adiciona o dicionario personagem à lista de personagens
    
def modificar_personagem(lista_personagens): #função para modificar as informações da personagem
    for personagem in lista_personagens:
        print(personagem["nome"])
    pesquisa_nome=input("Qual a personagem a modificar? Introduza o nome: ") #pede o nome da personagem
    print("Personagem selecionada: ", pesquisa_nome) 
    personagem_encontrada = False
    for personagem in lista_personagens:
        if personagem["nome"]==pesquisa_nome:   #verifica se existe o nome da personagem no dicionario 
            personagem_encontrada = True
            #exibe opções das informações de personagem       
            print("1. Idade")               
            print("2. Profissão")
            print("3. Hobbies")
            print("4. Descrição")
            campo=input("Qual a informação a modificar?: ") #pergunta a informação a modificar
            if campo=="1":
                personagem["idade"]=input("Digite novo valor para idade: ")
                break
            if campo=="2":
                personagem["profissão"]=input("Digite novo valor para profissão: ")
                break
            if campo=="3":
                personagem["hobbies"]=input("Digite novo valor para hobbies: ").split(",")
                break
            if campo=="4":
                personagem["descrição"]=input("Digite novo valor para descrição: ")
                break    
            else:
                print("Opção inválida. Tente novamente.") 
            
            
    if personagem_encontrada == False:
             print("Personagem não consta na lista. Tente novamente.")
          
            

def remover_personagem(lista_personagens):  #função para remover personagem
    for personagem in lista_personagens:
        print(personagem["nome"])
    pesquisa=input("Qual a personagem a remover? Introduza o nome: ")
    personagem_encontrada = False
    for personagem in lista_personagens:
        if personagem["nome"].lower()==pesquisa.lower():    #procura nome da personagem no dicionario
            lista_personagens.remove(personagem)    #remove personagem da lista
            print("Personagem removida.")
            personagem_encontrada = True
            break
    if personagem_encontrada == False:
             print("Personagem não consta na lista. Tente novamente.")
             
def pesquisar_personagem(lista_personagens): #função para pesquisar por nome de personagem na lista
    pesquisa=input("Qual a personagem a pesquisar? Introduza o nome: ")
    personagem_encontrada = False
    for personagem in lista_personagens:
        if personagem["nome"]==pesquisa:
            print("Personagem encontrada.")
            personagem_encontrada = True
            print("                           ")
            print("---------------------------")
            print("Nome:", personagem["nome"])
            print("Idade:", personagem["idade"])
            print("Profissão:", personagem["profissão"])
            print("Hobbies:", ", ".join(personagem["hobbies"]))
            print("Descrição:", personagem["descrição"])
            break
    if personagem_encontrada == False:
        print("Personagem não encontrada. Tente novamente.")
           
       
    
def visualizar_personagens(lista_personagens): #função para apresentar a personagem e suas informações
    for personagem in lista_personagens:
        print("                           ")
        print("---------------------------")
        print("Nome:", personagem["nome"])
        print("Idade:", personagem["idade"])
        print("Profissão:", personagem["profissão"])
        print("Hobbies:", ", ".join(personagem["hobbies"]))
        print("Descrição:", personagem["descrição"])


while True:                                  #ciclo de menu de opções do programa
    print("                           ")
    print("1. Adicionar personagem")
    print("2. Modificar personagem")
    print("3. Remover personagem")
    print("4. Visualizar personagens")
    print("5. Pesquisar personagem")
    print("6. Sair")
    print("                           ")
    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        adicionar_personagem()
    elif opcao == 2:
        modificar_personagem(lista_personagens)
    elif opcao == 3:
        remover_personagem(lista_personagens)
    elif opcao == 4:
        visualizar_personagens(lista_personagens)
    elif opcao == 5:
        pesquisar_personagem(lista_personagens)
    elif opcao == 6:
        break
    else:
        print("Opção inválida. Tente novamente.")

