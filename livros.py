"""
Módulo de livros
"""
import utils

#lista dos livros
livros=[]

#lista de livros de exemplo
exemplo_livros=[
    {'id':1,'nome':'Livro 1','autor':'Autor 1','ano':2000,'editora':'editora 1','estado':'disponível','leitor':None,'nr_emprestimos':0},
    {'id':2,'nome':'Livro 2','autor':'Autor 1','ano':2000,'editora':'editora 1','estado':'disponível','leitor':None,'nr_emprestimos':0},
    {'id':3,'nome':'Livro 3','autor':'Autor 2','ano':2000,'editora':'editora 2','estado':'disponível','leitor':None,'nr_emprestimos':0},
]

def configurar():
    """Adiciona livros de exemplo"""
    
    livros.extend(exemplo_livros)

def menu_livros():
    """Menu dos livros"""
    
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
    """Adiciona um livro novo à lista de livros"""
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
    """Lista os livros todos da lista"""
    print("#"*80)
    print("Lista de livros")
    print("#"*80)
    for livro in livros:
        print(f"Id: {livro['id']} Nome: {livro['nome']} Autor: {livro['autor']} Estado: {livro['estado']}")
        print("-"*80)

def get_livro(id):
    """Função que pesquisa o dicionário com o id fornecido e devolve o livro ou None"""
    for livro in livros:
        if livro['id']==id:
            return livro
    return None

def editar():
    """Edita os dados de um livro"""
    pass

def apagar():
    """Remove um livro da lista"""
    pass