"""Módulo de estatísticas"""
import utils,emprestimos, livros, leitores


def menu_estatisticas():
    """Menu de estatísticas"""
    while True:
        utils.mostrar_menu("Estatísticas",["Voltar","Empréstimos por mês","Empréstimos por leitor","Empréstimos por livro"])
        op=utils.le_numero("Opção:")
        if op==1:
            break
        if op==2:
            emprestimos_mes()
        if op==3:
            emprestimos_leitor()
        if op==4:
            emprestimos_livro()

def emprestimos_mes():
    """Calcula e mostra o nº de empréstimos por mês"""
    conta_mes=[]
    for mes in range(12):
        conta_mes.append(0)
    for emprestimo in emprestimos.emprestimos:
        mes=emprestimo['data_emprestimo'].month-1
        conta_mes[mes] += 1
    for mes in range(12):
        print(f"Mês {mes+1} - empréstimos: {conta_mes[mes]}")
    maior=max(conta_mes)
    print(f"Maior número de empréstimos de um mês: {maior}")

def emprestimos_leitor():
    """Empréstimos por leitor"""
    emp_leitores=[]
    conta=[]
    for emprestimo in emprestimos.emprestimos:
        if emprestimo['leitor'] not in emp_leitores:
            emp_leitores.append(emprestimo['leitor'])
            conta.append(1)
        else:
            pos=emp_leitores.index(emprestimo['leitor'])
            conta[pos]+=1
    for i,leitor in enumerate(emp_leitores):
        print(f"Leitor {leitor['nome']} - nº de empréstimos {conta[i]}")

def emprestimos_livro():
    """Empréstimos por livro"""
    livros_ordenados=sorted(livros.livros, key=lambda x: x['nr_emprestimos'],reverse=True)
    for livro in livros_ordenados:
        print(f"Livro: {livro['nome']} Empréstimos: {livro['nr_emprestimos']}")
