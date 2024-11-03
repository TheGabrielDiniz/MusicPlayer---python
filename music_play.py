from tkinter import *
import pygame
from tkinter import filedialog, ttk
import time
from mutagen.mp3 import MP3
from PIL import Image, ImageTk

# Tela
tocador = Tk()
tocador.title('Tocador MPG V.1')
# tocador.iconbitmap(r'logozin.ico')
tocador.geometry("660x520")
tocador.configure(bg='DarkSeaGreen')

# Colocar uma imagem de fundo
# image = PhotoImage(file='C:/Users/Mdiniz/Pictures/coizinhas/100/teste_music.png')

# Se você quer ela na frente do programa
# w = Label(tocador, image=image)
# w.image = image
# w.pack()

# Se quer no fundo do programa
# Imagem no background

# image = image.subsample(1, 1)

# Direcionamento da imagem

# labelimage = Label(image=image)

# labelimage.place(x=0, y=0, relwidth=1.0, relheight=1.0)

# iniciador do pygame
pygame.mixer.init()

linksMusicas = []

# FUNÇÕES

# Tempo da música
def contagem():
    #Verificar se a barra de musica parou
    if stopped:
        return

    # formatação do tempo
    contar_tempo = pygame.mixer.music.get_pos() / 1000

    # conversão
    conversao_contar_tempo = time.strftime('%H:%M:%S', time.gmtime(contar_tempo))

    # Pegar a música
    # ver a música pelo número
    som_recorrente = caixa_musicas.curselection()

    # ver o nome da musica na playlist
    musica = caixa_musicas.get(som_recorrente)

    # acionar o diretório

    def selected_item():
        for i in caixa_musicas.curselection():
            return (caixa_musicas.getint(i))

    music = selected_item()


    musica = f'{linksMusicas[music]}'

    # Pegar a música pela Mutagen
    musica_mut = MP3(musica)

    # Ter uma extensão da mùsica
    extensao_musica = musica_mut.info.length

    # converter o tempo
    conversao_extensao_musica = time.strftime('%M:%S', time.gmtime(extensao_musica))


    # slide musica plus
        #slide_musica.config(to=extensao_musica)
        #barra_status.config(text=slide_musica.get())

    #Verificar a musica parou
    if int(slide_musica.get()) == int(extensao_musica):
        reset()

    elif paused:
        #Verificar se o reset passa
        pass
    else:
        #mover o slide 1 segundo no tempo
        tempo_seguinte = int(slide_musica.get()) + 1

        #Carregar novo tempo do slide
        slide_musica.config(to=extensao_musica, value=tempo_seguinte)

        #Converter a posição do slide no cronometro
        conversao_contar_tempo = time.strftime('%H:%M:%S', time.gmtime(int(slide_musica.get())))

        #Resetar slide
        barra_status.config(text=f'Tempo da Música  :  {conversao_contar_tempo}  /  {conversao_extensao_musica} ',
                            fg='DarkSlateGray')


    # contagem na barra
    if contar_tempo > 0:
        barra_status.config(text=f'Tempo da Música  :  {conversao_contar_tempo}  /  {conversao_extensao_musica} ',
                        fg='DarkSlateGray')

    # subir tempo
    barra_status.after(1000, contagem)


# Função de adicionar música
def adicionar_musica():
    musica = filedialog.askopenfilename(initialdir='C:/', title='Escolha a música', filetypes=(('Arquivos mp3', '*.mp3'),))
    # minha_label.config(text=musica)

    linksMusicas.append(musica)

    # tirar coisas do nome
    musica = musica.replace('C:/Users/', '')
    musica = musica.replace('.mp3', '')


    nome = musica.split('/')


    print(len(nome)-1)

    x = len(nome)-1

    while len(nome)-1 > 0:
        del nome[x-1]
        x -= 1

    print(nome)

    # adicionar a musica na playlist
    caixa_musicas.insert(END, nome[0])


