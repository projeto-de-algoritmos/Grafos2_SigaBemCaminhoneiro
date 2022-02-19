from tkinter import *
from PIL import Image, ImageTk
import networkx as nx
import matplotlib.pyplot as plt

# instancia o grafo
Brasil = nx.DiGraph()

# adicionando os nos
Brasil.add_node('RR')
Brasil.add_node('AP')
Brasil.add_node('AM')
Brasil.add_node('AC')
Brasil.add_node('RO')
Brasil.add_node('PA')
Brasil.add_node('AP')
Brasil.add_node('MA')
Brasil.add_node('PI')
Brasil.add_node('CE')
Brasil.add_node('RN')
Brasil.add_node('PB')
Brasil.add_node('PE')
Brasil.add_node('AL')
Brasil.add_node('SE')
Brasil.add_node('BA')
Brasil.add_node('TO')
Brasil.add_node('MT')
Brasil.add_node('GO')
Brasil.add_node('MS')
Brasil.add_node('MG')
Brasil.add_node('ES')
Brasil.add_node('RJ')
Brasil.add_node('SP')
Brasil.add_node('PR')
Brasil.add_node('SC')
Brasil.add_node('RS')

# adicionando as arestas
Brasil.add_edge('RR', 'AM')
Brasil.add_edge('RR', 'PA')
Brasil.add_edge('AP', 'PA')
Brasil.add_edge('AM', 'RR')
Brasil.add_edge('AM', 'PA')
Brasil.add_edge('AM', 'MT')
Brasil.add_edge('AM', 'RO')
Brasil.add_edge('AM', 'AC')
Brasil.add_edge('RR', 'AM')
Brasil.add_edge('RR', 'PA')
Brasil.add_edge('PA', 'RR')
Brasil.add_edge('PA', 'AP')
Brasil.add_edge('PA', 'MA')
Brasil.add_edge('PA', 'TO')
Brasil.add_edge('PA', 'AM')
Brasil.add_edge('PA', 'MT')
Brasil.add_edge('MA', 'PA')
Brasil.add_edge('MA', 'TO')
Brasil.add_edge('MA', 'PI')
Brasil.add_edge('PI', 'MA')
Brasil.add_edge('PI', 'TO')
Brasil.add_edge('PI', 'BA')
Brasil.add_edge('PI', 'PE')
Brasil.add_edge('PI', 'CE')
Brasil.add_edge('CE', 'PI')
Brasil.add_edge('CE', 'RN')
Brasil.add_edge('CE', 'PB')
Brasil.add_edge('CE', 'PE')
Brasil.add_edge('RN', 'CE')
Brasil.add_edge('RN', 'PB')
Brasil.add_edge('PB', 'CE')
Brasil.add_edge('PB', 'RN')
Brasil.add_edge('PB', 'PE')
Brasil.add_edge('PE', 'PB')
Brasil.add_edge('PE', 'CE')
Brasil.add_edge('PE', 'PI')
Brasil.add_edge('PE', 'AL')
Brasil.add_edge('PE', 'BA')
Brasil.add_edge('AL', 'PE')
Brasil.add_edge('AL', 'SE')
Brasil.add_edge('AL', 'BA')
Brasil.add_edge('SE', 'AL')
Brasil.add_edge('SE', 'BA')
Brasil.add_edge('BA', 'SE')
Brasil.add_edge('BA', 'AL')
Brasil.add_edge('BA', 'PE')
Brasil.add_edge('BA', 'PI')
Brasil.add_edge('BA', 'TO')
Brasil.add_edge('BA', 'GO')
Brasil.add_edge('BA', 'MG')
Brasil.add_edge('BA', 'ES')
Brasil.add_edge('TO', 'PA')
Brasil.add_edge('TO', 'MA')
Brasil.add_edge('TO', 'PI')
Brasil.add_edge('TO', 'BA')
Brasil.add_edge('TO', 'GO')
Brasil.add_edge('TO', 'MT')
Brasil.add_edge('MT', 'RO')
Brasil.add_edge('MT', 'AM')
Brasil.add_edge('MT', 'PA')
Brasil.add_edge('MT', 'TO')
Brasil.add_edge('MT', 'GO')
Brasil.add_edge('MT', 'MS')
Brasil.add_edge('RO', 'MT')
Brasil.add_edge('RO', 'AM')
Brasil.add_edge('RO', 'AC')
Brasil.add_edge('AC', 'AM')
Brasil.add_edge('AC', 'RO')
Brasil.add_edge('GO', 'MT')
Brasil.add_edge('GO', 'TO')
Brasil.add_edge('GO', 'BA')
Brasil.add_edge('GO', 'MG')
Brasil.add_edge('GO', 'MS')
Brasil.add_edge('MG', 'BA')
Brasil.add_edge('MG', 'ES')
Brasil.add_edge('MG', 'GO')
Brasil.add_edge('MG', 'RJ')
Brasil.add_edge('MG', 'SP')
Brasil.add_edge('MG', 'MS')
Brasil.add_edge('ES', 'BA')
Brasil.add_edge('ES', 'MG')
Brasil.add_edge('ES', 'RJ')
Brasil.add_edge('RJ', 'ES')
Brasil.add_edge('RJ', 'MG')
Brasil.add_edge('RJ', 'SP')
Brasil.add_edge('MS', 'MT')
Brasil.add_edge('MS', 'GO')
Brasil.add_edge('MS', 'MG')
Brasil.add_edge('MS', 'SP')
Brasil.add_edge('MS', 'PR')
Brasil.add_edge('SP', 'RJ')
Brasil.add_edge('SP', 'MG')
Brasil.add_edge('SP', 'MS')
Brasil.add_edge('SP', 'PR')
Brasil.add_edge('PR', 'MS')
Brasil.add_edge('PR', 'SP')
Brasil.add_edge('PR', 'SC')
Brasil.add_edge('SC', 'PR')
Brasil.add_edge('SC', 'RS')
Brasil.add_edge('RS', 'SC')

