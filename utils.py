def le_numero(titulo):
    """função que lê e devolve um inteiro do utilizador"""
    temp=input(titulo)
    while not temp.isnumeric():
        temp=input(titulo)
    return int(temp)

def le_texto(titulo,minimo):
    """função para ler um texto com um número minimo de letras"""
    temp=input(titulo)
    while len(temp)<minimo:
        temp=input(titulo)
    return temp

def mostrar_menu(titulo,opcoes):
    """função para mostrar um menu
    p.ex.: mostrar_menu("Menu Principal",["Livros","Leitores",...])"""
    print("="*40)
    print(titulo)
    print("="*40)
    for i in range(len(opcoes)):
        print(f"{i+1} - {opcoes[i]}")
    print("="*40)