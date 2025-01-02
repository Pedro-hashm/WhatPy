import customtkinter
import csv
from customtkinter import filedialog
arquivo_img = None

# text = textbox.get("0.0", "end")  # get text from line 0 character 0 till the end
# CheckboxState = checkbox1.get() / 1 = ativa / 0 = inativa
# Pra o Slider, é só acessar a variavel: wait_time_value

app = customtkinter.CTk()
app.geometry("1280x720")

# Função do Slider
def atualizar_tempo(wait_time_value):
    tempo_label.configure(text=f"Tempo de Espera: {int(wait_time_value)}")

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
            atualizar_feedback_func=atualizar_feedback
        )

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
        ("Todos os Arquivos", "*.*")
        ]
    )

# Função do Terminal
def atualizar_feedback(mensagem, terminal_box):
    if terminal_box.winfo_exists():  # Verifica se o widget ainda existe
        terminal_box.configure(state="normal")
        terminal_box.delete("1.0", "end")
        terminal_box.insert("1.0",(mensagem))
        terminal_box.configure(state="disabled")

# Configurar linhas e colunas da janela principal
app.grid_rowconfigure(0, weight=1)  # Primeira linha expande
app.grid_rowconfigure(1, weight=1)  # Segunda linha expande
app.grid_columnconfigure(0, weight=1)  # Primeira coluna expande
app.grid_columnconfigure(1, weight=2)  # Segunda coluna expande mais

# Frame para arquivo CSV
framecsv = customtkinter.CTkFrame(app)
framecsv.grid(row=0, column=0, padx=(10, 10), pady=(10, 5), sticky="nsew")

# Config do Grid do Frame CSV
framecsv.grid_rowconfigure(0, weight=1)
framecsv.grid_columnconfigure(0, weight=1)

# Frame para imagem
frameimg = customtkinter.CTkFrame(app)
frameimg.grid(row=1, column=0, padx=(10, 10), pady=(5, 10), sticky="nsew")

# Config do Grid do Frame Img
frameimg.grid_rowconfigure(0, weight=1)
frameimg.grid_columnconfigure(0, weight=1)

# Frame para texto
frametxt = customtkinter.CTkFrame(app)
frametxt.grid(row=0, column=1, rowspan=2, padx=(10, 10), pady=(10, 10), sticky="nsew")

# Config do Grid do Frame Txt
frametxt.grid_rowconfigure(0, weight=4)  # Mais espaço para a txt_box principal
frametxt.grid_rowconfigure(1, weight=0)  # Espaço mínimo para CheckBoxes
frametxt.grid_rowconfigure(2, weight=0)  # Espaço mínimo para CheckBoxes
frametxt.grid_rowconfigure(3, weight=0)  # Espaço para Slider
frametxt.grid_rowconfigure(4, weight=0)  # Espaço mínimo para Label
frametxt.grid_rowconfigure(5, weight=0)  # Espaço pequeno para TextBox de hora
frametxt.grid_rowconfigure(6, weight=1)  # Terminal_box vai ocupar o espaço restante
frametxt.grid_columnconfigure(0, weight=1)
frametxt.grid_columnconfigure(1, weight=1)

# Botão CSV
csv_button = customtkinter.CTkButton(framecsv, text="Carregar Arquivo CSV", command=carregar_csv, height=50)
csv_button.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew")

# Botão Img
img_button = customtkinter.CTkButton(frameimg, text="Carregar Imagem", command=carregar_img, height=50)
img_button.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew")

# Caixa de Texto
txt_box = customtkinter.CTkTextbox(frametxt)
txt_box.grid(row=0, column=0, padx=(10,10), pady=(10,10), sticky="nsew", columnspan=2)

# CheckBoxes
tab_close_var = customtkinter.BooleanVar()
tab_close = customtkinter.CTkCheckBox(frametxt, text="Fechar Abas?", command=None, variable=tab_close_var)
tab_close.grid(row=1, column=0, padx=(10, 10), pady=(10,10), sticky="w")
inst_msg_var = customtkinter.BooleanVar()
inst_msg = customtkinter.CTkCheckBox(frametxt, text="Começar Imediatamente?", variable=inst_msg_var, command=toggle_textbox)
inst_msg.grid(row=2, column=0, padx=(10, 10), pady=(10,10), sticky="w")

# Label para exibir o valor do slider
wait_time_value = 10
tempo_label = customtkinter.CTkLabel(frametxt, text=f"Tempo de Espera: {wait_time_value}")
tempo_label.grid(row=3, column=0, padx=(220,10), pady=(10,10), sticky="w")

# Slider
wait_time = customtkinter.CTkSlider(frametxt, from_=1, to=40, number_of_steps=39, command=atualizar_tempo)
wait_time.grid(row=3, column=0, padx=(10,10), pady=(10,10), sticky="w")

# Textbox para exibir "Escolha quando a mensagem será enviada"
escolha_label = customtkinter.CTkLabel(frametxt, text="Digite a hora de envio das mensagems (HH,MM):")
escolha_label.grid(row=5, column=1, padx=(10, 10), pady=(10, 10), sticky="w")

# Textbox para user digitar a hora
txtbox_hora = customtkinter.CTkTextbox(frametxt, width=250, height=25, corner_radius=10)
txtbox_hora.grid(row=6, column=0, padx=(10,10), pady=(5,10), sticky="w")
toggle_textbox()

# Terminal do Programa
feedback_label = customtkinter.CTkLabel(frametxt, text="Terminal do Programa")
feedback_label.grid(row=1, column=1, padx=(10, 10), pady=(10, 5), sticky="w")

# TextBox do Terminal
terminal_box = customtkinter.CTkTextbox(frametxt, corner_radius=10, state="disabled")
terminal_box.grid(row=2, column=1, rowspan=8 ,padx=(10,10), pady=(5,10), sticky="nsew")

# Label da TXTbox numero da coluna
label_coluna = customtkinter.CTkLabel(frametxt, text="Digite o numero da coluna onde estão os numeros:")
label_coluna.grid(row=7, column=0, padx=(10,10), pady=(10,10), sticky="w")

# TextBox numero da coluna
txtbox_coluna = customtkinter.CTkTextbox(frametxt, corner_radius=10, width=50, height=25)
txtbox_coluna.grid(row=8, column=0, padx=(10,10), pady=(10,10), sticky="w")

# Botão de enviar mensagem
from Logica import enviar_mensagem
enviar_button = customtkinter.CTkButton(
    frametxt, 
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

app.mainloop()