# Função de adicionar várias músicas
def adicionar_varias_musicas():
    musicas = filedialog.askopenfilenames(initialdir='C:/' or '/storage/emulated/0' or '/Meu aparelho',
                                          title='Escolha as músicas', filetypes=(('Arquivos mp3', '*.mp3'),))

    # Loops
    for musica in musicas:
        # tirar coisas do nome
        # musica = musica.replace('C:/Users/', '')
        musica = musica.replace('.mp3', '')

        # adicionar as musicas na playlist
        caixa_musicas.insert(END, musica)


# Função de deletar música
def deletar_musica():
    caixa_musicas.delete(ANCHOR)
    reset()


# Função de deletar todas as músicas
def deletar_musicas():
    caixa_musicas.delete(0, END)
    reset()


# ------------------
# FUNÇÕES DOS BOTÕES
# ------------------

# Função do play
def play():
    #Fazer a variável mudar pra tocar o som
    global stopped
    stopped = False

    # Limpar barra do tempo
    barra_status.config(text='')

    # Zerar a barra de musica
    slide_musica.config(value=0)

    #musica = caixa_musicas.get(curselection)

    def selected_item():
        for i in caixa_musicas.curselection():
            return (caixa_musicas.getint(i))

    music = selected_item()


    musica = f'{linksMusicas[music]}'

    pygame.mixer.music.load(musica)
    pygame.mixer.music.play()

    # função pra contar o tempo da musica
    contagem()


# Variável Reset
global stopped
stopped = False
# Função do reset
def reset():
    pygame.mixer.music.stop()
    caixa_musicas.selection_clear(ACTIVE)

    # Limpar barra do tempo
    barra_status.config(text='')

    # Zerar a barra de musica
    slide_musica.config(value=0)

    #transformar variável
    global stopped
    stopped = True

# Função de pular
def proxima_musica():
    # Resetar a barra de música e de status
    barra_status.config(text='')
    slide_musica.config(value=0)

    # ver a música pelo número
    proxima = caixa_musicas.curselection()

    # selecionar somente o número da musica
    proxima = proxima[0] + 1

    # ver o nome da musica na playlist
    musica = caixa_musicas.get(proxima)

    # acionar o diretório

    def selected_item():
        for i in caixa_musicas.curselection():
            return (caixa_musicas.getint(i))

    music = selected_item()


    musica = f'{linksMusicas[music]}'

    # Tocar a próxima música
    pygame.mixer.music.load(musica)
    pygame.mixer.music.play()

    # limpar a barra de seleção
    caixa_musicas.selection_clear(0, END)

    # mover a barra pra baixo
    caixa_musicas.activate(proxima)

    # ativar a barra
    caixa_musicas.selection_set(proxima, last=None)


# Função de voltar na música anterior
def anterior_musica():
    # Resetar a barra de música e de status
    barra_status.config(text='')
    slide_musica.config(value=0)

    # ver a música pelo número
    anterior = caixa_musicas.curselection()

    # selecionar somente o número da musica
    anterior = anterior[0] - 1

    # ver o nome da musica na playlist
    musica = caixa_musicas.get(anterior)

    # acionar o diretório

    def selected_item():
        for i in caixa_musicas.curselection():
            return (caixa_musicas.getint(i))

    music = selected_item()


    musica = f'{linksMusicas[music]}'

    # Tocar a próxima música
    pygame.mixer.music.load(musica)
    pygame.mixer.music.play()

    # limpar a barra de seleção
    caixa_musicas.selection_clear(0, END)

    # mover a barra pra baixo
    caixa_musicas.activate(anterior)

    # ativar a barra
    caixa_musicas.selection_set(anterior, last=None)


# Variável paused
global paused
paused = False


# Função de pause
def pause(is_paused):
    global paused
    paused = is_paused

    if paused:
        # Unpause
        pygame.mixer.music.unpause()
        paused = False
    else:
        # Pause
        pygame.mixer.music.pause()
        paused = True

# Função Volume
def Volume(x):
    pygame.mixer.music.set_volume(slide_volume.get())
#    barra_status.config(text=slide_volume.get())


