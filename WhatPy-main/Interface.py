import customtkinter as ctk
import tkinter as tk
from customtkinter import filedialog
import csv

# Função para mostrar um tooltip (balão de comentário)
def mostrar_tooltip(event, texto):
    global tooltip
    x = event.widget.winfo_rootx() + 25
    y = event.widget.winfo_rooty() + 25

    # Cria a janela de tooltip
    tooltip = tk.Toplevel(event.widget)
    tooltip.wm_overrideredirect(True)
    tooltip.wm_geometry("+%d+%d" % (x, y))

    label = ctk.CTkLabel(tooltip, text=texto, fg_color="white", text_color="black")
    label.pack()

# Função para esconder o tooltip
def esconder_tooltip(event):
    global tooltip
    if tooltip:
        tooltip.destroy()

# Função do Slider
def atualizar_tempo(wait_time_value):
    tempo_label.configure(text=f"Tempo de Espera para o envio por mensagens: {int(wait_time_value)}")

# Função de esconder TextBox da hora
def toggle_textbox():
    if inst_msg_var.get():
        escolha_label.grid_forget()
        txtbox_hora.grid_forget()
    else:
        escolha_label.grid(row=5, column=0, padx=(10, 10), pady=(10, 10), sticky="w")
        txtbox_hora.grid(row=6, column=0, padx=(10, 10), pady=(5, 10), sticky="w")

# Função carregar CSV
def carregar_csv():
    from Logica import get_phones
    arquivo_csv = filedialog.askopenfilename(
        title='Selecione um Arquivo', 
        filetypes=[("Arquivos CSV", "*.csv"), ("Todos os Arquivos", "*.*")]
    )
    if arquivo_csv:
        get_phones(
            arquivo_csv=arquivo_csv,
            row_number=(int(txtbox_coluna.get("0.0", "end").strip()) - 1),
            terminal_box=terminal_box,
            atualizar_feedback_func=atualizar_feedback )
    else:
        atualizar_feedback("Nenhum csv foi carregado", terminal_box)

# Função carregar IMG
def carregar_img():
    global arquivo_img
    arquivo_img = filedialog.askopenfilename(
        title='Selecione um Arquivo',
        filetypes=[
            ("Imagens JPEG", "*.jpg *.jpeg"),
            ("Imagens PNG", "*.png"),
            ("Imagens GIF", "*.gif"),
            ("Imagens BMP", "*.bmp"),
            ("Imagens WebP", "*.webp"),
            ("Imagens SVG", "*.svg"),
            ("Imagens TIFF", "*.tiff"),
            ("Ícones", "*.ico"),
            ("Todos os Arquivos", "*.*")]
    )
    if arquivo_img: 
       atualizar_feedback(f"Imagem carregada: {arquivo_img}", terminal_box) 
    else: 
       atualizar_feedback("Nenhuma imagem foi carregada", terminal_box)        
    return arquivo_img

# Função do Terminal
def atualizar_feedback(mensagem, terminal_box):
    if terminal_box.winfo_exists():  # Verifica se o widget ainda existe
        terminal_box.configure(state="normal")
        terminal_box.delete("1.0", "end")
        terminal_box.insert("1.0",(mensagem))
        terminal_box.configure(state="disabled")

# Configurar linhas e colunas da janela principal
app = ctk.CTk()
app.geometry("1280x720")
app.grid_rowconfigure(0, weight=1)  # Primeira linha expande
app.grid_rowconfigure(1, weight=1)  # Segunda linha expande
app.grid_columnconfigure(0, weight=1)  # Primeira coluna expande
app.grid_columnconfigure(1, weight=2)  # Segunda coluna expande mais

# Frame para arquivo CSV
framecsv = ctk.CTkFrame(app)
framecsv.grid(row=0, column=0, padx=(10, 10), pady=(10, 5), sticky="nsew")

# Config do Grid do Frame CSV
framecsv.grid_rowconfigure(0, weight=1)
framecsv.grid_columnconfigure(0, weight=1)

# Frame para imagem
frameimg = ctk.CTkFrame(app)
frameimg.grid(row=1, column=0, padx=(10, 10), pady=(5, 10), sticky="nsew")

# Config do Grid do Frame Img
frameimg.grid_rowconfigure(0, weight=1)
frameimg.grid_columnconfigure(0, weight=1)

# Frame para texto
frametxt = ctk.CTkFrame(app)
frametxt.grid(row=0, column=1, rowspan=2, padx=(10, 10), pady=(10, 10), sticky="nsew")

# Config do Grid do Frame Txt
frametxt.grid_rowconfigure(0, weight=4)
frametxt.grid_rowconfigure(1, weight=0)
frametxt.grid_rowconfigure(2, weight=0)
frametxt.grid_rowconfigure(3, weight=0)
frametxt.grid_rowconfigure(4, weight=0)
frametxt.grid_rowconfigure(5, weight=0)
frametxt.grid_rowconfigure(6, weight=1)
frametxt.grid_columnconfigure(0, weight=1)
frametxt.grid_columnconfigure(1, weight=1)

# Botão CSV

csv_button = ctk.CTkButton(
    
    framecsv, 
    text="Carregar Arquivo CSV", 
    command=carregar_csv, 
    height=50, 
    fg_color="green",  # Cor de fundo do botão
    hover_color="green"  # Mantém a mesma cor ao passar o mouse
)
csv_button.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew")
csv_button.bind("<Enter>", lambda event: mostrar_tooltip(event, "Carregar um arquivo CSV"))
csv_button.bind("<Leave>", esconder_tooltip)

