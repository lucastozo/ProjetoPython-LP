import manipulaCSV as mcsv
import apresentacao

def carregar(campos={}, mostrarApenasDisponiveis = False) -> list :
    '''
    Retorna uma lista de dicionários contendo carros

    Parâmetros
    ----------
    campos: dict, opcional
        Dicionário contendo os campos a serem filtrados. Se vazio, retorna todos os carros
    mostrarApenasDisponiveis: bool, opcional
        Se True, retorna apenas carros disponíveis

    Retorno
    -------
    Retorna uma lista vazia caso o arquivo não exista ou uma lista de dicionários contendo os dados dos carros

    Exemplo
    -------
    carregar() -> Retorna todos os carros
    carregar({'Categoria': 'Econômico', 'Cor': 'Preto'}, True) -> Retorna carros econômicos e pretos disponíveis
    carregar({'AnoFabricacao': '2020'}, False) -> Retorna carros fabricados em 2020 disponíveis e indisponíveis
    '''
    lista = mcsv.carregarDados("Carros.csv")
    if not lista or not campos:
        return lista
    
    carrosFiltrados = []
    for carro in lista:
        if mostrarApenasDisponiveis and (carro['Disponivel'].lower() != 'sim' and carro['Disponivel'].lower() != 's'):
            continue
        igual = True
        for campo, valor in campos.items():
            if carro.get(campo) != valor:
                igual = False
                break
        if igual:
            carrosFiltrados.append(carro)
    return carrosFiltrados

def cadastrar(carro : dict) -> bool :
    '''
    Rotina para cadastrar um carro

    Parâmetros
    ----------
    carro: dict
        Dicionário contendo os dados do carro

    Retorno
    -------
    Retorna True se o carro foi cadastrado com sucesso
    '''
    listaCarros = carregar()
    camposCarro =  ["Identificacao","Modelo","Cor","AnoFabricacao","Placa","Cambio","Categoria", "Km", "Diaria", "Seguro", "Disponivel"]
    # Verifica se o carro já existe
    for c in listaCarros:
        if c['Identificacao'] == carro['Identificacao']:
            print("Um carro com essa identificação já existe")
            return False
    listaCarros.append(carro)
    return mcsv.gravarDados('Carros.csv', camposCarro, listaCarros )

def alterar(id : int) -> bool:
    '''
    Alterar um carro da lista de carros e atualiza o arquivo CSV

    Parâmetros
    ----------
    id: int
        Identificação do carro a ser alterado

    Retorno
    -------
    Retorna True se o carro foi alterado com sucesso e False caso contrário
    '''
    listaCarros = carregar()
    if listaCarros == []:
        return False
    alterou = False
    camposCarro = list(listaCarros[0].keys())
    for carro in listaCarros:
        if int(carro['Identificacao']) == id :
            opcao = -1
            while opcao != 0:
                apresentacao.ExibirCarro(carro, mostrarIndices=True)
                print("Digite o número do campo para alterar ou 0 para sair")
                opcao = int(input("Opção -> "))
                if opcao != 0:
                    alterou = True
                    campo = list(carro.keys())[opcao-1]
                    carro[campo] = input(f"{apresentacao.saidaCamposCarro[opcao-1]}: ")
            break
    if alterou:
        mcsv.gravarDados("Carros.csv", camposCarro, listaCarros)
    return alterou

def excluir(id : int) -> bool:
    '''
    Excluir um carro da lista de carros e atualiza o arquivo CSV

    Parâmetros
    ----------
    id: int
        Identificação do carro a ser excluído

    Retorno
    -------
    Retorna True se o carro foi excluído com sucesso e False caso contrário
    '''
    listaCarros = carregar()
    if listaCarros == []:
        return False
    excluiu = False
    camposCarro = list(listaCarros[0].keys())
    for i,carro in enumerate(listaCarros):
        if int(carro['Identificacao']) == id :
            apresentacao.ExibirCarro(carro)
            confirma = input("Confirma a exclusão? (S/N) ").upper()
            if confirma == 'S':
                excluiu = True
                listaCarros.pop(i)
            break
    if excluiu:
        mcsv.gravarDados("Carros.csv", camposCarro, listaCarros)
    return excluiu

def disponibilizarCarrosParaVenda() -> bool:
    '''
    Disponibiliza carros para venda

    Retorno
    -------
    Retorna True se os carros foram disponibilizados para venda e False caso não haja carros disponíveis
    '''
    anoMaximo = 2018
    kmMinimo = 60000

    listaCarros = carregar()
    if listaCarros == []:
        return False
    carrosVenda = []
    idCarrosExcluir = []
    for carro in listaCarros:
        if carro['Disponivel'] == 'Sim' and (int(carro['AnoFabricacao']) <= anoMaximo or int(carro['Km']) >= kmMinimo):
            carrosVenda.append(carro)
            idCarrosExcluir.append(int(carro['Identificacao']))
    if carrosVenda == []:
        return False
    camposCarro = list(listaCarros[0].keys())
    mcsv.gravarDados("Vendas.csv", camposCarro, carrosVenda)
    for id in idCarrosExcluir:
        excluir(listaCarros, id)
    return True

def listarCarrosPorCategoria(categoria : str) -> list:
    '''
    Lista os carros DISPONÍVEIS PARA LOCAÇÃO de uma determinada categoria

    Parâmetros
    ----------
    categoria: str
        Categoria do carro

    Retorno
    -------
    Retorna uma lista de dicionários contendo os carros da categoria disponíveis para locação
    '''
    carrosCategoria = carregar({'Categoria': categoria}, True)
    if carrosCategoria == []:
        print("Nenhum carro disponível nessa categoria")
    else:
        for carro in carrosCategoria:
            apresentacao.ExibirCarro(carro)
    return carrosCategoria

def obterProximoId() -> int:
    '''
    Obtém o próximo ID para cadastrar um carro

    Retorno
    -------
    Retorna o ID disponível para cadastro
    '''
    listaCarros = carregar()
    if listaCarros == []:
        return 1
    return int(listaCarros[-1]['Identificacao']) + 1