import os
from sys import exit

saldo = 2.0
email = "usuario@gmail.com"
senha = "1234" 

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def bemvindo():
    print("Bem-vindo ao Banco Caixa Universal")
    resposta_1 = input("Você já tem conta com a gente? ").lower().strip()
    if resposta_1 in ["nao", "n", "não"]:
        resposta_2 = input("Gostaria de fazer agora? ").lower().strip()

        if resposta_2 in ["sim", "s"]:
            cadastro()
            tela_inicial()
        else:
            print("Sem problemas! Se mudar de ideia estamos à disposição")
            print("Saindo...")
            exit()

    else:
        print("Ótimo! Vamos acessar sua conta.")
        resposta_3 = input("Email: ")
        resposta_4 = input("Senha: ")
        if resposta_3 == email and resposta_4 == senha:
            limpar_tela()
            print("Bem-vindo de volta, como podemos ajudar?")
            tela_inicial()
        else:
            limpar_tela()
            print("Email ou senha incorretos, tente novamente!")
            bemvindo()
        

def cadastro():
    global email, senha
    print("Que bom que quer se juntar a nós!")
    nome     = input("Qual seu nome completo? ")
    cpf      = input("Qual o seu CPF? ")
    email    = input("Qual sera seu endereço de e-mail? ")
    telefone = input("Telefone para contato: ")
    senha    = input("vamos criar uma senha de acesso: ")
    print(f"Tudo pronto, seu Cadastro está concluído!")
    limpar_tela()

def tela_inicial():
    print("1 -- Saldo")
    print("2 -- Transferencia")
    print("3 -- Depósito")
    print("4 -- Saque")
    print("5 -- Configuração")
    escolha = input("")
    if escolha == "1":
        limpar_tela()
        print(f"O seu saldo é de R${saldo:.2f}")
        tela_inicial()
    elif escolha == "2":
        if saldo <= 0:
            limpar_tela()
            print("Você não pode fazer transferência, pois não tem saldo")
            tela_inicial()
        else:
            limpar_tela()
            print("Qual o valor?")

bemvindo()