# Botão Img
img_button = ctk.CTkButton(
    frameimg, 
    text="Carregar Imagem", 
    command=carregar_img, 
    height=50,
    fg_color="green",  # Cor de fundo do botão
    hover_color="green"  # A cor do botão não mudará ao passar o mouse
)
img_button.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew")
img_button.bind("<Enter>", lambda event: mostrar_tooltip(event, "Carregar uma imagem"))
img_button.bind("<Leave>", esconder_tooltip)



# Caixa de Texto
txt_box = ctk.CTkTextbox(frametxt)
txt_box.grid(row=0, column=0, padx=(10,10), pady=(10,10), sticky="nsew", columnspan=2)

# CheckBoxes
tab_close_var = ctk.BooleanVar()
tab_close = ctk.CTkCheckBox(frametxt, text="Fechar Abas?", command=None, variable=tab_close_var, fg_color="green")
tab_close.grid(row=1, column=0, padx=(10, 10), pady=(10,10), sticky="w")

# Funções para alterar a cor ao passar o mouse
def on_enter(event):
    tab_close.configure(fg_color="darkgreen")  # Muda para um verde escuro

def on_leave(event):
    tab_close.configure(fg_color="green")  # Restaura o verde original

tab_close.bind("<Enter>", on_enter)
tab_close.bind("<Leave>", on_leave)

tab_close.bind("<Enter>", lambda event: mostrar_tooltip(event, "Fechar as abas ao final"))
tab_close.bind("<Leave>", esconder_tooltip)



inst_msg_var = ctk.BooleanVar()
inst_msg = ctk.CTkCheckBox(frametxt, text="Começar Imediatamente?", variable=inst_msg_var, command=toggle_textbox, fg_color="green")
inst_msg.grid(row=2, column=0, padx=(10, 10), pady=(10,10), sticky="w")

# Funções para alterar a cor ao passar o mouse
def on_enter_inst_msg(event):
    inst_msg.configure(fg_color="darkgreen")  # Muda para um verde escuro

def on_leave_inst_msg(event):
    inst_msg.configure(fg_color="green")  # Restaura a cor original (cinza)

inst_msg.bind("<Enter>", on_enter_inst_msg)
inst_msg.bind("<Leave>", on_leave_inst_msg)

inst_msg.bind("<Enter>", lambda event: mostrar_tooltip(event, "Marcado: As mensagens serão enviadas"))
inst_msg.bind("<Leave>", esconder_tooltip)

# Label para exibir o valor do slider
wait_time_value = 10
tempo_label = ctk.CTkLabel(frametxt, text=f"Tempo de Espera para o envio por mensagens: {wait_time_value}")
tempo_label.grid(row=3, column=0, padx=(220,10), pady=(10,10), sticky="w")

# Slider
import customtkinter as ctk

# Configurar um tema sem efeitos de hover no botão do slider
ctk.set_appearance_mode("Dark")  # Ou "Light", depende do seu gosto

# Criação do CTkSlider
wait_time = ctk.CTkSlider(
    frametxt, 
    from_=1, 
    to=40, 
    number_of_steps=39, 
    command=atualizar_tempo, 
    button_color='green',  # Cor do botão
    progress_color='green'  # Cor da barra de progresso
)

# Aplicar a grade para a interface
wait_time.grid(row=3, column=0, padx=(10,10), pady=(10,10), sticky="w")

# Textbox para exibir "Escolha quando a mensagem será enviada"
escolha_label = ctk.CTkLabel(frametxt, text="Digite a hora de envio das mensagems (HH,MM):")
escolha_label.grid(row=5, column=1, padx=(10, 10), pady=(10, 10), sticky="w")

# Textbox para user digitar a hora
txtbox_hora = ctk.CTkTextbox(frametxt, width=250, height=25, corner_radius=10)
txtbox_hora.grid(row=6, column=0, padx=(10,10), pady=(5,10), sticky="w")
toggle_textbox()

# Terminal do Programa
feedback_label = ctk.CTkLabel(frametxt, text="Terminal do Programa")
feedback_label.grid(row=1, column=1, padx=(10, 10), pady=(10, 5), sticky="w")

# TextBox do Terminal
terminal_box = ctk.CTkTextbox(frametxt, corner_radius=10, state="disabled",)
terminal_box.grid(row=2, column=1, rowspan=8 ,padx=(10,10), pady=(5,10), sticky="nsew")

# Label da TXTbox numero da coluna
label_coluna = ctk.CTkLabel(frametxt, text="Digite o numero da coluna onde estão os numeros:")
label_coluna.grid(row=7, column=0, padx=(10,10), pady=(10,10), sticky="w")

# TextBox numero da coluna
txtbox_coluna = ctk.CTkTextbox(frametxt, corner_radius=10, width=50, height=25)
txtbox_coluna.grid(row=8, column=0, padx=(10,10), pady=(10,10), sticky="w")

# Botão de enviar mensagem
from Logica import enviar_mensagem

enviar_button = ctk.CTkButton(
    frametxt, 
    fg_color="green",  # Cor de fundo do botão
    hover_color="green",  # A cor do botão não mudará ao passar o mouse
    text="Enviar Mensagems", 
    command=lambda: enviar_mensagem(
        txt_box.get("0.0", "end"), 
        int(wait_time.get()), 
        tab_close_var.get(), 
        inst_msg_var.get(), 
        txtbox_hora.get("0.0", "end"),
        arquivo_img if arquivo_img else None,
        terminal_box,
        atualizar_feedback
    )
)
enviar_button.grid(row=8, column=0, padx=(100,10), pady=(10,10), sticky="w")

# Tooltip do botão
enviar_button.bind("<Enter>", lambda event: mostrar_tooltip(event, "Enviar as mensagens"))
enviar_button.bind("<Leave>", esconder_tooltip)

app.mainloop()