estados = list(Brasil.nodes)
estados.sort()
traduz = []
for i in range(len(estados)):
    traduz.append({'estado': str(estados[i]), 'cod': i})

malha_rodoviaria = {}


def retorna_cod_estado(estado):
    for i in range(len(estados)):
        if traduz[i]['estado'] == estado:
            cod = traduz[i]['cod']
    return cod


def retorna_nome_estado(cod):
    estado = str('-')
    for i in range(len(traduz)):
        if traduz[i]['cod'] == int(cod):
            estado = traduz[i]['estado']
    return estado


def bfs(grafo, inicio, fim):
    explorado = []
    fila = [[inicio]]
    if inicio == fim:
        return inicio
    while fila:
        caminho = fila.pop(0)
        no = caminho[-1]
        if no not in explorado:
            vizinhos = grafo[no]
            for vizinho in vizinhos:
                novo_caminho = caminho.copy()
                novo_caminho.append(vizinho)
                fila.append(novo_caminho)
                if vizinho == fim:
                    return novo_caminho
            explorado.append(no)


def reativa_estrada(estado1, estado2):
    Brasil.add_edge(estado1, estado2)
    return


def estados_ligados(estado):
    lista_estados_ligados = Brasil.neighbors(estado)
    return lista_estados_ligados


def imprime_mapa():

    nx.draw_spring(Brasil, with_labels=1, node_size=300, font_size=8, width=2, style="solid", node_color="green",
                   font_color="white", font_weight="bold", edge_color="gray")
    plt.show()
    return


lista_estradas_inativas = []


def inativa_estrada(estado1, estado2):
    Brasil.remove_edge(estado1, estado2)
    lista_estradas_inativas.append({'estado1': estado1, 'estado2': estado2})
    return


def mostra_estradas_inativas():
    if len(lista_estradas_inativas) == 0:
        return '\nNão há estradas inativas.\n'
    else:
        lista_final = []
        lista_final.append('Estradas inativas:\n')
        for i in range(len(lista_estradas_inativas)):
            lista_final.append(str(i) + '. ' +
                               str(lista_estradas_inativas[i]['estado1']) + ' - ' + str(lista_estradas_inativas[i]['estado2']))
        lista_final = ('\n'.join(lista_final))
        return lista_final


