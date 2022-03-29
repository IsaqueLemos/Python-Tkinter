from tkinter import *
from tkinter.ttk import Combobox

def salvar():
    arquivo = open('dados.txt', 'a')
    dados = []
    
    nome = en_nome.get()
    dados.append(nome)
    c1 = all(char.isalpha() or char.isspace() for char in nome)
    if c1:
        lb_nome.configure(fg='limegreen')
    else:
        lb_nome.configure(fg='red')

    cpf = en_cpf.get()
    dados.append(f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}')
    c2 = len(cpf) == 11 and cpf.isdigit()
    if c2:
        lb_cpf.configure(fg='limegreen')
    else:
        lb_cpf.configure(fg='red')

    matricula = en_matricula.get()
    dados.append(matricula)
    c3 = len(matricula) < 20 and matricula.isdigit()
    if c3:
        lb_matricula.configure(fg='limegreen')
    else:
        lb_matricula.configure(fg='red')

    data = en_data.get()
    dados.append(f'{data[:2]}/{data[2:4]}/{data[4:8]}')
    dia = int(data[:2])
    mes = int(data[2:4])
    ano = int(data[4:8])
    c4 = len(data) == 8 and dia < 32 and mes < 13 and ano < 2023
    if c4:
        lb_data.configure(fg='limegreen')
    else:
        lb_data.configure(fg='red')

    if c1 and c2 and c3 and c4:
        arquivo.write('%'.join(dados))
        arquivo.write('\n')
        arquivo.close()
        janela.destroy()
    else:
        dados = []
        janela.bell()

def verificar():
    dados_cadastrado = cadastrados[tb.get()]
    dt_cpf.configure(text=f'CPF: {dados_cadastrado[0]}')
    dt_matricula.configure(text=f'Matrícula: {dados_cadastrado[1]}')
    dt_data.configure(text=f'Data de Nascimento: {dados_cadastrado[2]}')

### Interface dos Dados Salvos
def dados_salvos():
    global tb, cadastrados, dt_cpf, dt_data, dt_matricula

    ### Configuraçao da janela
    janela2 = Tk()
    janela2.title('Dados Salvos')
    janela2.geometry('500x400')
    janela2.resizable(False, False)
    janela2['bg'] = '#121212'

    ### Lendo e agrupando dados 
    arquivo = open('dados.txt', 'r')
    dados = arquivo.readlines()
    nomes = []
    cadastrados = {}
    for pessoa in dados:
        pessoa = pessoa.split('%')
        nomes.append(pessoa[0])
        cadastrados.setdefault(pessoa[0], pessoa[1:])
    arquivo.close()

    ### Lista de Dados na Interface
    Label(janela2, text='Dados:', font='arial 14', bg='#121212', fg='white').place(x=25, y=30)
    tb = Combobox(janela2, value=nomes, font='arial 14')
    tb.place(x=25, y=60)

    ### Botao Verificar
    Button(janela2, text='Verificar', bg='#00026B', fg='white', font='arial 18', command=verificar).place(x=350, y=45)

    ### CPF
    dt_cpf = Label(janela2, text='CPF:', fg='White', font='arial 17', bg='#121212')
    dt_cpf.place(x=25, y=190)

    ### Matrícula
    dt_matricula = Label(janela2, text='Matrícula:', fg='White', font='arial 17', bg='#121212')
    dt_matricula.place(x=25, y=220)

    ### Data de Nascimento
    dt_data = Label(janela2, text='Data de Nascimento:', fg='White', font='arial 17', bg='#121212')
    dt_data.place(x=25, y=250)

    ### Manter na tela
    janela2.mainloop()

### Interface de Cadastro no Formulário
def cadastrar():
    global janela, lb_cpf, lb_data, lb_matricula, lb_nome, en_nome, en_cpf, en_matricula, en_data, janela

    ### Configuraçao da janela
    janela = Toplevel()
    janela.title('Cadastro')
    janela.geometry('500x400')
    janela.resizable(False, False)
    janela['bg'] = '#121212'

    ### Nome 
    lb_nome = Label(janela, text = 'Nome:', bg='#121212', fg='white', font='arial 14')
    lb_nome.place(x= 85, y=20)
    en_nome = Entry(janela, font='arial 14', width=30)
    en_nome.place(x= 85, y=50)

    ### CPF
    lb_cpf = Label(janela, text = 'CPF:', bg='#121212', fg='white', font='arial 14')
    lb_cpf.place(x= 85, y=100)
    en_cpf = Entry(janela, font='arial 14', width=30)
    en_cpf.place(x= 85, y=130)

    ### Matricula
    lb_matricula = Label(janela, text = 'Número de Matrícula:', bg='#121212', fg='white', font='arial 14')
    lb_matricula.place(x= 85, y=180)
    en_matricula = Entry(janela, font='arial 14', width=30)
    en_matricula.place(x= 85, y=210)

    ### Data
    lb_data = Label(janela, text = 'Data de Nascimento:', bg='#121212', fg='white', font='arial 14')
    lb_data.place(x= 85, y=260)
    en_data = Entry(janela, font='arial 14', width=30)
    en_data.place(x= 85, y=290)

    ### Botao
    Button(janela, text='Cadastrar', bg='#00026B', fg='white', font='arial 14', command=salvar).place(x= 325, y=340)

    ### Manter na tela
    janela.mainloop()

### Tela Inicial
tela = Tk()
tela.title('Formulário')
tela.geometry('500x200')
tela.resizable(False, False)
tela['bg'] = '#121212'

Button(text='Formulário', font='arial 18', fg='white', bg='#F2CB07', command=cadastrar).place(x=80, y=70)
Button(text='Dados Salvos', font='arial 18', fg='white', bg='#F2CB07', command=dados_salvos).place(x=250, y=70)

tela.mainloop()
