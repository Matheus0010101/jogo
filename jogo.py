import tkinter as tk

# Funções do jogo

def iniciar_jogo():
    mensagem.config(text="Você está em uma aventura na floresta.\nSua jornada começa em uma bifurcação.")
    criar_botoes(["esquerda", "direita", "colina"], escolha_bifurcacao)

def escolha_bifurcacao():
    mensagem.config(text="Você deseja ir para a esquerda, para a direita, ou subir a colina?")
    criar_botoes(["esquerda", "direita", "colina"], executar_escolha_bifurcacao)

def executar_escolha_bifurcacao(escolha):
    if escolha == "esquerda":
        mensagem.config(text="Você segue pelo caminho da esquerda e encontra uma cabana abandonada.")
        criar_botoes(["mapa", "espada", "sair"], escolha_cabana)
    elif escolha == "direita":
        mensagem.config(text="Você segue pelo caminho da direita e se depara com uma cachoeira majestosa.")
        criar_botoes(["nadar", "voltar"], escolha_cachoeira)
    elif escolha == "colina":
        mensagem.config(text="Você decide subir a colina e avista uma montanha misteriosa à distância.")
        criar_botoes(["entrar", "voltar"], escolha_montanha)

def escolha_cabana(escolha):
    if escolha == "mapa":
        mensagem.config(text="Você pega o mapa e sai da cabana.\nO mapa mostra um atalho para fora da floresta. Você escapa em segurança.")
        fim_jogo()
    elif escolha == "espada":
        mensagem.config(text="Você pega a espada e sai da cabana.\nCom a espada em mãos, você enfrenta alguns monstros na floresta.\nApós uma batalha difícil, você consegue sair da floresta.")
        fim_jogo()
    elif escolha == "sair":
        mensagem.config(text="Você decide não pegar nada e sai da cabana.\nEnquanto anda pela floresta, você encontra um grupo de viajantes amigáveis.\nEles te ajudam a encontrar a saída da floresta.")
        fim_jogo()

def escolha_cachoeira(escolha):
    if escolha == "nadar":
        mensagem.config(text="Você nada no lago e encontra uma passagem secreta atrás da cachoeira.\nA passagem leva você para fora da floresta. Parabéns, você escapou!")
        fim_jogo()
    elif escolha == "voltar":
        executar_escolha_bifurcacao("direita")

def escolha_montanha(escolha):
    if escolha == "entrar":
        mensagem.config(text="Você entra na caverna escura.\nDentro da caverna, você encontra um enigma antigo que precisa resolver para continuar.")
        criar_botoes(["resolver", "voltar"], resolver_enigma)
    elif escolha == "voltar":
        executar_escolha_bifurcacao("colina")

def resolver_enigma(escolha):
    if escolha == "resolver":
        resposta = entrada_enigma.get().lower()
        if resposta == "segredo":
            mensagem.config(text="Você resolve o enigma e encontra um tesouro escondido!\nCom o tesouro em mãos, você sai da caverna e da floresta com riquezas inimagináveis.")
            fim_jogo()
        else:
            mensagem.config(text="Você não conseguiu resolver o enigma. Tente novamente.")
            entrada_enigma.delete(0, tk.END)

def criar_botoes(opcoes, funcao):
    for opcao in opcoes:
        botao = tk.Button(root, text=opcao, command=lambda escolha=opcao: funcao(escolha))
        botao.pack()

# Configuração da janela Tkinter

root = tk.Tk()
root.title("Aventura na Floresta")

mensagem = tk.Label(root, text="", wraplength=400)
mensagem.pack()

entrada_enigma = tk.Entry(root)
entrada_enigma.pack()

iniciar_jogo()
