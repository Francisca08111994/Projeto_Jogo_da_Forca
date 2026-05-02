# Jogo 
def jogar():
    palavra = "python"
    letras_acertadas = []
    tentativas = 6

    print("Bem-vindo ao Jogo da Forca!")

    while tentativas > 0:
        resultado = ""

        for letra in palavra:
            if letra in letras_acertadas:
                resultado += letra
            else:
                resultado += "_"

        print("\nPalavra:", resultado)

        if "_" not in resultado:
            print("Ganhou!")
            break

        tentativa = input("Escolhe uma letra: ")

        if tentativa in palavra:
            letras_acertadas.append(tentativa)
            print("Correto!")
        else:
            tentativas -= 1
            print(f"Errado! Tentativas restantes: {tentativas}")

    if tentativas == 0:
        print("Perdeu! A palavra era:", palavra)
