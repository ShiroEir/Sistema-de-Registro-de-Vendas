import tkinter
import tkinter.dialog
import tkinter.messagebox
import psycopg2

janela = tkinter.Tk()
janela.title("Sistema de Registro de Vendas")
janela.geometry("1400x450")
janela.resizable(False,False)

connection = psycopg2.connect(
    host='localhost',
    database='revendedor',
    user='postgres',
    password='admin7841'
)
cursor = connection.cursor()

def cadastrar():
    try:
        cursor.execute(f"INSERT INTO PRODUTO (codigo,nome,quantidade,preço_unitario) VALUES ('{EntryCodigo.get()}','{EntryNome.get()}','{EntryQuantidade.get()}','{EntryPreço.get()}');"),
        connection.commit()
    except:
        tkinter.messagebox.showerror(title="Erro de Cadastro",message="Ocorreu algum erro! Você colocou os dados corretos? Alguma caixa está vazia?")
def alterar():
    try:
        cursor.execute(f"UPDATE PRODUTO SET nome='{EntryNome.get()}',quantidade='{EntryQuantidade.get()}',preço_unitario='{EntryPreço.get()}' WHERE codigo='{EntryCodigo.get()}';"),
        connection.commit()
    except:
        tkinter.messagebox.showerror(title="Erro de Alteração",message="Ocorreu algum erro! Você colocou os dados corretos? Alguma caixa está vazia?")
def remover():
    try:
        cursor.execute(f"DELETE FROM PRODUTO WHERE codigo='{EntryCodigo.get()}';"),
        connection.commit()
    except:
        tkinter.messagebox.showerror(title="Erro de Remoção",message="Ocorreu algum erro! Você colocou os dados corretos? Alguma caixa está vazia?")
def consultar():
    try:
        ListboxLista.delete(0,tkinter.END)
        cursor.execute(f"SELECT * FROM PRODUTO;")
        connection.commit()
        registros = cursor.fetchall()
        for registro in registros:
            codigo = registro[0]
            nome = registro[1]
            quantidade = registro[2]
            preço = registro[3]
            ListboxLista.insert(tkinter.END,registro[0])
            ListboxLista.insert(tkinter.END,registro[1])
            ListboxLista.insert(tkinter.END,registro[2])
            ListboxLista.insert(tkinter.END,registro[3])
            ListboxLista.insert(tkinter.END,"")
    except:
        tkinter.messagebox.showerror(title="Erro de Consulta",message="Ocorreu algum erro! Tente novamente e preste atenção com as ações...")

LabelTitulo = tkinter.Label(
    janela,
    width=25,
    bg=("#FFF"),
    relief=("solid"),
    font=("Impact",32),
    text=("Operações")
)
LabelCodigo = tkinter.Label(
    janela,
    font=("Impact",20),
    text=("CÓDIGO")
)
LabelNome = tkinter.Label(
    janela,
    font=("Impact",20),
    text=("NOME")
)
LabelQuantidade = tkinter.Label(
    janela,
    font=("Impact",20),
    text=("QUANTIDADE")
)
LabelPreço = tkinter.Label(
    janela,
    font=("Impact",20),
    text=("PREÇO ÚNICO")
)
EntryCodigo = tkinter.Entry(
    janela,
    width=20,
    bg=("#FFF"),
    relief=("solid"),
    font=("Poppins",14)
)
EntryNome = tkinter.Entry(
    janela,
    width=20,
    bg=("#FFF"),
    relief=("solid"),
    font=("Poppins",14)
)
EntryQuantidade = tkinter.Entry(
    janela,
    width=20,
    bg=("#FFF"),
    relief=("solid"),
    font=("Poppins",14)
)
EntryPreço = tkinter.Entry(
    janela,
    width=20,
    bg=("#FFF"),
    relief=("solid"),
    font=("Poppins",14)
)
ButtonCadastro = tkinter.Button(
    janela,
    width=11,
    bg=("#000"),
    fg=("#FFF"),
    relief=("solid"),
    cursor=("hand2"),
    font=('Impact',15),
    text=("CADASTRAR"),
    command=lambda:cadastrar()
)
ButtonAlterar = tkinter.Button(
    janela,
    width=11,
    bg=("#000"),
    fg=("#FFF"),
    relief=("solid"),
    cursor=("hand2"),
    font=('Impact',15),
    text=("ALTERAR"),
    command=lambda:alterar()
)
ButtonRemover = tkinter.Button(
    janela,
    width=11,
    bg=("#000"),
    fg=("#FFF"),
    relief=("solid"),
    cursor=("hand2"),
    font=('Impact',15),
    text=("REMOVER"),
    command=lambda:remover()
)
ButtonConsultar = tkinter.Button(
    janela,
    width=11,
    bg=("#000"),
    fg=("#FFF"),
    relief=("solid"),
    cursor=("hand2"),
    font=('Impact',15),
    text=("CONSULTAR"),
    command=lambda:consultar()
)
ListboxLista = tkinter.Listbox(
    janela,
    width=66,
    height=12,
    bg=("#FFF"),
    relief=("solid"),
    font=("Impact",15)
)
ListboxLista.insert(tkinter.END,"SISTEMA DE REGISTRO DE VENDAS - LISTA COMPLETA")

LabelTitulo.place(x=40,y=20)
LabelCodigo.place(x=40,y=100)
LabelNome.place(x=40,y=160)
LabelQuantidade.place(x=40,y=220)
LabelPreço.place(x=40,y=280)
EntryCodigo.place(x=210,y=105)
EntryNome.place(x=210,y=165)
EntryQuantidade.place(x=210,y=225)
EntryPreço.place(x=210,y=285)
ButtonCadastro.place(x=40,y=360)
ButtonAlterar.place(x=180,y=360)
ButtonRemover.place(x=320,y=360)
ButtonConsultar.place(x=1205,y=360)
ListboxLista.place(x=600,y=20)

janela.mainloop()