def melhor_caminho(estado_1, estado_2):

    malha_rodoviaria = {}

    estradas = list(Brasil.edges)

    for i in range(len(estradas)):

        estado1 = estradas[i][0]
        estado2 = estradas[i][1]
        cod_estado1 = retorna_cod_estado(estado1)
        cod_estado2 = retorna_cod_estado(estado2)
        if cod_estado1 not in malha_rodoviaria:
            malha_rodoviaria[cod_estado1] = []

        malha_rodoviaria[cod_estado1].append(cod_estado2)

    lista_final = []
    lista_final.append('O melhor caminho para você utilizar é: ')
    caminho = bfs(malha_rodoviaria, retorna_cod_estado(
        estado_1), retorna_cod_estado(estado_2))

    for i in range(len(caminho)):
        if i == (len(caminho) - 1):
            lista_final.append(retorna_nome_estado(caminho[i]))
        else:
            lista_final.append(retorna_nome_estado(caminho[i]) + ' -> ')

    lista_final.append('. Boa viagem!')
    lista_final = (''.join(lista_final))

    return lista_final


def pergunta_caminho():

    lista_estados = list(Brasil.nodes)
    lista_estados.sort()
    lista_final = []
    for i in range(len(lista_estados)):
        if i == (len(lista_estados) - 1):
            lista_final.append(str(lista_estados[i]) + '.')
        else:
            lista_final.append(str(lista_estados[i]) + ', ')

    lista_final = (''.join(lista_final))
    return lista_final


def mostra_estradas():
    lista_estradas = list(Brasil.edges)

    if len(lista_estradas) == 0:
        return '\nNão há estradas ativas.\n'

    lista_final = []
    lista_final.append('Estradas ativas:\n')
    for i in range(len(lista_estradas)):
        lista_final.append(str(i) + '. ' +
                           str(lista_estradas[i][0]) + ' - ' + str(lista_estradas[i][1]))
    lista_final = ('\n'.join(lista_final))
    return lista_final


def pergunta_inativar(x):

    lista_estradas = list(Brasil.edges)
    cod_estrada = int(x)

    if(int(x) > len(lista_estradas) or int(x) < 0):
        return 'Não existe essa estrada! Digite um número listado.'

    estado_origem = lista_estradas[cod_estrada][0]
    estado_final = lista_estradas[cod_estrada][1]
    lista_final = []
    inativa_estrada(estado_origem, estado_final)

    lista_final.append('\nA estrada que liga ' + estado_origem +
                       ' a ' + estado_final + ' foi desativada.\n')
    lista_final = (''.join(lista_final))
    return lista_final


def ativa_estrada(estado1, estado2):
    Brasil.add_edge(estado1, estado2)
    return


def pergunta_ativar(x):

    cod_estrada = int(x)

    if(int(x) > len(lista_estradas_inativas) or int(x) < 0):
        return 'Essa estrada não está inativa! Digite um número listado.'

    estado_origem = lista_estradas_inativas[cod_estrada]['estado1']
    estado_final = lista_estradas_inativas[cod_estrada]['estado2']
    lista_final = []
    ativa_estrada(estado_origem, estado_final)
    lista_estradas_inativas.pop(cod_estrada)

    lista_final.append('\nA estrada que liga ' + estado_origem +
                       ' a ' + estado_final + ' foi reativada.\n')

    lista_final = (''.join(lista_final))
    return lista_final


root = Tk()

root.geometry('1000x800')
root.config(background='White')
root.resizable(width=False, height=False)

imag_1 = Image.open('background.jpg')

imag_1 = ImageTk.PhotoImage(imag_1)

background = Label(image=imag_1)
background.grid(row=0, column=0, columnspan=3)


