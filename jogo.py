

papelpetrtatesolra /
You’ve activated the file finder. Start typing to filter the file list. Use ↑ and ↓ to navigate, enter to view files, esc to exit.
from  random  import randint
from time import *
intens = ['pedra', 'papel','Tesolra']
comp = randint(0,2)
joga = 0
compu = 0
while True:
    print('''Suas opeções:
    [0] Pedra
    [1] Papel
    [2] Tesolra ''')
    print()
    jogador = int(input("Escolha sua jogada? "))
    if jogador > 2:
        print("Escolha invalida Numeros valifos  0, 1 ,2")
    else:

        print("JO")
        sleep(1)
        print("KEE...")
        sleep(2)
        print("PO!!!")
        sleep(1)
        print()
        print(f"O computador escolheu: {intens[comp]}")
        print(f"O jogador  jogou: {intens[jogador]}")
        print()


        if comp == 0: #computador jogou pedra
            if  jogador == 0:
                print("EMPATE!")
            
            elif jogador == 1:
                print("JOGADOR VENCE!")
                joga += 1
            
            elif jogador == 2:
                print("COMPUTADOR VENCE!")
                compu += 1
                
            else:
                print("JOGADA INVALIDA!")
            

        elif comp == 1: # computador jogoou Papel
            if  jogador == 0:
                print("COMPUTADOR VENCE!")
                compu += 1
            
            elif jogador == 1:
                print("EMPATE!")
            
            elif jogador == 2:
                print("JOGADOR VENCE!")
                joga += 1
                
            else:
                print("JOGADA INVALIDA!")

        elif comp == 2: # computador jogou Tesolra
            if  jogador == 0:
                print("JOGADOR VENCE!")
                joga += 1
            
            elif jogador == 1:
                print("COMPUTADOR VENCE!")
                compu += 1
            
            elif jogador == 2:
                print("EMPATE!")
                
            else:
                print("JOGADA INVALIDA!")
        print()
        print(" Jogador Vitorias: ",joga)
        print(" Computador Vitorias: ",compu)
        print()
        if joga ==3:
            print("O  FIM DE JOGO!!")
            print("O jogardar vecenu vitorias: ",joga)
            print("O computador foi derrotado vitorias: ",compu)
            break
        if compu ==3:
            print("O  FIM DE JOGO!!")
            print("O computador vecenu vitorias: ",compu)
            print("O jogador foi derrotado vitorias: ",joga)
            break


