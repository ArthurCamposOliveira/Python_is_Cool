import random
from time import sleep
print("\033[1;36m---" * 10, end=" ")
print("\033[1;33mJOKENPO", end=" ")
print("\033[1;36m---" * 10)
print("\033[1;36mVamos jogar JOKENPO")
print("Estou escolhendo entre \033[1;31mPapel\033[m, \033[1;33mTesoura\033[m e \033[1;35mPedra\033[m...")
sleep(3)
print("\033[1;36mPronto já escolhi")
j = str(input("\033[1;mAgora é sua vez de escolher:")).strip().lower()
lista = ["pedra", "papel", "tesoura"]
e = random.choice(lista)
print("JO")
sleep(1)
print("KEM")
sleep(1)
print("PO")
print("")
if j == "papel":
    if e == "tesoura":
        print("Eu ganhei, eu escolhi \033[1;33mTesoura\033[m e \033[1;33mTesoura\033[m ganha de \033[1;35mPapel")
        print("\033[1;31mMais sorte da proxima vez !!!")
    elif e == "pedra":
        print("Você ganhou eu escolhi \033[1;35mPedra\033[m e \033[1;31mPapel\033[m ganha de \033[1;35mPedra")
        print("\033[1;34mParabens !!!")
    else:
        print("\033[1;37mEmpatamos eu também escolhi Papel")
elif j == "pedra":
    if e == "tesoura":
        print("Você ganhou eu escolhi \033[1;33mTesoura\033[m e \033[1;33mTesoura\033[m perde para \033[1;35mPedra")
        print("\033[1;34mParabens !!!")
    elif e == "pedra":
        print("\033[1;37mEmpatamos eu também escolhi Pedra")
    else:
        print("Eu ganhei eu escolhi \033[1;31mPapel\033[m e \033[1;31mPapel\033[m ganha de \033[1;35mPedra")
        print("\033[1;31mMais sorte na proxima vez !!!")
elif j == "tesoura":
    if e == "tesoura":
        print("\033[1;37mEmpatamos eu também escolhi Tesoura")
    elif e == "pedra":
        print("Eu ganhei eu escolhi \033[1;35mPedra\033[m e \033[1;35mPedra\033[m ganha de \033[1;33mTesoura.")
        print("\033[1;31mMais sorte na proxima.")
    else:
        print("Você ganhou eu escolhi \033[1;31mPapel\033[m e \033[1;33mTesoura\033[m ganha de \033[1;31mPapel.")
        print("\033[1;34mParabéns !!!")
else:
    print("\033[1;31m"
          "Por favor escolha entre Tesoura, Papel e Pedra apenas.")
