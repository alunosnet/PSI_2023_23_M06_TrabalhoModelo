"""
Módulo de livros
"""
import utils

livros=[]

exemplo_livros=[
    {'id':1,'nome':'Livro 1','autor':'Autor 1','ano':2000,'editora':'editora 1','estado':'disponível','leitor':None,'nr_emprestimos':0},
    {'id':2,'nome':'Livro 2','autor':'Autor 1','ano':2000,'editora':'editora 1','estado':'disponível','leitor':None,'nr_emprestimos':0},
    {'id':3,'nome':'Livro 3','autor':'Autor 2','ano':2000,'editora':'editora 2','estado':'disponível','leitor':None,'nr_emprestimos':0},
]

def configurar():
    livros.extend(exemplo_livros)

def menu_livros():
    while True:
        utils.mostrar_menu("Menu Livros",["Adicionar","Listar","Editar","Apagar","Voltar"])
        op = utils.le_numero("Opção: ")
        if op==5:
            break
        if op==1:
            adicionar()
        if op==2:
            listar()
        if op==3:
            pass
        if op==4:
            pass

def adicionar():
    #nome
    nome=utils.le_texto("Nome do livro:",3)
    #autor
    autor=utils.le_texto("Nome do autor:",3)
    #ano
    ano=utils.le_numero("Ano de edição: ")
    #editora
    editora=utils.le_texto("Editora: ",3)
    #adicionar à lista dos livros
    id=1
    if len(livros)>0:
        id=livros[len(livros)-1]['id']+1
    novo = {
        'id':id,
        'nome':nome,
        'autor':autor,
        'ano':ano,
        'editora':editora,
        'estado':'disponível',
        'leitor':None,
        'nr_emprestimos':0
    }
    livros.append(novo)
    print(f"Livro adicionado com sucesso. Tem {len(livros)} livros.")

def listar():
    print("#"*40)
    print("Lista de livros")
    print("#"*40)
    for livro in livros:
        print(f"Id: {livro['id']} Nome: {livro['nome']} Autor: {livro['autor']} Estado: {livro['estado']}")
        print("-"*40)