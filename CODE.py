from sys import exit

saldo = 0.0
depo  = 0
saque = 0

def bemvindo():
    print("Bem vindo ao Banco Caixa Universal")
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
        tela_inicial()
        

def cadastro():
    print("Que bom que quer se juntar a nós!")
    nome     = input("Qual seu nome completo? ")
    cpf      = input("Qual o seu CPF? ")
    email    = input("Qual sera seu endereço de e-mail? ")
    telefone = input("Telefone para contato: ")
    senha    = input("vamos criar uma senha de acesso: ")
    print(f"Tudo pronto, seu Cadastro está concluído!")

def tela_inicial():
    print("1 -- Ver Saldo")
    print("2 -- Fazer Transferencia")
    print("3 -- Fazer Depósito")
    print("4 -- Saque")
    escolha = input("Escolha qual opção quer fazer ")
    if escolha == "1":
        if saldo <= 0:
            print(f"O seu saldo é de R${saldo}")
            tela_inicial()
    elif escolha == "2":
        if saldo <= 0:
            print("Você não pode fazer transferência, pois não tem saldo")
            tela_inicial()
        else:
            print("Quanto gostaria transferir?")

        

        




bemvindo()
