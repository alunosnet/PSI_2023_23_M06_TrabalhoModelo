#função que lê um inteiro do utilizador
def le_numero(titulo):
    temp=input(titulo)
    while not temp.isnumeric():
        temp=input(titulo)
    return int(temp)

#função para ler um texto com um número minimo de letras
def le_texto(titulo,minimo):
    temp=input(titulo)
    while len(temp)<minimo:
        temp=input(titulo)
    return temp

#função para mostrar um menu
#mostrar_menu("Menu Principal",["Livros","Leitores",...])
def mostrar_menu(titulo,opcoes):
    print("="*40)
    print(titulo)
    print("="*40)
    for i in range(len(opcoes)):
        print(f"{i+1} - {opcoes[i]}")
    print("="*40)