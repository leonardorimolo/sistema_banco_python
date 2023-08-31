from dados import *
from usuarios import *
from sys import exit

def bem_vindo():
    print()#Espaçamento
    print()#Espaçamento
    print("------ Bem vindo ao banco da CC -----")
    interface_do_usuario()


def interface_do_usuario():
        
    print("""
        1 - Criar nova conta
        2 - Buscar uma conta
        3 - Atualizar uma conta
        4 - Deletar uma conta
        10 - Sair
          """)
    
    escolha = escolher(["1", "2", "3", "4", "10"])
    
    match escolha:
        case "1":
            criar_conta_interface()
            print() #Espaçamento
            interface_do_usuario()
             
        case "2":
            buscar_conta_interface()
            print() #Espaçamento
            interface_do_usuario()
        
        case "3":
            atualizar_conta_interface()
            print() #Espaçamento
            interface_do_usuario()


        case "4":
            deletar_conta_interface()
            print() #Espaçamento
            interface_do_usuario()

        
        

def criar_conta_interface():
            nome_usuario = input("Digite o nome da pessoa que deseja cadastrar: ")
            email_correntista = input(f"Digite o email de {nome_usuario}: ")
            cpf = input(f"Digite o CPF de {nome_usuario}: ")
            limite = input("Digite o limite que deseja conceder: ")
            
            criar_conta(nome = nome_usuario,limite = limite,cpf = cpf,email_correntista = email_correntista)
            

def buscar_conta_interface():
    opcoes ="""
            1 - Buscar conta por ID
            2 - Buscar conta por nome
            3 - Buscar conta por cpf    
            10 - Sair
            """
    print(opcoes)
    
    escolha = escolher(["1", "2", "3", "10"])

    match escolha:
        case "1":
            escolha_busca = input("Digite o id do usuário que deseja buscar: ")
            busca = buscar_conta(usuario_id = escolha_busca)   
        
        case "2":
            escolha_busca = input("Digite o nome do correntista que deseja buscar: ")
            busca = buscar_conta(nome = escolha_busca)
            
        case "3":
            escolha_busca = input("Digite o cpf do correntista que deseja buscar: ")
            busca = buscar_conta(cpf = escolha_busca)
    
    print() #Espaçamento       
    if busca == 3:
        print("Usuário não encontrado!")
        buscar_conta_interface()
    elif busca == 50:
        print("Nenhum usuário encontrado na base de dados!")
    else:

        # Verifica se essa foi era a conta que usuário deseja
        print(dados_formatados_usuario(busca))
        print() #Espaçamento
        conta_certa = input("Essa é a conta que voce deseja [s] [n]? ")
        if conta_certa != "s":
            buscar_conta_interface()
        else:
            return busca
    
            
def atualizar_conta_interface():
    
    print("Escolha a conta que deseja atualizar!")
    
    conta = buscar_conta_interface()
    
    opcoes =("""
            1 - Atualizar o limite da conta
            2 - Sacar
            3 - Depositar
            10 - Sair
            """)
    print(opcoes)

    escolha = escolher(["1", "2", "3", "10"])
    
    try:
        match escolha:
            case "1":
                limite = input("Digite o novo limite da conta: ")
                erro = atualizar_conta(conta = conta, tipo = "limite", troca = limite)
            
            case "2":
                saque = input("Digite o valor que deseja sacar na conta: ")
                erro = atualizar_conta(conta = conta, tipo = "saque", troca = saque)
                
            case "3":
                deposito = input("Digite o valor que deseja depositar na conta: ")
                erro = atualizar_conta(conta = conta, tipo = "deposito", troca = deposito)
    
    except ValueError:
        print() #Espaçamento
        print("Parece que voce inseriu algo que nao deveria, por favor, tente novamente")
        atualizar_conta_interface()

    erros(erro)


# em desenvolvimento:
def deletar_conta_interface():
    print("Escolha a conta que deseja deletar!")


    conta = buscar_conta_interface()
    if conta == 50:
        print()#Espaçamento
        print("Nenhum usuário encontrado no banco de dados")
        interface_do_usuario()
    
    opcoes =("""
            1 - Deletar Conta!
            10 - Sair
            """)
    print(opcoes)

    escolha = escolher(["1","10"])
    
    match escolha:
        case "1":
            deletar_conta(conta)
            print("A conta foi do Deletada com sucesso!")


def dados_formatados_usuario(usuario):
    return f"""
nome : {usuario["nome"]}
saldo: {usuario["saldo"]}
limite: {usuario["limite"]}
cpf: {usuario["cpf"]}
email correntista: {usuario["email_correntista"]}
"""

def escolher(alternativas):
    escolha = input("Digite a sua escolha: ")
    
    while escolha not in alternativas:
        escolha = input("Digite uma escolha válida: ")

    if escolha == "10":
        exit("Saindo do programa")

    return escolha


def erros(erro):
    if erro != 0:
        match erro:
            case 50:
                print("Nenhum usuário encontrado na base de dados!")
            case 1:
                print("Voce tentou sacar ou depositar um valor negativa, por favor repita a operacao")
            case 2:
                print("Crédito insuficiente")
            case 3:
                print("Usuário nao encontrado")
