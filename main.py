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
    print("\n1-Adicionar wod\n2-Ver Wod\n3-Editar Wod\n4-Excluir Wod\n5-filtrar wod\n6-Adicionar metas\n7-Ver Metas\n8-Atualizar metas\n9-Sugestao de wod aleatorio\n10- Frases Motivacionais para treinar inspirado\n0- Para sair do programa")
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
            input("Pressione enter para voltar para o menu\n")

        case 2:
            os.system('cls')
            print(f"{formato['negrito']}Você escolheu ver wod\n{formato['padrao']}")
            funcoes.ver_wod()
            input("Pressione enter para voltar para o menu\n")

        case 3:
            os.system('cls')
            print(f"{formato['negrito']}Você escolheu editar Wod{formato['padrao']}")
            funcoes.editar_wod()
            input("Pressione enter para voltar para o menu\n")

        case 4:
            os.system('cls')
            print(f"{formato['negrito']}Você escolheu excluir Wod{formato['padrao']}")
            funcoes.excluir_wod()
            input("Pressione enter para voltar para o menu\n")

        case 5:
            os.system('cls')
            print(f"{formato['negrito']}Você escolheu filtrar Wods{formato['padrao']}")
            resultado = funcoes.filtro()
            if resultado: funcoes.exibir(resultado)
            input("Pressione enter para voltar para o menu\n")

        case 6:
            os.system('cls')
            print(f"{formato['negrito']}Você escolheu adicionar metas{formato['padrao']}")
            funcoes.adicionar_meta()
            input("Pressione enter para voltar para o menu\n")

        case 7:
            os.system('cls')
            print(f"{formato['negrito']}Você escolheu ver metas{formato['padrao']}")
            funcoes.ver_meta()
            input("Pressione enter para voltar para o menu\n")

        case 8:
            os.system('cls')
            print(f"{formato['negrito']}Você escolheu atualizar metas{formato['padrao']}")
            funcoes.atualizar_meta()
            input("Pressione enter para voltar para o menu\n")

        case 9:
            os.system('cls')
            print(f"{formato['negrito']}Você escolheu receber uma sugestao de exercicios aleatorios{formato['padrao']}")
            funcoes.sugestao_aleatoria3()
            input("Pressione enter para voltar para o menu\n")

        case 10:
            os.system('cls')
            print(f"{formato['negrito']}Você escolheu frase motivacionais{formato['padrao']}")
            funcoes.frase_motivacional()
            input("Pressione enter para voltar para o menu\n")

        case 0:
            print(f"{formato['negrito']}Você escolheu encerrar o programa{formato['padrao']}")
            break
        case _: 
            print(f"{formato['negrito']}A opção digitada não se encontra no menu de opções{formato['padrao']}")
            input("Pressione enter para voltar para o menu\n")
    
    os.system('cls')
