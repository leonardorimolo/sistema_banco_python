from dados import *

"""
GESTAO DA CONTA:
criar_conta()
buscar_conta()
atualizar_conta()
deletar_conta()
"""

# CRIAR CONTA:
def criar_conta(nome, limite, cpf, email_correntista):
    nome_usuario = nome
    limite_usuario = float(limite)
    email_correntista = email_correntista

    print(cpf)

    # Criar um novo usuário
    novo_usuario = {
                "nome": nome_usuario,
                "saldo": "0",
                "limite": limite_usuario,
                "cpf": cpf,
                "email_correntista": email_correntista        
                }
    
    # pegar os dados do banco
    usuarios = ler_arquivo()

    if usuarios == 1:
        guardar_arquivo({0: novo_usuario,})
    else:
        # Calcular ID
        id = len(usuarios)

        # Adiciona o usuário na base         
        usuarios[id] = novo_usuario 

        # Atualiza a base de dados
        guardar_arquivo(usuarios)



# BUSCAR CONTA:
def buscar_conta(usuario_id="-1", nome="nenhum", cpf="nenhum"):
    
    # Ler arquivo
    dados = ler_arquivo()
    if dados == 1:
        return 50 # Nenhum usuário dentro do banco
    
    # Verificando qual opcao de busca o corretor selecionou
    if usuario_id != "-1":
        usuario_selecionado = buscar_conta_por_id(usuario_id, dados)
    elif nome != "nenhum":
        usuario_selecionado = buscar_conta_por_nome(nome, dados)
    elif cpf != "nenhum":
        usuario_selecionado = buscar_conta_por_cpf(cpf, dados)

    return usuario_selecionado

def buscar_conta_por_id(usuario_id, dados):
    usuario_encontrado = "-1"

    for id in dados:
        if id == usuario_id:
            usuario_encontrado = id
            
    if usuario_encontrado == "-1":
        return 3
    else:
        return dados[usuario_encontrado]
        
def buscar_conta_por_nome(nome, dados):
    usuario_encontrado = "-1"

    for id in dados:
        if dados[id]["nome"] == nome:
            usuario_encontrado = id

    if usuario_encontrado == "-1":
        return 3
    else:
        return dados[usuario_encontrado]
    

def buscar_conta_por_cpf(cpf, dados):
    usuario_encontrado = "-1"

    for id in dados:
        if dados[id]["cpf"] == cpf:
            usuario_encontrado = id

    if usuario_encontrado == "-1":
        return 3
    else:
        return dados[usuario_encontrado]



# ATUALIZAR CONTA:
def atualizar_conta(conta, tipo, troca):
    erro = 0
    troca = float(troca)

    match tipo:
        case "limite":
            conta["limite"] = troca

        case "saque":
            erro = sacar(conta, troca)
        
        case "deposito":
            erro = depositar(conta, troca)

    # Verifica se nao deu erro durante a atualizacao:
    if erro != 0:
        return erro
    
    # Atualizando dados
    dados = ler_arquivo()
    if dados == 1:
        return 50 # Nenhum usuário encontrado no banco
    
    for id in dados:
        if dados[id]["cpf"] == conta["cpf"]:
            dados[id] = conta

    guardar_arquivo(dados)
    return 0

def sacar(conta, valor):
    if valor < 0:
        return 1

    saldo_atual = float(conta["saldo"])
    limite_atual = float(conta["limite"])

    credito = saldo_atual + limite_atual

    if credito >= valor:
        if valor <= saldo_atual:
            conta["saldo"] = str(saldo_atual - valor)
        else:
            limite_a_usar = valor - saldo_atual
            conta["saldo"] = "0"
            conta["limite"] = str(limite_atual - limite_a_usar)
        return 0  # Saque bem-sucedido
    else:
        return 2  # Crédito insuficiente

def depositar(conta, valor):
    if valor < 0:
        return 1 # Está tentando depositar um valor negativo
    else:
        conta["saldo"] = str(float(conta["saldo"]) + valor)
        return 0


# DELETAR CONTA:
def deletar_conta(conta):
    dados = ler_arquivo()
    
    if dados == 1:
        return 50  # Nenhum usuário encontrado no banco
        
    for id in dados:
        print("dados id cpf: ",dados[id]["cpf"])
        if dados[id]["cpf"] == conta["cpf"]:
            dados.pop(id)
            break
    
    
    guardar_arquivo(dados)
    return 0
