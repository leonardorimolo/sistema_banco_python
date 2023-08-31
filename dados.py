import json

#guarda os dados do dicionário em json
def guardar_arquivo(dicionario):
    
    with open('banco-do-banco.json','w') as arquivo:
        
        json.dump(dicionario,arquivo, indent=4)
        


#le o arquivo json e retorna o dicionário
def ler_arquivo():
    try:
        with open('banco-do-banco.json','r') as arquivo:
            
            dictionary = json.load(arquivo)
            
            return dictionary
    except FileNotFoundError:
        return 1
        