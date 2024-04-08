"""
Trabalho Modelo - Módulo 6
------------------------------
Um programa para ajudar a gerir os livros e empréstimos de um biblioteca
Requisitos:
    - Gestão livros (CRUD)
    - Gestão leitores (CRUD)
    - Empréstimos/devoluções
    - Estatísticas (top livro, top mês, top leitores)
"""
import utils, livros

#em modo debug vamos fornecer leitores e livros de exemplo
DEBUG=True

def menu_principal():
    while True:
        utils.mostrar_menu("Menu Principal",["Livros","Leitores","Empréstimos e devoluções","Estatísticas","Sair"])
        op = utils.le_numero("Opção: ")
        if op==5:
            break
        if op==1:
            livros.menu_livros()
        if op==2:
            pass
        if op==3:
            pass
        if op==4:
            pass

def main():
    if DEBUG:
        livros.configurar()
    menu_principal()

if __name__=='__main__':
    main()