def estradas_ativas(x):
    global background
    background.grid_forget()
    background = Label(image=imag_1)
    background.grid(row=1, column=0, columnspan=3)

    text = Text(root, width=30, height=30, fg='snow', bg='black')
    text.place(relx=0.5, rely=0.4, anchor=CENTER)
    texto = mostra_estradas()
    text.insert(END, texto)
    if int(x) == 1:
        buttonVoltar = Button(root, text='Voltar', padx=117,
                              pady=5, fg='white', bg='black', command=caminhoneiro)
        buttonVoltar.place(relx=0.5, rely=0.8, anchor=CENTER)
    else:
        buttonVoltar = Button(root, text='Voltar', padx=117,
                              pady=5, fg='white', bg='black', command=fiscal)
        buttonVoltar.place(relx=0.5, rely=0.8, anchor=CENTER)


def estradas_inativas(y):
    global background
    background.grid_forget()
    background = Label(image=imag_1)
    background.grid(row=1, column=0, columnspan=3)

    if int(y) == 1:
        buttonVoltar = Button(root, text='Voltar', padx=117,
                              pady=5, fg='white', bg='black', command=caminhoneiro)
        buttonVoltar.place(relx=0.5, rely=0.8, anchor=CENTER)
    else:
        buttonVoltar = Button(root, text='Voltar', padx=117,
                              pady=5, fg='white', bg='black', command=fiscal)
        buttonVoltar.place(relx=0.5, rely=0.8, anchor=CENTER)

    text = Text(root, width=30, height=30, fg='snow', bg='black')
    text.place(relx=0.5, rely=0.4, anchor=CENTER)
    texto = mostra_estradas_inativas()
    text.insert(END, texto)


def MyClick(atual, dest):
    text = Text(root, width=90, height=2, fg='black', bg='White')
    text.place(relx=0.5, rely=0.7, anchor=CENTER)
    texto = melhor_caminho(atual, dest)
    text.insert(END, texto)


def encontrar():
    global background
    background.grid_forget()
    background = Label(image=imag_1)
    background.grid(row=1, column=0, columnspan=3)

    text = Text(root, width=41, height=2, fg='White', bg='black')
    text.place(relx=0.5, rely=0.1, anchor=CENTER)
    texto = '\t    Olá, Caminhoneiro!\nNo Brasil nós temos os seguintes estados:\n'
    text.insert(END, texto)

    text = Text(root, width=90, height=2, fg='White', bg='black')
    text.place(relx=0.5, rely=0.15, anchor=CENTER)
    texto = pergunta_caminho()
    text.insert(END, texto)

    text = Text(root, width=43, height=1, fg='White', bg='black')
    text.place(relx=0.5, rely=0.26, anchor=CENTER)
    texto = 'Insira o local de partida: (apenas a sigla)'
    text.insert(END, texto)
    estado_atual = Entry(root, width=26, fg='black', bg='White')
    estado_atual.place(relx=0.5, rely=0.3, anchor=CENTER)

    text = Text(root, width=43, height=1, fg='White', bg='black')
    text.place(relx=0.5, rely=0.36, anchor=CENTER)
    texto = 'Insira o local da chegada: (apenas a sigla)'
    text.insert(END, texto)
    estado_destino = Entry(root, width=26, fg='black', bg='White')
    estado_destino.place(relx=0.5, rely=0.4, anchor=CENTER)

    buttonConfirmar = Button(root, text='Confirmar', padx=117, pady=5, fg='white',
                             bg='black', command=lambda: MyClick(estado_atual.get(), estado_destino.get()))
    buttonConfirmar.place(relx=0.5, rely=0.5, anchor=CENTER)

    buttonVoltar = Button(root, text='Voltar', padx=117, pady=5,
                          fg='white', bg='black', command=lambda: caminhoneiro())
    buttonVoltar.place(relx=0.5, rely=0.8, anchor=CENTER)


def MyClick1(atual):
    text = Text(root, width=90, height=2, fg='White', bg='black')
    text.place(relx=0.5, rely=0.7, anchor=CENTER)
    texto = pergunta_inativar(atual)
    text.insert(END, texto)

    text = Text(root, width=30, height=20, fg='snow', bg='black')
    text.place(relx=0.5, rely=0.30, anchor=CENTER)
    texto = mostra_estradas()
    text.insert(END, texto)


