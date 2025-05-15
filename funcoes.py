import random


def adicionar_wod():
    d = input("Data (DD/MM/AAAA): ")
    t = input("Tipo do treino: ")
    dur = input("Duração em min: ")
    mov = input("Movimentos: ")
    with open("treino.txt", "a", encoding="utf-8") as f:  # adiciona no wods.csv os inputs acima
        f.write(f"{d};{t};{dur};{mov}\n")
    print("treino adicionado com sucesso!")

def ver_wod():
    try:
        with open("treino.txt", "r", encoding="utf-8") as f:  # faz a leitura do arquivo
            treinos = f.readlines()  # conta quantas linhas possuem no arquivo
        if len(treinos) == 0:
            print("nao possui treinos")
            return
        for i, treino in enumerate(treinos):
                dados = treino.strip().split(";") # separa os movimentos do treino
                if len(treino) >= 4:
                    print(f"{i:^4} ---> Data: {dados[0]}\t Tipo: {dados[1]}\t Duração: {dados[2]}\t Movimentos: {dados[3]}")

    except FileNotFoundError:
        print("arquivo não encontrado")


def editar_wod():
    try:
        with open("treino.txt", "r", encoding="utf-8") as f:
            linhas = f.readlines()
        if len(linhas) == 0:
            print("não existem treinos cadastrados")
            return

        
        n_tro = linhas.index(selecionar())

        if n_tro < 0 or n_tro >= len(linhas):
            print("digite outro numero")
            return

        nd = input("digite a nova data: ")
        nt = input("digite o novo tipo: ")
        ndur = input("digite a nova duração: ")
        nmov = input("digite os novos movimentos (separados por vírgula): ")

        nova_linha = f"{nd};{nt};{ndur};{nmov}\n"
        linhas[n_tro] = nova_linha

        with open("treino.txt", "w", encoding="utf-8") as f:
            f.writelines(linhas)
        print("wod editado com sucesso")

    except FileNotFoundError:
        print("arquivo não encontrado")
    except ValueError:
        print("digite um numero")

        
def excluir_wod():
    try:
        with open("treino.txt", "r", encoding="utf-8") as f:
            linhas = f.readlines()

        if len(linhas) == 0:
            print("não existem wods")
            return

       
        for i, linha in enumerate(linhas):
            partes = linha.strip().split(";")
            d = partes[0]
            t = partes[1]
            dur = partes[2]
            mov = ", ".join(partes[3:])
            print(f"{i+1}. data: {d} ; tipo: {t} ; duração: {dur}min ; movimentos: {mov}")

        
        n_exc = int(input("Digite o número do WOD que deseja excluir: ")) - 1

        if n_exc < 0 or n_exc >= len(linhas):
            print("digite outro numero")
            return

        linhas.pop(n_exc)
        with open("treino.txt", "w", encoding="utf-8") as f:
            f.writelines(linhas)

        print("o treino selecionado foi excluido")

    except FileNotFoundError:
        print("arquivo não encontrado")
    except ValueError:
        print("entrada inválida")

def adicionar_meta():
    obj = input("digite a meta desejada: ")
    prazo = input("digite o prazo (DD/MM/AAAA) para concluir a meta: ")
    status = "em andamento"

    with open("metas.txt", "a", encoding="utf-8") as f:
        f.write(f"{obj},{prazo},{status}\n")

    print("sua meta foi adicionada")

def ver_meta():
    try:
        with open("meta.txt", "r", encoding="utf-8") as f:  # faz a leitura do arquivo
            linhas = f.readlines()  # conta quantas linhas possuem no arquivo
        if len(linhas) == 0:
            print("nao possui metas")
            return
        for i, linha in enumerate(linhas):
            partes = linha.strip().split(", ")  # divide
            obj = partes[0]
            prazo = partes[1]
            status = partes[2]
           

            print(f"{i+1}. {obj}; {prazo}; {status};\n")
    except FileNotFoundError:
        print("arquivo não encontrado")


def frase_motivacional():
    try:
        with open("frases.txt", "r", encoding="utf-8") as f:
            frases = f.readlines()
    
        frase = random.choice(frases).strip()
        print("\n Frase motivacional do dia:")
        print(f"  {frase}\n")

    except FileNotFoundError:
        print("arquivo frases.txt não encontrado")

        

