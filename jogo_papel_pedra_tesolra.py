from  random  import randint
from time import *
intens = ['pedra', 'pepel','Tesolra']
comp = randint(0,2)

print('''Suas opeções:
[0] Pedra
[1] Papel
[2] Tesolra ''')
print()
jogador = int(input("Escolha sua jogada? "))
print("JO")
sleep(1)
print("KEEE...")
sleep(2)
print("PO!!!")
sleep(1)
print()
print(f"O computador escolheu: {intens[comp]}")
print(f"O jogador  jogou: {intens[jogador]}")
#Mudar para proximo arquivo
