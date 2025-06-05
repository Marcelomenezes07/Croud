import random


def adicionar_wod():
    d = input("Data (DD/MM/AAAA): ")
    t = input("Tipo do treino: ")
    dur = input("Duração em min: ")
    mov = input("Movimentos: ")
    if d and t and dur and mov:
        with open("treino.txt", "a", encoding="utf-8") as f:  
            f.write(f"{d};{t};{dur};{mov}\n")
        print("treino adicionado com sucesso!")
    else:
        print("Nem todos os campos estão preenchidos")


def ver_wod():
    try:
        with open("treino.txt", "r", encoding="utf-8") as f:  # faz a leitura do arquivo
            treinos = f.readlines()  # conta quantas linhas possuem no arquivo
        if len(treinos) == 0:
            print("nao possui treinos")
            return
        for i, treino in enumerate(treinos):
                dados = treino.strip().split(";") # separa os movimentos do treino
                if len(dados) >= 4:
                    print(f"{i+1:^4} ---> Data: {dados[0]}\t Tipo: {dados[1]}\t Duração: {dados[2]}\t Movimentos: {dados[3]}")

    except FileNotFoundError:
        print("arquivo não encontrado")


def editar_wod():
    try:
        with open("treino.txt", "r", encoding="utf-8") as f:
            linhas = f.readlines()
        if len(linhas) == 0:
            print("não existem treinos cadastrados")
            return

        
        n_tro = linhas.index(selecionar()) #n_tro é o numero de troca
            # A funcao selecionar retorna o treino que o usuario irá selecionar de forma interativa, após isso é visto o index dela no conjunto total de treino 
        if n_tro < 0 or n_tro >= len(linhas):
            print("digite outro numero")
            return

        nd = input("digite a nova data: ")
        nt = input("digite o novo tipo: ")
        ndur = input("digite a nova duração: ")
        nmov = input("digite os novos movimentos (separados por vírgula): ")

        nova_linha = f"{nd};{nt};{ndur};{nmov}\n" #
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


def filtro():  # recebe o caminho do arquivo e retorna uma lista de treinos filtrados
    try:
        with open("treino.txt", "r", encoding="utf8") as arquivo:
            treinos = []
            for linha in arquivo:
                partes = linha.strip().split(";")
                if len(partes) == 4:  # garantir que a linha tenha os 4 campos esperados
                    treinos.append(partes)
    except FileNotFoundError:
        print("Arquivo 'treino.txt' não encontrado.")
        return []
    try:
        filtrado = treinos  # lista para armazenar os treinos filtrados
        filtros = input("Digite qual o filtro você deseja usar para buscar o treino:\n1. Data\n2. Tipo\n3. Duração\n4. Movimento\n").strip().replace(" ","").split(",")

        for filtro in filtros:
            filtro_temporario = []

            # Filtro por Data
            if filtro == "1":
                data = input("Digite a data do treino (ex: 20/04): ").strip()
                filtrado = [treino for treino in filtrado if treino[0].strip() == data]

            # Filtro por Tipo
            elif filtro == "2":
                tipo = input("Digite o tipo do treino (ex: perna, ombros...): ").strip().lower()
                filtrado = [treino for treino in filtrado if treino[1].strip().lower() == tipo]

            # Filtro por Duração
            elif filtro == "3":
                duracao_opcao = input("Digite 1 ou 2 a seguir:\n1 - Buscar duração exata\n2 - Buscar por intervalo de duração\n").strip()
                
                # duração exata
                if duracao_opcao == "1":
                    duracao = input("Digite a duração exata (em minutos): ").strip()
                    filtrado = [treino for treino in filtrado if treino[2].strip() == duracao]

                # duração por intervalo
                elif duracao_opcao == "2": 
                    try:
                        i1 = int(input("Digite o menor número do intervalo de duração (em minutos): "))
                        i2 = int(input("Digite o maior número do intervalo de duração (em minutos): "))
                        for treino in filtrado:
                            try:
                                tempo = int(treino[2].strip())  # treino[2] é a duração
                                if i1 <= tempo <= i2:
                                    filtro_temporario.append(treino)
                            except ValueError:
                                continue  # ignora treinos com duração inválida
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
                    movimentos = [movimento.strip().lower() for movimento in movimentos]
                    if movimento_buscado in movimentos:
                        filtro_temporario.append(treino)
                filtrado = filtro_temporario

            else:
                print("Filtro não encontrado!")
        
        if filtrado == []:
            print("Não foi encontrado nenhum treino com esses filtros")
        else:
            filtrado = [";".join(treino) for treino in filtrado] 
            return filtrado
    except ValueError: 
        print("Digite corretamente a opção citada")


# Funcoes meta:

def adicionar_meta():
    obj = input("Digite a meta desejada: ")
    prazo = input("Digite o prazo (DD/MM/AAAA) para concluir a meta: ")

    print("1 - não iniciada\n2 - em andamento...")
    opcao = input("Digite o status da meta acima: ").strip()

    if opcao == "1":
        status = "não iniciada"
    elif opcao == "2":
        status = "\033[33mem andamento\033[0m"
    else:
        print("Digite uma opção correta!")
        return 
    
   
    with open("metas.txt", "a", encoding="utf-8") as f:
        f.write(f"{obj};{prazo};{status}\n")
    print("Sua meta foi adicionada.")