def filtro():  # recebe o caminho do arquivo e retorna uma lista de treinos filtrados
    with open("treino.txt", "r",encoding="utf8") as arquivo:
        treinos = [treino.split(";") for treino in arquivo.readlines()] #transforma os treinos em uma lista de treino
    filtrado = treinos  # lista para armazenar os treinos filtrados
    filtros = input("Digite qual o filtro você deseja usar para buscar o treino:\n1. Data\n2. Tipo\n3. Duração\n4. Movimento\n").strip().replace(" ","").split(",")

    for filtro in filtros:
        filtro_temporario = []
        # Filtro por Data
        if filtro == "1":
            data = input("Digite a data do treino (ex: 20/04): ").strip()
            filtrado = [treino for treino in filtrado if treino[0] == data]
        
        # Filtro por Tipo
        elif filtro == "2":
            tipo = input("Digite o tipo do treino (ex: perna, ombros...): ").strip().lower()
            filtrado = [treino for treino in filtrado if treino[1] == tipo]

        # Filtro por Duração
        elif filtro == "3":
            duracao_opcao = input("Digite 1 ou 2 a seguir:\n1 - Buscar duração exata\n2 - Buscar por intervalo de duração\n").strip()
            
            #duracao exata
            if duracao_opcao == "1":
                duracao = input("Digite a duração exata (em minutos): ").strip()
                filtrado = [treino for treino in filtrado if treino[2] == duracao]
            
            #duracao por intervalo
            elif duracao_opcao == "2": 
                try:
                    i1 = int(input("Digite o menor número do intervalo de duração (em minutos): "))
                    i2 = int(input("Digite o maior número do intervalo de duração (em minutos): "))
                    for treino in filtrado:
                        tempo = int(treino[2])  # treino[2] é a duração
                        
                        if i1 <= tempo <= i2:
                            filtro_temporario.append(treino)
                    filtrado = filtro_temporario
                except ValueError:
                    print("Valores inválidos para intervalo de duração.")

            else:
                print("Opção de duração inválida!")

        # Filtro por Movimento
        elif filtro == "4":
            movimento_buscado = input("Digite o movimento que você deseja encontrar: ").strip().lower()
            for treino in filtrado:
                movimentos = treino[3].split(",")
                movimentos = [movimento.strip()for movimento in movimentos]
                for movimento in movimentos:
                    print(movimento)
                    if movimento_buscado == movimento:
                        filtro_temporario.append(treino)
            filtrado = filtro_temporario
        else:
            print("Filtro não encontrado!")
    
    if filtrado == []:
        print("Não foi encontrado nenhum treino com esses filtros")
    else:
        #como os treinos tavam em formato de lista, separando cada campo como um intem da lista, eu to colocando cada treino como um unico elemento da lista
        filtrado = [";".join(treino) for treino in filtrado] 
        return filtrado 





def selecionar(): #Retorna um treino selecionado em formado de uma lista
    try:
        with open("treino.txt", "r", encoding="utf8") as arquivo:
            treinos = arquivo.readlines()

        chave = int(input(f"Digite:\n1-Para visualizar todos os treinos\n2-Para buscar o treino usando filtro:\n"))
        # Visualizacao completa
        if chave == 1:
            for i, treino in enumerate(treinos):
                dados = treino.strip().split(";") # separa os movimentos do treino
                if len(treino) >= 4:
                    print(f"Index: {i} ---> Data: {dados[0]} | Tipo: {dados[1]} | Duração: {dados[2]} | Movimentos: {dados[3]}")
            treino_selecionado = treinos[int(input("Digite o index do treino que voce deseja selecionar: "))]
        
        #Visualizacao por filtro 
        elif chave == 2:
            filtrados = filtro()
            for i, treino in enumerate(filtrados):
                treino = treino.strip().split(";") 
                if len(treino) >= 4:
                    print(f"Index {i} ---> Data: {treino[0]} | Tipo: {treino[1]} | Duração: {treino[2]} | Movimentos: {treino[3]}")
            treino_selecionado = filtrados[int(input("Selecione o treino de acordo com o index dele:"))]
        else:
            print("O valor digitado nao corresponde as opções acima")
        
        return treino_selecionado
    
    except ValueError:
        print("O valor que voce digitou não é valido")
    except IndexError: 
        print("O índice digitado não foi encontrado")


def sugestao_aleatoria3(): # Retorna uma lista de 3 exercicios aleatorios de acordo com o tipo escolhido pelo usuario.
    try:
        def sorteio(exercicios_salvos):
            if len(exercicios_salvos) > 3:
                selecionados = []
                for _ in range(3):  # Seleciona 3 aleatórios sem repetição
                    indice = random.randint(0, len(exercicios_salvos) - 1)
                    selecionados.append(exercicios_salvos.pop(indice))
                return selecionados
            else:
                return exercicios_salvos


        # 0 - ombro/ 1- Peito/ 2- costas/ 3- braço/ 4-pernas
        sugestoes = [["desenvolvimento","elevação lateral", "elevação frontal","Crucifixo inverso","Remada Alta","Pulley Articulado"],["supino reto","supino inclinado","Crucifixo reto","Crossover","Banch press","Crucifixo inclinado"],["remada alta","puxada","pulldown","Remada baixa", "Remada curvada","Levantamento terra"],["Rosca","Triceps Françês","Triceps na corda","Rosca Scott","Triceps testa","Mergulho"],["leg press", "agachamento livre", "agachamento com barra","flexora","Abdutora","adutora"]]
        
        
        print("Digite o treino que voce quer fazer:\n1- Ombro\n2- Peito\n3- costas\n4- Braço\n5- Pernas")
        opcao = int(input("Digite o numero que corresponde a opcao: ")) -1
        
        if 0 <= opcao < len(sugestoes): 
            print(sorteio(sugestoes[opcao]))
        else: 
            print("Voce nao inseriu uma opção válida")
    except ValueError:
        print("Digite um número!")
        


