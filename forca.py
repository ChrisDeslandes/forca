## Exercícios com Strings e Arquivos

## Jogo da Forca - Você perde no 7º erro. Palavra escolhida aleatoriamente de um arquivo contendo palavras. 

import random
from colorama import init, Fore


init()


def getSeparador():
    return "  -------------------------------------------------------------------------------------------------------------------------"

def getAlfabeto():
    return "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def entradaDeDados(letrasDisponiveis):

    letra = ""

    while True:
            letra = input("\n  Digite uma letra (sem acentuação): ").upper()
            try:
                if len(letra) != 1: raise Exception()
                if not letra in getAlfabeto(): raise Exception()
                if not letra in letrasDisponiveis:
                    print("\n  Você já escolheu esta letra, por favor escolha outra!")
                    continue
                break
            except: print("\n  Entrada inválida!")

    return letra



def jogo(palavras):
    
    letrasDisponiveis = getAlfabeto()
    erros = ""
    palavra = random.choice(palavras).upper()
    palavraEscondida = "_ " * len(palavra)

    while True:
        print("\n  Palavra a ser descoberta: " + Fore.CYAN + palavraEscondida + Fore.RESET + "\n")
        print("  Erros = " + Fore.RED + str(len(erros)) + Fore.RESET + " ==> " + Fore.RED + " - ".join(erros) + Fore.RESET + "\n")
        print("  Letras disponíveis: " + Fore.GREEN + " - ".join(letrasDisponiveis) + Fore.RESET)
        
        letra = entradaDeDados(letrasDisponiveis)

        print("\n" + getSeparador())

        letrasDisponiveis = letrasDisponiveis.replace(letra, "")

        if letra in palavra:
            for i, lt in enumerate(palavra):
                if lt == letra:
                    palavraEscondida = palavraEscondida[:2 * i] + lt + palavraEscondida[2 * i + 1:]
        else:
            erros += letra

        if fimDoJogo(palavra, palavraEscondida, len(erros)): break



def fimDoJogo(palavra, palavraEscondida, numErros):

    if numErros == 7:
        print("\n  Você foi enforcado!!! =(\n  Tente novamente!\n\n  A palavra era: " + Fore.CYAN + " ".join(palavra) + Fore.RESET)
        return True

    if not "_" in palavraEscondida:
        print("\n  Parabéns!!! =D\n  Você descobriu a palavra!\n\n  A palavra era: " + Fore.CYAN + palavraEscondida + Fore.RESET)
        return True

    return False



def sair():

    jogar = input("\n  Deseja jogar novamente? (s para sim) ").lower()
    
    if jogar in ["s", "sim"]:
        print("\n" + getSeparador())
        return False

    return True



filePalavras = open("./palavras.txt", "r")
palavras = filePalavras.read().split(",")
filePalavras.close()

while True:

    print(getSeparador())
    print("\n  Bem-vindo ao Jogo da Forca! Lembre-se, você tem direito a 6 erros!\n")
    print(getSeparador())

    jogo(palavras)

    print("\n" + getSeparador())

    if sair():
        break
