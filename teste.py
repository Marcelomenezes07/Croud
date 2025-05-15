
# file = "projetofp/treino.txt"

# def adicionar_wod():
#     d = input("Data (DD/MM/AAAA): ")
#     t = input("Tipo (AMRAP/EMOM/For Time): ")
#     dur = input("Duração (min): ")
#     mov = input("Movimentos (vírgula): ")
#     with open(file, "a") as f:
#         f.write(f"{d} {t} {dur} {mov}\n")
#     print("treino modificado com sucesso")

# def editar():
#     with open(file,"r") as arquivo:
#         treinos = arquivo.readlines()   
#     filtrado = []  #colocando uma lista para exibir o que foi filtrado 
#     filtro = input("Digite qual o filtro voce deseja usar para buscar o treino:\n1data\n2tipo\n3.dur\n4movimento")
    
#     if filtro == 1: 
#         data = input("Digite a data que deseja modificar: ") 
#         for treino in treinos: # percorrendo a lista de treinos 
#             if data == treino[0]: # treino 0 é o index da data
#                 filtrado.append(treino) # guardando o treino na lista que sera exibida
#     elif




# def filtro(): # retorna uma lista de treinos filtrados de acordo com as seleçoes
#     with open(file,"r") as arquivo:
#         treinos = arquivo.readlines()   
#     filtrado = []  #colocando uma lista para exibir o que foi filtrado 
#     filtro = input("Digite qual o filtro voce deseja usar para buscar o treino:\n1data\n2tipo\n3.duracão\n4movimento")
    
#     if filtro == 1: 
#         data = input("Digite a data do treino: ") 
#         for treino in treinos: # percorrendo a lista de treinos 
#             if data == treino[0]: # treino 0 é o index da data
#                 filtrado.append(treino) # guardando o treino na lista que sera exibida
    
#     elif filtro == 2:
#         tipo = input("digite o tipo do treino: ")
#         for treino in treinos:
#             if tipo == treino[1]:
#                 filtrado.append(treino)
    
#     elif filtro == 3:
#         duracao = input("Digite o numero que corresponde a opção selecionada\n1.para buscar exatamente a duração do treino\n2.Para buscar uma faixa de duração do texto")
#         if duracao == 1: 
#             duracao = input("Digite o tempo de treino")
#             for treino in treinos:
#                 if duracao == treino[2]:
#                     filtrado.append(treino)        
#         elif duracao == 2:
#             i1 = input("Digite o menor número do intervalo de tempo: ")
#             i2 = input("Digite o maior numero do intervalo: ")
#             if duracao > i1 and duracao < i2:
#                 filtrado.append(treino)
#         else: print("opção não encontrada!")  

#     elif filtro == 4:
#         movimento = input("Digite o movimento que voce deseja encontrar: ")
#         for treino in treinos: 
#             if movimento == treino[3]:
#                 filtrado.append(treino)
        
    
    
#     else:
#         print("Filtro não encontrado!")

#     return filtrado  

# def filtro(): # retorna uma lista de treinos filtrados de acordo com as seleçoes
#     with open(file,"r") as arquivo:
#         treinos = [treino.split(";") for treino in arquivo.readlines()]
#     filtrado = []  #colocando uma lista para exibir o que foi filtrado 
#     filtro = input("Digite qual o filtro voce deseja usar para buscar o treino:\n1data\n2tipo\n3.duracão\n4movimento").strip()
    
    

#         if filtro == "1": 
#             data = input("Digite a data do treino: ") 
#             for treino in treinos: # percorrendo a lista de treinos 
#                 if data == treino[0]: # treino 0 é o index da data
#                     filtrado.append(treino) # guardando o treino na lista que sera exibida
        
#         elif filtro == "2":
#             tipo = input("digite o tipo do treino: ")
#             for treino in treinos:
#                 if tipo == treino[1]:
#                     filtrado.append(treino)
        
#         elif filtro == "3":
#             duracao = input("Digite o numero que corresponde a opção selecionada\n1.para buscar exatamente a duração do treino\n2.Para buscar uma faixa de duração do texto")
#             if duracao == 1: 
#                 duracao = input("Digite o tempo de treino")
#                 for treino in treinos:
#                     if duracao == treino[2]:
#                         filtrado.append(treino)        
#             elif duracao == 2:
#                 i1 = int(input("Digite o menor número do intervalo de tempo: "))
#                 i2 = int(input("Digite o maior numero do intervalo: "))
#                 if duracao > i1 and duracao < i2:
#                     filtrado.append(treino)
#             else: print("opção não encontrada!")  

#         elif filtro == "4":
#             movimentoe = input("Digite o movimento que voce deseja encontrar: ").lower().strip()
#             for treino in treinos: 
#                 movimentos = treino[3].split(",")
#                 for movimento in movimentos:
#                     if movimentoe == movimento:
#                         filtrado.append(treino)
            
#         else:
#             print("Filtro não encontrado!")
        
#     filtrado = list(map(list, set(tuple(t) for t in filtrado))) #remove as duplicadas, o primeiro parentese ta transformando os treinos em tupla, o segundo ta transformando a lista de treinos em set pra poder apagar os repetidos, O map ta transformando os treinos internos de lista pra tupla e o list no final ta transofrmando o set em list (as chaves mais externas).

#     return filtrado  