# Função deslizar da música
def deslizar(x):
    # restruturar o nome da musica
    #musica = caixa_musicas.get(ACTIVE)

    def selected_item():
        for i in caixa_musicas.curselection():
            return (caixa_musicas.getint(i))

    music = selected_item()


    musica = f'{linksMusicas[music]}'

    #carregar e tocar a musica
    pygame.mixer.music.load(musica)
    pygame.mixer.music.play(start=slide_musica.get())

# Criação do Menu Frame
Menu_frame = Frame()
Menu_frame.pack(pady=20)

# Barra de Volume
barra_volume = LabelFrame(Menu_frame, text="Volume")
barra_volume.grid(row=0, column=1, padx=15)

# Slide do Volume
slide_volume = ttk.Scale(barra_volume, from_=1, to=0, orient=VERTICAL, len=165, command=Volume)
slide_volume.pack(pady=10)

# Slide da Musica
slide_musica = ttk.Scale(Menu_frame, from_=0, to=100, orient=HORIZONTAL, len=520, value=0, command=deslizar)
slide_musica.grid(row=2, column=0, pady=20)

# Playlist
caixa_musicas = Listbox(Menu_frame, font='Candara', bg="#315b78", fg="#FFFAFA", width=60, selectbackground='MintCream',
                        selectforeground='grey11')
caixa_musicas.grid(row=0, column=0)

# Botões capas
voltar = Image.open("botao-voltar.png").resize((50, 50))
voltar_btn_img = ImageTk.PhotoImage(voltar)

plays = Image.open("botao-play.png").resize((50, 50))
play_btn_img = ImageTk.PhotoImage(plays)

parar = Image.open("stop-button.png").resize((50, 50))
parar_btn_img = ImageTk.PhotoImage(parar)

pauses = Image.open("botao-pause.png").resize((50, 50))
pause_btn_img = ImageTk.PhotoImage(pauses)

pular = Image.open("right.png").resize((50, 50))
pular_btn_img = ImageTk.PhotoImage(pular)


# Frames
controle_frame = Frame(Menu_frame)
controle_frame.grid(row=1, column=0, pady=20)

# Botões comandos
voltar_button = Button(controle_frame, borderwidth=0, command=anterior_musica, image=voltar_btn_img)
play_button = Button(controle_frame, borderwidth=0, command=play, image=play_btn_img)
parar_button = Button(controle_frame, borderwidth=0, command=reset, image=parar_btn_img)
pause_button = Button(controle_frame, borderwidth=0, command=lambda: pause(paused), image=pause_btn_img)
pular_button = Button(controle_frame, borderwidth=0, command=proxima_musica, image=pular_btn_img)

voltar_button.grid(row=0, column=0, padx=0)
play_button.grid(row=0, column=1, padx=0)
parar_button.grid(row=0, column=2, padx=0)
pause_button.grid(row=0, column=3, padx=0)
pular_button.grid(row=0, column=4, padx=0)

# Menu
meu_menu = Menu(tocador)
tocador.config(menu=meu_menu)

# adicionar músicas ao menu
colocar_msc_menu = Menu(meu_menu, tearoff=0)
meu_menu.add_cascade(label='Adicionar Músicas', menu=colocar_msc_menu)

# colocar um áudio na playlist
colocar_msc_menu.add_command(label='Adicionar uma música', command=adicionar_musica)

# colocar vários áudios na playlist
colocar_msc_menu.add_command(label='Adicionar várias músicas', command=adicionar_varias_musicas)

# Label temporaria
# minha_label = Label(tocador, text='')
# minha_label.pack(pady=20)

# Deletar um áudio da Playlist
remover_msc_menu = Menu(meu_menu, tearoff=0)
meu_menu.add_cascade(label='Remover músicas', menu=remover_msc_menu)
remover_msc_menu.add_command(label='Remover a música selecionada', command=deletar_musica)
remover_msc_menu.add_command(label='Remover todas as músicas', command=deletar_musicas)

# Criar barra de Status
barra_status = Label(tocador, text='', bd=1, relief=GROOVE, anchor=E, bg='LightSteelBlue')
barra_status.pack(fill=X, side=BOTTOM, ipady=2)

tocador.mainloop()
