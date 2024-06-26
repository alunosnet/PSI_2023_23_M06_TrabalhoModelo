"""
Módulo Leitores
"""
import utils, emprestimos

#lista de leitores
leitores=[]

#lista de leitores de exemplo
exemplo_leitores=[
    {'id':1,'nome':'joaquim','email':'joaquim@gmail.com'},
    {'id':2,'nome':'maria','email':'maria@gmail.com'}
]

def configurar():
    """Adiciona leitores de exemplo"""
    leitores.extend(exemplo_leitores)

def menu_leitores():
    """Menu de leitores"""
    while True:
        utils.mostrar_menu("Menu de Leitores",["Adicionar","Listar","Editar","Apagar","Voltar"])
        op=utils.le_numero("Opção: ")
        if op==5:
            break
        if op==1:
            adicionar()
        if op==2:
            listar()
        if op==3:
            editar()
        if op==4:
            apagar()
    
def adicionar():
    """Função para ler os dados de um leitor e adicionar à lista dos leitores"""
    nome=utils.le_texto("Nome:",3)
    email=utils.le_email("Email:")
    #adicionar à lista
    id=1
    if len(leitores)>0:
        id=leitores[len(leitores)-1]['id']+1
    novo={
        'id':id,
        'nome':nome,
        'email':email
    }
    leitores.append(novo)
    print(f"Leitor adicionado com sucesso. Tem {len(leitores)} leitores.")

def listar():
    """Mostra a lista de todos os leitores"""
    print("Lista de leitores")
    for leitor in leitores:
        print(f"Id: {leitor['id']} \tNome: {leitor['nome']} \tEmail:{leitor['email']}")

def get_leitor(id):
    """Devolve os dados de um leitor com base no id"""
    for leitor in leitores:
        if leitor['id']==id:
            return leitor
    return None

def editar():
    """Edita os dados de um leitor com base no id"""
    id_leitor=utils.le_numero("Id do leitor a editar:")
    leitor=get_leitor(id)
    if leitor is None:
        print("Não existe nenhum leitor com o id indicado.")
        return
        #Percorrer os campos do dicionário e permitir editar os dados
    campos_nao_editar=["id"]
    for campo,valor in leitor.items():
        if campo in campos_nao_editar:
            continue
        print(valor)
        novo=utils.le_texto(f"Novo {campo} ou enter para não alterar:")
        if novo!="":
            leitor[campo]=novo

def apagar():
    """Apaga um leitor com base no id"""
    id_leitor=utils.le_numero("Id do leitor a apagar:")
    leitor=get_leitor(id_leitor)
    if leitor is  None:
        print("Não existe nenhum leitor com o id indicado")
        return
    if leitor in emprestimos.leitores_com_livros():
        print("Leitor não pode ser removido uma vez que tem livros emprestados.")
        return
    op=utils.le_texto(f"Tem a certeza que pretende remover o leitor {leitor}")
    if op in ['s','S']:
        leitores.remove(leitor)
    print(f"Leitor removido com sucesso. Tem {len(leitores)} leitores.")