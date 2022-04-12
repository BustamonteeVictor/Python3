import random

def jogar(): #faz ligação com a pasta jogos 

    print("*********************************") #Dando as boas vindas ao usuario 
    print("Bem vindo ao jogo de Adivinhação!") #Dando as boas vindas ao usuario
    print("*********************************") #Dando as boas vindas ao usuario

    numero_secreto = random.randrange(1,101) # Gerado um numero aleatorio de 1 a 100
    total_de_tentativas = 0 # tentativa inicia em 0 pois o usuario digita a quantidade
    pontos = 1000 # pontos iniciais para o usuario

    print("Qual nível de dificuldade?")# Aparece na tela do usuario para ele digitar o nivel
    print("(1) Fácil (2) Médio (3) Difícil")# o usuario vai escolher o nivel de dificuldade

    nivel = int(input("Defina o nível: ")) # aqui o usuario digita o nivel 1,2,3

    if(nivel == 1):# se o usurio digitar um entra aqui 
        total_de_tentativas = 20 # e ja aparece as 20 tentativas para ele iniciar
    elif(nivel == 2): #se o usurio digitar dois entra aqui
        total_de_tentativas = 10 # e ja aparece as 10 tentativas para ele iniciar
    else: #se o usurio digitar Tres entra aqui
        total_de_tentativas = 5 # e ja aparece as 5 tentativas para ele iniciar

    for rodada in range(1, total_de_tentativas + 1): # toda vez que o usuario fizer uma tentativa aqui ira adicionar mais uma ate chegar no fim das tentativa dele
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))# aqui vai mostrar o tanto de tantativas que resta

        chute_str = input("Digite um número entre 1 e 100: ") # aqui o usuario vai digitar o numero para ele jogar , numero de 1 a 100
        print("Você digitou " , chute_str)# vai mostrar para ele o numero que ele digitou
        chute = int(chute_str)# esta vai converter o numero para inteiro

        if(chute < 1 or chute > 100):# vai conferir para ver se o numero esta dentro de 1 a 100
            print("Você deve digitar um número entre 1 e 100!") #caso nao tiver isso ira aparecer vai o usuario
            continue #caso esteja tudo certo, vai continuar

        acertou = chute == numero_secreto # aqui ele vai fazer a conferencia para dar a dica ao usuario
        maior   = chute > numero_secreto # aqui ele vai fazer a conferencia para dar a dica ao usuario
        menor   = chute < numero_secreto # aqui ele vai fazer a conferencia para dar a dica ao usuario

        if(acertou): # caso o usuario acerte 
            print("Você acertou e fez {} pontos!".format(pontos)) # vai aparecer que ele acertou e vai mostrar os pontos que ele fez
            break # e para o programa aqui 
        else:
            if(maior): # caso o numero foi maior vai avisalo 
                print("Você errou! O seu chute foi maior do que o número secreto.")# mandando essa mensagem para ajuda-lo
            elif(menor): # caso o numero for menor ira avisar ele 
                print("Você errou! O seu chute foi menor do que o número secreto.")# mandando essa mensagem para ajuda-lo 
            pontos_perdidos = abs(numero_secreto - chute) # aqui ele esta fazendo a soma do numero dos pontos
            pontos = pontos - pontos_perdidos# aqui ele vai subtrair os pontos que ele perdeu durante as tentativas 

    print("Fim do jogo")# essa menagem vai aparecer caso ele acerte ou caso as tentativas dele for encerradas 

#PLANOS FUTUROS ESSA PARTE ABAIXO

if(__name__ == "__main__"): # isso esta indicando que o programa inicia aqui
    jogar()# essa parte é lincada com outra pagina para fazer com que o usuario escolha qual jogo quer jogar
            
