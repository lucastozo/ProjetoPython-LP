import manipulaCSV as mcsv
import apresentacao

def carregar() -> list :
    '''
    Carrega o arquivo de Carro.csv numa lista
    
    Retorno
    -------
    Retorna uma lista vazia caso o arquivo não exista ou 
    uma lista de dicionários contendo os dados dos clientes
    '''
    lista = mcsv.carregarDados("Carros.csv")
    return lista


def cadastrar( listaCarros : list) -> bool :
    '''
    Rotina para cadastrar um carro

    Parâmetros
    ----------
    listaCarros: Lista atual dos carros

    Retorno
    -------
    Retorna True se o carro foi cadastrado com sucesso
    '''
    camposCarro =  ["Identificacao","Modelo","Cor","AnoFabricacao","Placa","Cambio","Categoria", "Km", "Diaria", "Seguro", "Disponivel"]
    carro = apresentacao.CadastrarCarro()
    # Verifica se o carro já existe
    for c in listaCarros:
        if c['Identificacao'] == carro['Identificacao']:
            print("Um carro com essa identificação já existe")
            return False
    listaCarros.append(carro)
    return mcsv.gravarDados('Carros.csv', camposCarro, listaCarros )

def alterar( listaCarros : list, id : int ) -> bool:
    '''
    Alterar um carro da lista de carros e atualiza o arquivo CSV
    '''
    if listaCarros == []:
        return False
    encontrou = False
    camposCarro = list(listaCarros[0].keys())
    for carro in listaCarros:
        if int(carro['Identificacao']) == id :
            encontrou = True
            opcao = -1
            while opcao != 0:
                apresentacao.ExibirCarro(carro, True)
                print("Digite o número do campo para alterar ou 0 para sair")
                opcao = int(input("Opção -> "))
                if opcao != 0:
                    campo = list(carro.keys())[opcao-1]
                    carro[campo] = input(f"{apresentacao.saidaCamposCarro[opcao-1]}: ")
            break
    if encontrou:
        mcsv.gravarDados("Carros.csv", camposCarro, listaCarros)
    return encontrou

def excluir(listaCarros : list, id : int ) -> bool:
    '''
    Excluir um carro da lista de carros e atualiza o arquivo CSV
    '''
    if listaCarros == []:
        return False
    encontrou = False
    camposCarro = list(listaCarros[0].keys())
    for i,carro in enumerate(listaCarros):
        if int(carro['Identificacao']) == id :
            encontrou = True
            listaCarros.pop(i)
    if encontrou:
        mcsv.gravarDados("Carros.csv", camposCarro, listaCarros)
    return encontrou