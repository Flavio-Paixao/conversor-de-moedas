import customtkinter
from pegar_moedas import nomes_moedas, conversoes_disponiveis
from pegar_cotacao import pegar_cotacao_moeda

# Criar e configurar a janela:
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry("500x500")

dic_conversoes_disponiveis = conversoes_disponiveis()

#dic_conversoes_disponiveis["USD"] => ["BRL", "CAD", "BTC", "AUD"]
# Criar botões, textos e outros elementos:
titulo = customtkinter.CTkLabel(janela, text="Conversor de Moedas", font=("", 20))
texto_moeda_origem = customtkinter.CTkLabel(janela, text="Selecione a moeda de origem")
texto_moeda_destino = customtkinter.CTkLabel(janela, text="Selecione a moeda de destino")

def carregar_moedas_destino(moeda_selecionada):
    lista_moedas_destino = dic_conversoes_disponiveis[moeda_selecionada]
    campo_moeda_destino.configure(values=lista_moedas_destino)
    campo_moeda_destino.set(lista_moedas_destino[0])

campo_moeda_origem = customtkinter.CTkOptionMenu(janela, values=list(dic_conversoes_disponiveis.keys()), command=carregar_moedas_destino)

campo_moeda_destino = customtkinter.CTkOptionMenu(janela, values=["Selecione uma moeda de origem"])

def converter_moeda():
    moeda_origem = campo_moeda_origem.get()
    moeda_destino = campo_moeda_destino.get()
    if moeda_origem and moeda_destino:
        cotacao = pegar_cotacao_moeda(moeda_origem, moeda_destino)
        texto_cotacao_moeda.configure(text=f"1 {moeda_origem} = {cotacao} {moeda_destino}")


botao_converter = customtkinter.CTkButton(janela, text="Converter", command=converter_moeda)

lista_moedas = customtkinter.CTkScrollableFrame(janela)

moedas_disponiveis = customtkinter.CTkLabel(janela)

texto_cotacao_moeda = customtkinter.CTkLabel(janela, text="")


moedas_disponiveis = nomes_moedas()
{"BRL": "Real Brasileiro", "USD": "Dólar Americano"}
for codigo_moeda in moedas_disponiveis:
    nomes_moedas = moedas_disponiveis[codigo_moeda]
    texto_moeda = customtkinter.CTkLabel(lista_moedas, text=f"{codigo_moeda}: {nomes_moedas}")
    texto_moeda.pack()


# Colocar os elementos na tela:
titulo.pack(padx=10, pady=10)
texto_moeda_origem.pack(padx=10, pady=10)
campo_moeda_origem.pack(padx=10)
texto_moeda_destino.pack(padx=10, pady=10)
campo_moeda_destino.pack(padx=10)
botao_converter.pack(padx=10, pady=10)
texto_cotacao_moeda.pack(padx=10, pady=10)
lista_moedas.pack(padx=10, pady=10)


janela.mainloop()