def inativar():
    global background
    background.grid_forget()
    background = Label(image=imag_1)
    background.grid(row=1, column=0, columnspan=3)

    text = Text(root, width=30, height=20, fg='snow', bg='black')
    text.place(relx=0.5, rely=0.30, anchor=CENTER)
    texto = mostra_estradas()
    text.insert(END, texto)

    text = Text(root, width=50, height=3, fg='White', bg='black')
    text.place(relx=0.5, rely=0.05, anchor=CENTER)
    texto = 'Há algum problema com as estradas?\nAqui você pode desativar uma delas.\nAtualmente temos as seguintes estradas funcionando:\n'
    text.insert(END, texto)

    text = Text(root, width=60, height=1, fg='White', bg='black')
    text.place(relx=0.5, rely=0.55, anchor=CENTER)
    texto = 'Digite o número da estrada que você deseja desativar:'
    text.insert(END, texto)
    estrada = Entry(root, width=26, fg='black', bg='White')
    estrada.place(relx=0.5, rely=0.6, anchor=CENTER)

    buttonConfirmar = Button(root, text='Confirmar', padx=117, pady=5,
                             fg='white', bg='black', command=lambda: MyClick1(estrada.get()))
    buttonConfirmar.place(relx=0.5, rely=0.65, anchor=CENTER)

    buttonVoltar = Button(root, text='Voltar', padx=117, pady=5,
                          fg='white', bg='black', command=lambda: fiscal())
    buttonVoltar.place(relx=0.5, rely=0.8, anchor=CENTER)


def MyClick2(atual):
    text = Text(root, width=90, height=2, fg='White', bg='black')
    text.place(relx=0.5, rely=0.7, anchor=CENTER)
    texto = pergunta_ativar(atual)
    text.insert(END, texto)

    text = Text(root, width=30, height=20, fg='snow', bg='black')
    text.place(relx=0.5, rely=0.30, anchor=CENTER)
    texto = mostra_estradas_inativas()
    text.insert(END, texto)


def reativar():
    global background
    background.grid_forget()
    background = Label(image=imag_1)
    background.grid(row=1, column=0, columnspan=3)

    text = Text(root, width=30, height=20, fg='snow', bg='black')
    text.place(relx=0.5, rely=0.30, anchor=CENTER)
    texto = mostra_estradas_inativas()
    text.insert(END, texto)

    text = Text(root, width=50, height=3, fg='White', bg='black')
    text.place(relx=0.5, rely=0.05, anchor=CENTER)
    texto = 'Há alguma estrada restaurada?\nAqui você pode reativar uma delas.\nAtualmente temos as seguintes estradas desativadas:\n'
    text.insert(END, texto)

    text = Text(root, width=50, height=1, fg='White', bg='black')
    text.place(relx=0.5, rely=0.55, anchor=CENTER)
    texto = 'Digite o número da estrada que você deseja reativar:'
    text.insert(END, texto)
    estrada = Entry(root, width=26, fg='black', bg='White')
    estrada.place(relx=0.5, rely=0.6, anchor=CENTER)

    buttonConfirmar = Button(root, text='Confirmar', padx=117, pady=5,
                             fg='white', bg='black', command=lambda: MyClick2(estrada.get()))
    buttonConfirmar.place(relx=0.5, rely=0.65, anchor=CENTER)

    buttonVoltar = Button(root, text='Voltar', padx=117, pady=5,
                          fg='white', bg='black', command=lambda: fiscal())
    buttonVoltar.place(relx=0.5, rely=0.8, anchor=CENTER)


