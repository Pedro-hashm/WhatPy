import pywhatkit
import csv
phonesl = list()

# Abre o arquivo csv especificado e lê ele

def get_phones(arquivo_csv, row_number, terminal_box, atualizar_feedback_func):
    with open(arquivo_csv) as csvfile:
        global phonesl
        reader = csv.reader(csvfile)
        phones = []
        
        for row in reader:
            phone = "+55" + row[row_number]
            phones.append(phone)

        phones.pop(0)
        phonesl = phones
        atualizar_feedback_func(f"Arquivo CSV carregado com sucesso! {len(phones)} numeros foram capturados: {phones}", terminal_box)

cont = 0

def enviar_mensagem(texto, tempo_espera, tab_fechar, começar_imd, hora_começo, imagem, terminal_box, atualizar_feedback_func):

    # Tratando Tempo_Espera

    if começar_imd != True:
        nova_hora_começo = str()
        hora = int()
        minuto = int()
        nova_hora_começo = hora_começo.replace(",", "").strip()
        hora = int(nova_hora_começo[0:2])
        minuto = int(nova_hora_começo[2:4])
    


    # Se começar imediatamente for True, enviar Mensagem instantaneas, se não, enviar mensagem com hora e minuto

    for phone in phonesl:
        if começar_imd == True and imagem == None:
            print(tempo_espera)
            pywhatkit.sendwhatmsg_instantly(phone, texto, tempo_espera, tab_fechar, 5)
        else:
            print(hora)
            print(minuto)
            pywhatkit.sendwhatmsg(phone, texto, hora, minuto, tempo_espera, tab_fechar, 5)
    atualizar_feedback_func('mensagem enviada', terminal_box)
        

    # print(phonesl)

    # lista, msg, hora_start, minuto_start, tempo_espera, tab_fechar, tempo_fechar
    #pywhatkit.sendwhatmsg(phone, "oi", 23, 60, 15, True, 3)

    # lista, msg, tempo_espera, tab_fechar, tempo_fechar
    #pywhatkit.sendwhatmsg_instantly(phone, "oi", 15, True, 3)

    #pywhatkit.sendwhatmsg_instantly(phone, texto, wait_time=tempo_espera, tab_close=tab_fechar, )

