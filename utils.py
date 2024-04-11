def le_numero(titulo):
    """função que lê e devolve um inteiro do utilizador"""
    temp=input(titulo)
    while not temp.isnumeric():
        temp=input(titulo)
    return int(temp)

def le_texto(titulo,minimo=None):
    """função para ler um texto com um número minimo de letras"""
    temp=input(titulo)
    while minimo is not None and len(temp)<minimo:
        temp=input(titulo)
    return temp

def le_email(titulo):
    """Função lê, valida e devolve um endereço de email"""
    while True:
        email=le_texto(titulo)
        tem_arroba=False
        for c in email:
            if c=="@":
                tem_arroba=True
            if tem_arroba:
                if c==".":
                    return email

def mostrar_menu(titulo,opcoes):
    """função para mostrar um menu
    p.ex.: mostrar_menu("Menu Principal",["Livros","Leitores",...])"""
    print("="*40)
    print(titulo)
    print("="*40)
    for i in range(len(opcoes)):
        print(f"{i+1} - {opcoes[i]}")
    print("="*40)