import os; os.system('cls')

#Funcoes criadas -  parte grafica -  Arquivo de treinos
import funcoes ; import interface ; file = "treino.txt" 
formato =  { 
    "negrito" : "\033[1m",
    "padrao" : "\033[0m",
}   

interface.inicio()
while True:
    #Placa do menu 
    interface.exibir_menu()
    #menu de opções
    print("\n 1-Adicionar wod\n 2-Ver Wod\n 3-Editar Wod\n 4-Excluir Wod\n 5-Filtrar wod\n 6-Adicionar metas\n 7-Ver Metas\n 8-Atualizar metas\n 9-Sugestao de wod aleatorio\n10-Frases Motivacionais para treinar inspirado\n0- Para sair do programa")
    try: 
        opcao = int(input("Digite o que voce vai querer fazer: "))
    except ValueError:
        print("O valor digitado nao corresponde a uma das opções acima")
        continue

    match opcao:
        case 1: 
            os.system('cls')
            print(f"{formato['negrito']}Você escolheu adicionar Wod\n{formato['padrao']}")
            funcoes.adicionar_wod()

        case 2:
            os.system('cls')
            print(f"{formato['negrito']}Você escolheu ver wod\n{formato['padrao']}")
            funcoes.ver_wod()

        case 3:
            os.system('cls')
            print(f"{formato['negrito']}Você escolheu editar Wod{formato['padrao']}")
            funcoes.editar_wod()

        case 4:
            os.system('cls')
            print(f"{formato['negrito']}Você escolheu excluir Wod{formato['padrao']}")
            funcoes.excluir_wod()

        case 5:
            os.system('cls')
            print(f"{formato['negrito']}Você escolheu filtrar Wods{formato['padrao']}")
            resultado = funcoes.filtro()
            if resultado: funcoes.exibir(resultado)

        case 6:
            os.system('cls')
            print(f"{formato['negrito']}Você escolheu adicionar metas{formato['padrao']}")
            funcoes.adicionar_meta()

        case 7:
            os.system('cls')
            print(f"{formato['negrito']}Você escolheu ver metas{formato['padrao']}")
            funcoes.ver_meta()

        case 8:
            os.system('cls')
            print(f"{formato['negrito']}Você escolheu atualizar metas{formato['padrao']}")
            funcoes.atualizar_meta()

        case 9:
            os.system('cls')
            print(f"{formato['negrito']}Você escolheu receber uma sugestao de exercicios aleatorios{formato['padrao']}")
            funcoes.sugestao_aleatoria3()

        case 10:
            os.system('cls')
            print(f"{formato['negrito']}Você escolheu frase motivacionais{formato['padrao']}")
            funcoes.frase_motivacional()

        case 0:
            print(f"{formato['negrito']}Você escolheu encerrar o programa{formato['padrao']}")
            break

        case _: 
            print(f"{formato['negrito']}A opção digitada não se encontra no menu de opções{formato['padrao']}")
            
    input("Pressione enter para voltar para o menu\n")
    os.system('cls')
