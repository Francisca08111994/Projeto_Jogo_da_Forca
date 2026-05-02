# Testes
from jogo import verificar_letra

# 5 casos válidos (devem ser True)
def testes_validos():
    assert verificar_letra("python", "p", []) == True
    assert verificar_letra("python", "y", []) == True
    assert verificar_letra("python", "t", []) == True
    assert verificar_letra("python", "h", []) == True
    assert verificar_letra("python", "o", []) == True

# 5 casos inválidos (devem ser False)
def testes_invalidos():
    assert verificar_letra("python", "a", []) == False
    assert verificar_letra("python", "b", []) == False
    assert verificar_letra("python", "c", []) == False
    assert verificar_letra("python", "d", []) == False
    assert verificar_letra("python", "z", []) == False


if __name__ == "__main__":
    testes_validos()
    testes_invalidos()
    print("Todos os testes passaram!")

