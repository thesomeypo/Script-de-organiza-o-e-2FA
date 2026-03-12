import pyotp
import os

SENHA_PADRAO = "SUASENHA"
NOME_ARQUIVO = "contas.txt"

while True:
    # Essa parte pega o emails
    email = input("Insira o email: ")
    print("email salvo")

    # essa parte é responsavel por pedir a 2fa e adicionar a variavel raw_2fa
    raw_2fa = input("🔑 Cole a chave 2FA:")

    # essa parte tira os espaços e deixa em maiusculo
    chave_limpa = raw_2fa.replace(" ", "").upper()

    # Essa parte sera responsavel por pegar a chave limpa da etapa anterior e usa-la para gerar o codigo otp
    totp = pyotp.TOTP(chave_limpa)
    codigo_6_digitos = totp.now() # Aqui é onde sai o codigo valido por 30 segundos
    print(codigo_6_digitos)
    # Cria a linha organizada do jeito que preciso
    # O \n no final serve para pular a linha
    linha = f"{email},{SENHA_PADRAO}:{chave_limpa}\n"

    with open(NOME_ARQUIVO, "a") as arquivo:
        arquivo.write(linha)
