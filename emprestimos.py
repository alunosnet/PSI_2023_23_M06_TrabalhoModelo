"""Módulo para gerir empréstimos/devolução"""
import leitores, livros, utils
import datetime

emprestimos=[]

def menu_emprestimos():
    while True:
        utils.mostrar_menu("Menu empréstimos",["Emprestar","Devolver","Livros emprestados","Leitores com livros","Voltar"])
        op=utils.le_numero("Opção: ")
        if op==5:
            break
        if op==1:
            emprestar()
        if op==2:
            devolver()
        if op==3:
            livros_emprestados()
        if op==4:
            leitores_com_livros()

def emprestar():
    """Função para registar o empréstimo de um livro"""
    #id do livro a emprestar
    id_livro=utils.le_numero("Id do livro a emprestar:")
    livro=livros.get_livro(id_livro)
    while livro is None:
        id_livro=utils.le_numero("O id indicado não existe.\nId do livro a emprestar:")
        livro=livros.get_livro(id_livro)
    #testar se o livro está disponível
    if livro['estado']!='disponível':
        print("O livro não se encontra disponível.")
        return
    #id do leitor
    id_leitor=utils.le_numero("Id do leitor:")
    leitor=leitores.get_leitor(id_leitor)
    if leitor is None:
        print("Esse leitor não existe.")
        return
    #Mostrar o livro e o leitor
    print(f"Empréstimo do livro {livro['nome']} ao leitor {leitor['nome']}")
    #guardar a data atual do computador
    data_emprestimo = datetime.datetime.now()
    #calcular a data de entrega do livro (somar 7 dias à data atual)
    data_devolucao = data_emprestimo + datetime.timedelta(days=7)
    data_formatada=data_devolucao.strftime("%d/%m/%Y")
    print(f"Tem de devolver o livro até {data_formatada}")
    #guardar na lista do empréstimos
    novo = {
        'livro': livro,
        'leitor': leitor,
        'data_emprestimo': data_emprestimo,
        'data_devolucao': data_devolucao,
        'estado': 'emprestado'
    }
    #alterar o estado do livro para emprestado
    livro['estado']='emprestado'
    #guardar o leitor no livro emprestado
    livro['leitor']=leitor
    livro['nr_emprestimos'] += 1
    emprestimos.append(novo)

def devolver():
    id_livro=utils.le_numero("Id do livro a devovler:")
    livro=livros.get_livro(id_livro)
    if livro is None:
        print("Esse livro não existe")
        return
    if livro['estado']!='emprestado':
        print("Esse livro não se encontra emprestado")
        return
    for emprestimo in emprestimos:
        if emprestimo['livro'] == livro and emprestimo['estado']=='emprestado':
            if emprestimo['data_devolucao']>datetime.datetime.now():
                print("Livro devolvido dentro do prazo.")
            else:
                print("Livro devolvido fora do prazo.")
            #alterar o estado do empréstimo
            emprestimo['estado']='concluído'
            #alterar o estado do livro
            livro['estado']='disponível'
            #retirar o leitor do livro
            livro['leitor']=None
            return
    print("Os dados da aplicação estão corrompidos. CHAME A ASSISTÊNCIA.")

def livros_emprestados():
    for livro in livros.livros:
        if livro['estado']=='emprestado':
            print(livro)

def leitores_com_livros():
    for livro in livros.livros:
        if livro['estado']=='emprestado':
            print(livro['leitor'])