# file = "treino.txt"
# def filtro(file):  # recebe o caminho do arquivo
#     with open(file, "r") as arquivo:
#         treinos = [treino.split(";") for treino in arquivo.readlines()] #transforma os treinos em uma lista de treino
#     filtrado = treinos  # lista para armazenar os treinos filtrados
#     filtros = input("Digite qual o filtro você deseja usar para buscar o treino:\n1. Data\n2. Tipo\n3. Duração\n4. Movimento\n").strip().replace(" ","").split(",")

#     for filtro in filtros:
#         filtro_temporario = []
#         # Filtro por Data
#         if filtro == "1":
#             data = input("Digite a data do treino (ex: 20/04): ").strip()
#             filtrado = [treino for treino in filtrado if treino[0] == data]
        
        

#         # Filtro por Tipo
#         elif filtro == "2":
#             tipo = input("Digite o tipo do treino (ex: perna, ombros...): ").strip().lower()
#             filtrado = [treino for treino in filtrado if treino[1] == tipo]

#         # Filtro por Duração
#         elif filtro == "3":
#             duracao_opcao = input("Digite 1 ou 2 a seguir:\n1 - Buscar duração exata\n2 - Buscar por intervalo de duração\n").strip()
            
#             #duracao exata
#             if duracao_opcao == "1":
#                 duracao = input("Digite a duração exata (em minutos): ").strip()
#                 filtrado = [treino for treino in filtrado if treino[2] == duracao]
            
#             #duracao por intervalo
#             elif duracao_opcao == "2": 
#                 try:
#                     i1 = int(input("Digite o menor número do intervalo de duração (em minutos): "))
#                     i2 = int(input("Digite o maior número do intervalo de duração (em minutos): "))
#                     for treino in filtrado:
#                         tempo = int(treino[2])  # treino[2] é a duração
                        
#                         if i1 <= tempo <= i2:
#                             filtro_temporario.append(treino)
#                     filtrado = filtro_temporario
#                 except ValueError:
#                     print("Valores inválidos para intervalo de duração.")

#             else:
#                 print("Opção de duração inválida!")

#         # Filtro por Movimento
#         elif filtro == "4":
#             movimento_buscado = input("Digite o movimento que você deseja encontrar: ").strip().lower()
#             for treino in filtrado:
#                 for movimento in treino:
#                     if movimento_buscado == movimento:
#                         filtro_temporario.append(treino)
#             filtrado = filtro_temporario
#         else:
#             print("Filtro não encontrado!")
#     if filtrado == []:
#         print("Não foi encontrado nenhum treino com esses filtros")
#     else:
#         return filtrado


# def atualizar_meta():
#     try:
#         with open("metas.txt", "r", encoding="utf-8") as f:
#             metas = f.readlines()

#         if not metas:
#             print("Não há metas para atualizar.")
#             return

#         print("Metas atuais:")
#         for i, linha in enumerate(metas):
#             partes = linha.strip().split(",")
#             if len(partes) == 3:
#                 print(f"{i+1}. {linha.strip()}")
#             else:
#                 print(f"{i+1}. [Formato inválido]")

#         escolha = int(input("Digite o número da meta que deseja atualizar: ")) - 1

#         if escolha < 0 or escolha >= len(metas):
#             print("Número inválido.")
#             return

#         partes = metas[escolha].strip().split(",")
#         if len(partes) != 3:
#             print("Formato inválido da meta.")
#             return

#         objetivo, prazo, _ = partes

#         print("Escolha o novo status da meta:")
#         print("1 - em andamento\n2 - concluída\n3 - cancelada")
#         status_opcao = input("Digite o número correspondente: ").strip()

#         if status_opcao == "1":
#             novo_status = "\033[33mem andamento\033[0m"  # amarelo
#         elif status_opcao == "2":
#             novo_status = "\033[32mconcluída\033[0m"     # verde
#         elif status_opcao == "3":
#             novo_status = "\033[31mcancelada\033[0m"     # vermelho
#         else:
#             print("Opção inválida.")
#             return

#         metas[escolha] = f"{objetivo},{prazo},{novo_status}\n"

#         with open("metas.txt", "w", encoding="utf-8") as f:
#             f.writelines(metas)

#         print("Status da meta atualizado com sucesso!")

#     except FileNotFoundError:
#         print("Arquivo 'metas.txt' não encontrado.")
#     except ValueError:
#         print("Entrada inválida. Por favor, digite um número válido.")

# cores =  { 
#     "negrito" : "\033[1m",
#     "padrao" : "\033[0m",
    
# }   

# print(f"{cores['negrito']}ola mundo{cores['padrao']}")
# print(f"ola mundo")
def inicio():
    print("\n" + "╔" + "═" * 58 + "╗")
    print("║" + " " * 58 + "║")
    print("║{:^60}║".format("🏋️  BEM-VINDO AO SEU APLICATIVO DE TREINOS  🏋️"))
    print("║" + " " * 58 + "║")
    print("║{:^57}║".format("Prepare-se para alcançar suas metas! 💪"))
    print("║" + " " * 58 + "║")
    print("╚" + "═" * 58 + "╝\n")
    print()
    print("----------------Pressione enter para entrar!----------------")
    input()

def exibir_menu():
    print("\n" + "╔" + "═" * 58 + "╗")
    print("║" + " " * 58 + "║")
    print("║{:^60}║".format("🏋️  Menu principal  🏋️"))
    print("║" + " " * 58 + "║")
    print("╚" + "═" * 58 + "╝\n")
    print()

inicio()
exibir_menu()

