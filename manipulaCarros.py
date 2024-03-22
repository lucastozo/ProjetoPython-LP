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
    if campos == {}:
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

def disponibilizarCarrosParaVenda(listaCarros : list) -> bool:
    '''
    Disponibiliza carros para venda

    Parâmetros
    ----------
    listaCarros: Lista atual dos carros

    Retorno
    -------
    Retorna True se os carros foram disponibilizados para venda e False caso não haja carros disponíveis
    '''
    carrosVenda = []
    idCarrosExcluir = []
    for carro in listaCarros:
        if carro['Disponivel'] == 'Sim' and (int(carro['AnoFabricacao']) <= 2018 or int(carro['Km']) >= 60000):
            carrosVenda.append(carro)
            idCarrosExcluir.append(int(carro['Identificacao']))
    if carrosVenda == []:
        return False
    camposCarro = list(listaCarros[0].keys())
    mcsv.gravarDados("Vendas.csv", camposCarro, carrosVenda)
    for id in idCarrosExcluir:
        excluir(listaCarros, id)
    return True

def listarCarrosPorCategoria(listaCarros : list, categoria : int) -> list:
    '''
    Lista os carros DISPONÍVEIS PARA LOCAÇÃO de uma determinada categoria

    Parâmetros
    ----------
    listaCarros: Lista atual dos carros
    categoria: Escolha da categoria do carro

    Retorno
    -------
    Retorna uma lista de dicionários contendo os carros da categoria disponíveis para locação
    '''
    categorias = ['Econômico', 'Intermediário', 'Conforto', 'Pickup']
    categoriaStr = categorias[categoria-1]
    carrosCategoria = []
    for carro in listaCarros:
        if carro['Categoria'] == categoriaStr and (carro['Disponivel'] == 'Sim' or carro['Disponivel'] == 'sim' or carro['Disponivel'] == 'S' or carro['Disponivel'] == 's'):
            carrosCategoria.append(carro)
    if carrosCategoria == []:
        print("Nenhum carro disponível nessa categoria")
    else:
        for carro in carrosCategoria:
            apresentacao.ExibirCarro(carro)
    return carrosCategoria