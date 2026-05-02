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
# Tratamento de erros
        try:
            tentativa = input("Escolhe uma letra: ").lower()

            if len(tentativa) != 1 or not tentativa.isalpha():
               raise ValueError("Introduz apenas uma letra válida!")

        except ValueError as e:
            print("⚠ Erro:", e)
            continue


        if tentativa in palavra:
            letras_acertadas.append(tentativa)
            print("Correto!")
        else:
            tentativas -= 1
            print(f"Errado! Tentativas restantes: {tentativas}")

    if tentativas == 0:
        print("Perdeu! A palavra era:", palavra)

def verificar_letra(palavra, letra, letras_acertadas):
    return letra in palavra

