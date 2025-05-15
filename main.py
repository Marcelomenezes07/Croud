import os ; os.system('cls')

#Funcoes criadas - Arquivo de treinos
import funcoes   ; file = "treino.txt" 
while True:
    #menu de opções
    print("1-Adicionar wod\n2-Ver Wod\n3-Editar Wod\n4-Excluir Wod\n5-filtrar wod\n6-Adicionar metas\n7-Ver Metas\n8-Atualizar metas\n9-Sugestao de wod aleatorio\n10- Frases Motivacionais para treinar inspirado\n0- Para sair do programa")
    try: 
        opcao = int(input("Digite o que voce vai querer fazer: "))
    except ValueError:
        print("O valor digitado nao corresponde a uma das opções acima")
        continue
    match opcao:
        case 1: 
            print("Você escolheu adicionar Wod")
        case 2:
            print("Você escolheu ver Wod")
        case 3:
            print("Você escolheu Editar Wod")
        case 4:
            print("Você escolheu excluir Wod")
        case 5:
            print("Você escolheu Filtrar Wod")
        case 6:
            print("Você escolheu adicionar metas")
        case 7:
            print("Você escolheu ver metas")
        case 8:
            print("Você escolheu atualizar metas")
        case 9:
            print("Você escolheu sugestão de um treino aleatório")
        case 10:
            print("Você escolheu frase motivacionais")
        case 0:
            print("Você escolheu encerrar o programa")
            break
        case _: 
            print("A opção digitada não se encontra no menu de opções")


