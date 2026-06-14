while True:
    print('\nVocê acordou em um porão misterioso, você não sabe como chegou ali.')
    print('Após despertar você vê num canto uma pá, uma tocha e uma espada.')
    pergunta = input('Qual devo pegar? '.lower().strip())
    if pergunta == 'pá':
        print('Você pegou a pá e está pronto para cavar.')
    elif pergunta == 'tocha':
        print('Você pegou a tocha e está pronto para iluminar o caminho.')
    elif pergunta == 'espada':
        print('Você pegou a espada e está pronto para lutar.')
    else:
        print('Opção inválida, por favor escolha entre pá, tocha ou espada.')
    print('\nVocê decide explorar o porão e encontra uma porta de madeira trancada.')
    pergunta2 = input('O que você faz? (usar pá, usar tocha, usar espada) '.lower().strip())
    if pergunta2 == 'usar pá':
        print('Você usa a pá para quebrar a porta, voce consegue abri-la mas vê um corrdor grande. Sua aventura continua...')
    elif pergunta2 == 'usar tocha':
        print('Você usa a tocha para queimar a porta, você vê um corredor escuro e decide seguir por ele. Sua aventura continua...')
    elif pergunta2 == 'usar espada':
        print('Você usa a espada para quebrar a porta, você consegue e vê um corredor grande. Sua aventura continua...')
    else:        print('Opção inválida, por favor escolha entre usar pá, usar tocha ou usar espada.')
    print('\nEnquanto você caminha pelo corredor, você ve uma gigantesca aranha e voces entraram em combate.')
    pergunta3 = input('O que você faz? (usar pá, usar tocha, usar espada) '.lower().strip())
    if pergunta3 == 'usar pá':
        print('Você usa a pá para atacar a aranha, mas a pá quebra. A aranha ataca você e você perde a luta. Fim de jogo.')
    elif pergunta3 == 'usar tocha':
        print('Você usa a tocha para atacar a aranha, a aranha queima lentamente e morre. Você continua sua aventura...')
    elif pergunta3 == 'usar espada':
        print('Você usa a espada para atacar a aranha, a aranha é cortada em pedaços e morre. Você continua sua aventura...')
    else:        print('Opção inválida, por favor escolha entre usar pá, usar tocha ou usar espada.')