def caminhoneiro():

    global background
    background.grid_forget()
    background = Label(image=imag_1)
    background.grid(row=1, column=0, columnspan=3)

    buttonEncontrar = Button(root, text='Encontrar a melhor rota para o meu destino',
                             padx=117, pady=5, fg='white', bg='black', command=lambda: encontrar())
    buttonEncontrar.place(relx=0.5, rely=0.1, anchor=CENTER)

    buttonAtivas = Button(root, text='Saber quais estradas estão ativas', padx=117,
                          pady=5, fg='white', bg='black', command=lambda: estradas_ativas(1))
    buttonAtivas.place(relx=0.5, rely=0.2, anchor=CENTER)

    buttonInativas = Button(root, text='Saber quais estradas estão inativas', padx=117,
                            pady=5, fg='white', bg='black', command=lambda: estradas_inativas(1))
    buttonInativas.place(relx=0.5, rely=0.3, anchor=CENTER)

    buttonMapa = Button(root, text='Ver um mapa com estradas atuais', padx=117,
                        pady=5, fg='white', bg='black', command=lambda: imprime_mapa())
    buttonMapa.place(relx=0.5, rely=0.4, anchor=CENTER)

    buttonVoltar = Button(root, text='Voltar', padx=117,
                          pady=5, fg='white', bg='black', command=menu)
    buttonVoltar.place(relx=0.5, rely=0.7, anchor=CENTER)


def fiscal():

    global background
    background.grid_forget()
    background = Label(image=imag_1)
    background.grid(row=1, column=0, columnspan=3)

    buttonInativar = Button(root, text='Inativar uma estrada', padx=117,
                            pady=5, fg='white', bg='black', command=lambda: inativar())
    buttonInativar.place(relx=0.5, rely=0.1, anchor=CENTER)

    buttonReativar = Button(root, text='Reativar uma estrada', padx=117,
                            pady=5, fg='white', bg='black', command=lambda: reativar())
    buttonReativar.place(relx=0.5, rely=0.2, anchor=CENTER)

    buttonAtivas = Button(root, text='Saber quais estradas estão ativas', padx=117,
                          pady=5, fg='white', bg='black', command=lambda: estradas_ativas(0))
    buttonAtivas.place(relx=0.5, rely=0.3, anchor=CENTER)

    buttonInativas = Button(root, text='Saber quais estradas estão inativas', padx=117,
                            pady=5, fg='white', bg='black', command=lambda: estradas_inativas(0))
    buttonInativas.place(relx=0.5, rely=0.4, anchor=CENTER)

    buttonMapa = Button(root, text='Ver um mapa com estradas atuais', padx=117,
                        pady=5, fg='white', bg='black', command=lambda: imprime_mapa())
    buttonMapa.place(relx=0.5, rely=0.5, anchor=CENTER)

    buttonVoltar = Button(root, text='Voltar', padx=117,
                          pady=5, fg='white', bg='black', command=menu)
    buttonVoltar.place(relx=0.5, rely=0.7, anchor=CENTER)


def menu():

    global background
    background.grid_forget()
    background = Label(image=imag_1)
    background.grid(row=1, column=0, columnspan=3)

    logo = Image.open('assets/logo.jpg')
    logo = ImageTk.PhotoImage(logo)
    logo_label = Label(root, image=logo)
    logo_label.image = logo
    logo_label.grid(column=0, row=1)
    logo_label.place(relx=0.5, rely=0.2, anchor=CENTER)

    placa = Image.open('assets/placa.png')
    placa = ImageTk.PhotoImage(placa)
    placa_label = Label(root, image=placa)
    placa_label.image = placa
    placa_label.grid(column=0, row=1)
    placa_label.place(relx=0.5, rely=0.4, anchor=CENTER)

    buttonCaminhoneiro = Button(root, text='Caminhoneiro', padx=85,
                                pady=5, fg='white', bg='black', command=caminhoneiro)
    buttonCaminhoneiro.place(relx=0.5, rely=0.6, anchor=CENTER)

    buttonFiscal = Button(root, text='Fiscal do DER', padx=85,
                          pady=5, fg='white', bg='black', command=fiscal)
    buttonFiscal.place(relx=0.5, rely=0.7, anchor=CENTER)

    buttonSaida = Button(root, text='Sair', padx=85, pady=5,
                         fg='white', bg='black', command=root.quit)
    buttonSaida.place(relx=0.5, rely=0.9, anchor=CENTER)


menu()
root.mainloop()
