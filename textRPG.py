##version 1.2
import time
while True:
    print('\nVocê acordou em um porão misterioso, você não sabe como chegou ali.')
    print('Após despertar você vê num canto uma pá, uma tocha e uma espada.')
    pergunta = input('Qual devo pegar? '.lower().strip())
    time.sleep(3)
    if pergunta == 'pá':
        print('Você pegou a pá e está pronto para cavar.')
    elif pergunta == 'tocha':
        print('Você pegou a tocha e está pronto para iluminar o caminho.')
    elif pergunta == 'espada':
        print('Você pegou a espada e está pronto para lutar.')
    else:
        print('Opção inválida, por favor escolha entre pá, tocha ou espada.')
        break
    print('\nVocê decide explorar o porão e encontra uma porta de madeira trancada.')
    pergunta2 = input('O que você faz? (usar pá, usar tocha, usar espada) '.lower().strip())
    time.sleep(3)
    if pergunta2 == 'usar pá':
        print('Você usa a pá para quebrar a porta, voce consegue abri-la mas vê um corrdor grande. Sua aventura continua...')
    elif pergunta2 == 'usar tocha':
        print('Você usa a tocha para queimar a porta, você vê um corredor escuro e decide seguir por ele. Sua aventura continua...')
    elif pergunta2 == 'usar espada':
        print('Você usa a espada para quebrar a porta, você consegue e vê um corredor grande. Sua aventura continua...')
    else:        print('Opção inválida, por favor escolha entre usar pá, usar tocha ou usar espada.')
    break
    print('\nEnquanto você caminha pelo corredor, você ve uma gigantesca aranha e voces entraram em combate.')
    pergunta3 = input('O que você faz? (usar pá, usar tocha, usar espada) '.lower().strip())
    if pergunta3 == 'usar pá':
        print('Você usa a pá para atacar a aranha, mas a pá quebra. A aranha ataca você e você perde a luta. Fim de jogo.')
        break
    elif pergunta3 == 'usar tocha':
        print('Você usa a tocha para atacar a aranha, a aranha queima lentamente e morre. Você continua sua aventura...')
    elif pergunta3 == 'usar espada':
        print('Você usa a espada para atacar a aranha, a aranha é cortada em pedaços e morre. Você continua sua aventura...')
    else:        print('Opção inválida, por favor escolha entre usar pá, usar tocha ou usar espada.')
    break
    print('\nApós derrotar a aranha, você encontra uma escada que leva para o próximo andar do porão.')
    pergunta4 = input('Você sobe a escada? (sim ou não) '.lower().strip())
    time.sleep(3)   
    if pergunta4 == 'sim':
        print('Você sobe a escada e encontra um poderoso dragao, vermelho e amendrontador.' \
        'suas escamas brilham e seu bafo fede a morte e destruição. Você entra em combate com o dragão.')
        pergunta5 = input('O que você faz? (usar tocha, usar espada) '.lower().strip())
        if pergunta5 == 'usar tocha':
            print('Você usa a tocha para atacar o dragão, mas o dragão é resistente ao fogo e você perde a luta. Fim de jogo.')
            break
        elif pergunta5 == 'usar espada':
            print('Você usa a espada para atacar o dragão, o dragão é cortado em pedaços e morre. Você continua sua aventura...')
        else:        print('Opção inválida, por favor escolha entre usar tocha ou usar espada.')
        break
    elif pergunta4 == 'não':
        print('Você decide não subir a escada e continua explorando o porão, mas acaba se perdendo e morre de fome. Fim de jogo.')
    else:        print('Opção inválida, por favor escolha entre sim ou não.')
    time.sleep(3)
    print('\nvocê encontra um bau cheio de riquezas e consegue sair do porão.' \
    'fim de jogo. Deseja jogar novamente? (sim ou não) '.lower().strip())
    jogar_novamente = input()
    if jogar_novamente == 'sim':
        continue
    elif jogar_novamente == 'não':
        print('Obrigado por jogar! Até a próxima!')
        break
    else:
        print('Opção inválida, por favor escolha entre sim ou não.')
        # solicita novamente ao jogador em caso de resposta inválida
        continue