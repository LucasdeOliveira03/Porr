import random

def load_phrase(counter):
    phrase = [
        f"Nicolas deu mole {counter} vezes. Tá treinando pra errar mais?",
        f"Mais um vacilo. Já são {counter}, vai querer bater recorde?",
        f"Putz, Nicolas. {counter} erros já. Bora dobrar esse número?",
        f"E lá vamos nós… Nicolas já se embolou {counter} vezes.",
        f"Tá difícil, hein? {counter} erros e contando",
        f"Mais um tropeço pro currículo! {counter} erros registrados.",
        f"Nicolas errou {counter} vezes. Será que chega nos {counter+5} hoje?",
        f"Nicolas errou {counter} vezes até hoje",
        f"Opa, mais um erro! Já são {counter}, bora tentar os {counter+2}?",
        f"De novo? O contador tá em {counter}",
        f"Nicolas rolou um 1 crítico... de novo. Já são {counter} falhas críticas acumuladas",
        f"O dado não tá ajudando hoje... {counter} falhas seguidas no teste de inteligência!",
        f"Nicolas tentou e... falhou! {counter} testes de perícia errados até agora.",
        f"Mais um erro crítico! O contador de falhas já chegou a {counter}.",
        f"O destino não sorriu pra você... Nicolas já errou {counter} vezes.",
        f"Se fosse um teste de acerto, era tudo 1 no dado. {counter} vacilos anotados!",
        f"{counter} erros acumulados. Já dá pra pedir uma consultoria em como não fazer.",
        f"Com {counter} erros, o cérebro pediu férias.",
        f"Já são {counter}. A lógica foi dar uma volta e não voltou mais.",
        f"{counter} falhas consecutivas. Conquista desbloqueada: Mestre do Vacilo.",
        f"Score: {counter} vacilos. Tá jogando no modo difícil da vida.",
        f"Subiu pra {counter}. Vai zerar o jogo do erro antes de aprender a jogar.",
        f"{counter} tentativas, nenhuma vitória. Isso virou experimento científico.",
        f"A cada erro, mais dados pro laboratório. Já são {counter} no total.",
        f"{counter} falhas catalogadas. O método científico tá chorando.",
        f"Acumulando erros desde sempre. Já são {counter} no placar.",
        f"De erro em erro, chegamos em {counter}. Uma verdadeira linha do tempo do caos.",
        f"{counter} episódios de pura vergonha. Essa série precisa de um reboot urgente.",
        f"Já são {counter} cenas de erro. E o Oscar vai para…",
        f"{counter} falhas. Isso aqui é roteiro de comédia ou drama existencial?",
        f"Contagem atual: {counter} erros. Líder do campeonato do vacilo.",
        f"{counter} no placar. Tá correndo atrás do próprio rabo com excelência.",
        f"Subindo na tabela com {counter} erros. É quase um recorde olímpico."
    ]

    i = random.randrange(0, len(phrase))

    return(phrase[i])