def ver_meta():
    try:
        with open("metas.txt", "r", encoding="utf-8") as f:
            linhas = f.readlines()
        if not linhas:
            print("Não possui metas.")
            return
        for i, linha in enumerate(linhas):
            partes = linha.strip().split(";")
            if len(partes) == 3:
                obj, prazo, status = partes
                print(f"{i+1}. {obj} - prazo: {prazo} - status: {status}")
            else:
                print(f"{i+1}. [Formato inválido]")
    except FileNotFoundError:
        print("Arquivo 'metas.txt' não encontrado.")


def atualizar_meta():
    try:
        with open("metas.txt", "r", encoding="utf-8") as f:
            metas = f.readlines()

        if not metas:
            print("Não há metas para atualizar.")
            return

        print("Metas atuais:")
        for i, linha in enumerate(metas):
            partes = linha.strip().split(";")
            if len(partes) == 3:
                print(f"{i+1}. {linha.strip()}")
            else:
                print(f"{i+1}. [Formato inválido]")

        escolha = int(input("Digite o número da meta que deseja atualizar: ")) - 1

        if escolha < 0 or escolha >= len(metas):
            print("Número inválido.")
            return

        partes = metas[escolha].strip().split(";")
        if len(partes) != 3:
            print("Formato inválido da meta.")
            return

        objetivo, prazo, _ = partes

        print("Escolha o novo status da meta:")
        print("1 - em andamento\n2 - concluída\n3 - cancelada\n4 - não iniciada")
        status_opcao = input("Digite o número correspondente: ").strip()

        if status_opcao == "1":
            novo_status = "\033[33mem andamento\033[0m"  # amarelo
        elif status_opcao == "2":
            novo_status = "\033[32mconcluída\033[0m"     # verde
        elif status_opcao == "3":
            novo_status = "\033[31mcancelada\033[0m"     # vermelho
        elif status_opcao == "4":
            novo_status = "não iniciada"                 # sem cor
        else:
            print("Opção inválida.")
            return

        metas[escolha] = f"{objetivo};{prazo};{novo_status}\n"

        with open("metas.txt", "w", encoding="utf-8") as f:
            f.writelines(metas)

        print("Status da meta atualizado com sucesso!")

    except FileNotFoundError:
        print("Arquivo 'metas.txt' não encontrado.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido.")


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
            exercicios = sorteio(sugestoes[opcao])
            for i, exercicio in enumerate(exercicios):
                print(f"{i+1}- {exercicio}")
        else: 
            print("Voce nao inseriu uma opção válida")
    except ValueError:
        print("Digite um número!")


def frase_motivacional():
    try:
        with open("frases.txt", "r", encoding="utf-8") as f:
            frases = f.readlines()
    
        frase = random.choice(frases).strip()
        print("\n Frase motivacional do dia:")
        print(f"  {frase}\n")

    except FileNotFoundError:
        print("arquivo frases.txt não encontrado")



# Funções auxiliares: 

def selecionar():
    try:
        with open("treino.txt", "r", encoding="utf8") as arquivo:
            treinos = arquivo.readlines()

        chave = int(input("Digite:\n1 - Para visualizar todos os treinos\n2 - Para buscar o treino usando filtro:\n"))

        if chave == 1:
            for i, treino in enumerate(treinos):
                dados = treino.strip().split(";")
                if len(dados) >= 4:
                    print(f"Index: {i} ---> Data: {dados[0]} | Tipo: {dados[1]} | Duração: {dados[2]} | Movimentos: {dados[3]}")
            return int(input("Digite o index do treino que deseja selecionar: "))

        elif chave == 2:
            filtrados = filtro()
            if not filtrados:
                print("Nenhum treino encontrado.")
                return None

            for i, treino in enumerate(filtrados):
                dados = treino.strip().split(";")
                if len(dados) >= 4:
                    print(f"Index {i} ---> Data: {dados[0]} | Tipo: {dados[1]} | Duração: {dados[2]} | Movimentos: {dados[3]}")
            index_filtro = int(input("Selecione o treino de acordo com o index mostrado: "))
            treino_filtro = filtrados[index_filtro]

            # encontrar o índice real do treino no arquivo
            for i, linha in enumerate(treinos):
                if linha.strip() == treino_filtro.strip():
                    return i

        else:
            print("Opção inválida.")
            return None
    except (ValueError, IndexError):
        print("Erro ao selecionar treino.")
        return None


def exibir(treinos):
    for i, treino in enumerate(treinos):
        dados = treino.strip().split(";")  # separa os dados do treino
        if len(dados) >= 4:
            print(f"{i+1:^4} ---> Data: {dados[0]}\t Tipo: {dados[1]}\t Duração: {dados[2]} min\t Movimentos: {dados[3]}")

