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
        utils.mostrar_menu("Menu Livros",["Adicionar","Listar","Editar","Apagar","Pesquisar","Voltar"])
        op = utils.le_numero("Opção: ")
        if op==6:
            break
        if op==1:
            adicionar()
        if op==2:
            listar()
        if op==3:
            editar()
        if op==4:
            apagar()
        if op==5:
            pesquisar()

def pesquisar():
    """Pesquisa livros por nome ou autor"""
    utils.mostrar_menu("Escolha o campo de pesquisa",["Nome","Autor"])
    op=utils.le_numero("Opção:")
    if op==1:
        campo="nome"
    else:
        campo="autor"
    pesquisa=utils.le_texto(f"{campo} a pesquisar:")
    for livro in livros:
        if pesquisa.lower() in livro[campo].lower():
            print(livro)

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
    id=int(input("Qual o id do livro a editar?"))
    livro=get_livro(id)
    if livro is None:
        print("Não existe nenhum livro com o id indicado.")
        return
    #Percorrer os campos do dicionário e permitir editar os dados
    campos_nao_editar=["id","nr_emprestimos","leitor"]
    for campo,valor in livro.items():
        if campo in campos_nao_editar:
            continue
        print(valor)
        novo=utils.le_texto(f"Novo {campo} ou enter para não alterar:")
        if novo!="":
            livro[campo]=novo

def apagar():
    """Remove um livro da lista"""
    id=utils.le_numero("Qual o id do livro a apagar?")
    livro=get_livro(id)
    if livro is None:
        print("Não existe nenhum livro com o id indicado.")
        return
    if livro['estado']!='disponível':
        print("Só pode remover livros cujo estado é disponível")
        return
    op=utils.le_texto(f"Pretende remover o livro {livro['nome']}?")
    if op in ['s','S','sim','SIM','yes','Sim','y']:
        livros.remove(livro)
        print(f"Livro removido com sucesso. Tem {len(livros)} livros.")