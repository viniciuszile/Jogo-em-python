import random #biblioteca que traz um numero aleatorio
cont = 0 #contador 
numero = int ((random.randint(1,100)))#intervalo de numeros que define o valor minino e valor maximo que a biblioteca informara


#começo do programa/tutotial
print("-"*79)
print ("|     Seja bem vindo!                                                         |")
print ("|     Neste jogo você deverá descobrir o número secreto entre 0 e 100.        |")
print ("|     O número de tentativas são ilimitadas, boa sorte!                       |")
print("-"*79)
print ("")
print ("")
print ("-=-"*34)
print ("Deseja jogar nosso jogo?")
começo = str (input("Pressione 's' para entrar e para sair pressione qualquer outra tecla:"))


#estrutura de repitiçao do programa 
while começo == "s" or começo == "S" or começo == "sim" or começo == "SIM":    
    print ("O jogo já começou!")

    while True: #verifica se o usario informou um caractere invalido
        
        cont = cont + 1
        
        while True:#loping que verifica se o usario informou um caractere invalido
            print ("-="*34)
            escolha = str (input("Chute um número entre 0 e 100 : "))
            
            if escolha.isnumeric() :#verifica se o usario informou um caractere valido
                break
            else:
                print ("=-"*34)#erro exibido caso o usario informe um caractere invalido
                print ("|                            ErRor!!!                                           |")
                print ("|     Você informou um caractere invalido. Por favor, Tente novamente.          |")
                print ("|     Informe apenas números positivos e inteiros entre 0 e 100.                |")
                print ("=-"*34)

        
        t = int(escolha)#transforma a variavel escolha de str para int 
        
        if t < numero:#verifica se o numero do usario é mais baixo ou mais alto do que o numero secreto
            print ("Chutou baixo. Tente Novamente")
                

        if t > numero:#verifica se o numero do usario é mais baixo ou mais alto do que o numero secreto
            print("Chutou alto. Tente Novamente")

        if t == numero:#mensagem exibida caso o usario acerto o numero secreto
            print ("-="*24)
            print ("{    Uau, voçê conseguiu!                        }")    
            print ("{    Número de tentativas :",cont,("                   }"))
            print ("{    O número secreto corresponde ao número:",numero,(" }"))
            print ("=-"*24)
            break
    
    
    começo = str (input("Deseja jogar novamente? Pressione 's' para sim e para sair pressione qualquer outra tecla:"))#local onde o usario informa se ele deseja jogar o jogo novamente ou deseja sair do programa 
    numero = int ((random.randint(1,100)))#local onde o programa gera um novo numero aleatorio caso o usario deseje jogar novamente 
    cont = cont - cont#local onde o contador é zerado caso o usario deseje jogar novamente

#mensagem exibida caso o usario nao deseje jogar(caso ele precionar uma tecla diferente de 's' ou "S")
if começo != "s":
    print ("-=-"*34)
    print ("Obrigado por entrar, volte sempre!")    