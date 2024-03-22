from os import system, name
import manipulaCarros as mcar

# saidaCampos é uma lista para mostrar os campos de uma forma mais amigável
saidaCamposCarro = ["Identificação", "Modelo", "Cor", "Ano de Fabricação", "Placa", "Câmbio", "Categoria", "Km", "Diária", "Seguro", "Disponível"]

#################################################################

def EsperaEnter():
    '''
    Função que aguarda o usuário pressionar a tecla enter
    '''
    input("Pressione enter para continuar")

def limpaTela():
    '''
    Limpa a tela de acordo com o systema operacional
    '''
    if name == 'nt':
        _ = system("cls")
    else:
        _ = system("clear")       

def MenuPrincipal() -> str :
    '''
    Exemplo de Menu principal para o sistema
    
    Retorno    
    -------
    Retorna escolha do usuário

    '''
    opcoes = [1,2,3,9]
    opcao = 0
    while opcao not in opcoes:
        limpaTela()
        print("#"*20)
        print("1. Locações\n2. Clientes\n3. Carros\n9. Sair")    
        print('#'*20)
        opcao = int(input("Opção -> "))            
    return opcao

def MenuLocacoes() -> str:
    '''
    Menu de locações

    Retorno
    -
    Retorna escolha do usuário
    '''

    opcoes = [1,2,3,9]
    opcao = 0
    while opcao not in opcoes:
        limpaTela()
        print("#"*20)
        print("1. Nova locação\n2. Finalizar locação\n3. Relatório de carros locados\n9. Sair")
        print("#"*20)
        opcao = int(input("Opção -> "))
    return opcao

def MenuClientes() -> str:
    '''
    Menu de clientes

    Retorno
    -------
    Retorna escolha do usuário
    '''
    opcoes = [1,2,3,4,9]
    opcao = 0
    while opcao not in opcoes:
        limpaTela()
        print("#"*20)
        print("1. Cadastrar cliente\n2. Atualizar informações\n3. Excluir cliente\n4. Localizar locações\n9. Sair")
        print("#"*20)
        opcao = int(input("Opção -> "))
    return opcao

def MenuCarros() -> str:
    '''
    Menu de carros

    Retorno
    -------
    Retorna escolha do usuário
    '''
    opcoes = [1,2,3,4,5,9]
    opcao = 0
    while opcao not in opcoes:
        limpaTela()
        print("#"*20)
        print("1. Cadastrar carro\n2. Atualizar informações\n3. Excluir carro\n4. Disponibilizar carros para venda\n5. Carros por categoria\n9. Sair")
        print("#"*20)
        opcao = int(input("Opção -> "))
    return opcao

def CadastrarCliente() -> dict :
    '''
    Procedimento que mostra os campos para cadastramento de um cliente
    
    Retorno
    -------
    Retorna um dicionário com as informações de um cliente    
    '''
    print("#"*30)
    print("Cadastramento de um novo cliente ")
    l = ["CPF","Nome","Nascimento","Idade","Endereço","Cidade","Estado"]
    cliente = {}
    for campo in l:
        cliente[campo] = input(f"{campo}:")
        print("#"*30)
    return cliente 

def CadastrarCarro() -> dict:
    '''
    Procedimento que mostra os campos para cadastramento de um carro
    
    Retorno
    -------
    Retorna um dicionário com as informações de um carro    
    '''
    limpaTela()
    print("Cadastramento de um novo carro ")
    l = ["Identificacao","Modelo","Cor","AnoFabricacao","Placa","Cambio","Categoria", "Km", "Diaria", "Seguro", "Disponivel"]
    
    carro = {}
    for campo in l:
        if campo == "Identificacao":
            carro[campo] = mcar.obterProximoId()
        else:
            carro[campo] = input(f"{saidaCamposCarro[l.index(campo)]}: ")
    return carro

def ExibirCarro(carro : dict, campos=None, mostrarIndices = False):
    '''
    Procedimento que exibe as informações de um carro

    Parâmetros
    ----------
    carro : dict
        Dicionário com as informações do carro
    campos : list, opcional
        Lista com os campos a serem exibidos
    mostrarIndices : bool, opcional
        Exibir os índices dos campos

    Exemplo
    -------
    ExibirCarro(carro, [Identificacao, Modelo, Cor, AnoFabricacao]) # Exibe apenas os campos Identificacao, Modelo, Cor e AnoFabricacao
    ExibirCarro(carro, mostrarIndices=True) # Exibe todos os campos com os índices
    '''
    limpaTela()
    print("#"*30)
    print("Informações do carro")
    for indice, item in enumerate(carro.items(), start=1):
        chave, valor = item
        if campos is None or chave in campos:
            if mostrarIndices:
                print(f"{indice}. {saidaCamposCarro[list(carro.keys()).index(chave)]}: {valor}")
            else:
                print(f"{saidaCamposCarro[list(carro.keys()).index(chave)]}: {valor}")
    print("#"*30)
    print()