def filtro(file):  # recebe o caminho do arquivo
    with open(file, "r") as arquivo:
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
                for movimento in treino:
                    if movimento_buscado == movimento:
                        filtro_temporario.append(treino)
            filtrado = filtro_temporario
        else:
            print("Filtro não encontrado!")
    if filtrado == []:
        print("Não foi encontrado nenhum treino com esses filtros")
    else:
        return filtrado
