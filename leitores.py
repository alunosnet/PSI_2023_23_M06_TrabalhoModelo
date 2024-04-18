"""
Módulo Leitores
"""
import utils

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
            pass
        if op==4:
            pass
    
def adicionar():
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