import manipulaCSV as mcsv
import manipulaCarros as mcar
import datetime
import apresentacao

def diferenca_dias(d1, d2):
    d1 = datetime.strptime(d1, "%d/%m/%Y %H:%M:%S")
    d2 = datetime.strptime(d2, "%d/%m/%Y %H:%M:%S")
    return abs((d2 - d1).days * 24)

def carregar_Locacao() ->list: 
    '''
    Carrega o arquivo de Locacoes.csv numa lista
    
    Retorno
    -------
    Retorna uma lista vazia caso o arquivo não exista ou 
    uma lista de dicionários contendo os dados das locações
    '''
    lista = mcsv.carregarDados("Locacoes.csv")
    return lista

    def obterProximoId_Locacao() -> int:
        '''
    Obtém o próximo ID para cadastrar uma locacao
    Retorno
    -------
    Retorna o ID disponível para cadastro
    '''
    listaLocacoes = carregar_Locacao()
    if listaLocacoes == []:
        return 1
    return int(listaLocacoes[-1]['Identificacao']) + 1

def cadastrar_locacao(locacao : dict) -> bool :
    '''
    Rotina para cadastrar uma locacao

    Parâmetros
    ----------
    locacao: dict
        Dicionário contendo os dados da locacao

    Retorno
    -------
    Retorna True se a locacao foi cadastrada com sucesso
    '''
    listaLocacoes = mcsv.carregarDados("Locacoes.csv")
    camposLocacoes =  ["Identificacao","Identificacao_Carro","Cpf","Data_Inicial","Km_Inicial","Data_Final","Km_Final"]
    for l in listaLocacoes:
        if l['Identificacao'] == locacao['Identificacao']:
            print("Uma locação com essa identificação já existe")
            return False
    listaLocacoes.append(locacao)
    return mcsv.gravarDados('Locacoes.csv', camposLocacoes, listaLocacoes )

def excluir_Locacao(listaLocacoes : list, cpf : str ) -> bool:
    '''
    Excluir uma locacao da lista de locacoes e atualiza o arquivo CSV
    '''
    flag = False
    camposLocacoes = list(listaLocacoes[0].keys())
    for i,locacao in enumerate(listaLocacoes):
        if locacao['CPF'] ==  cpf :
            flag = True
            listaLocacoes.pop(i)
    if flag:
        mcsv.gravarDados("Locacoes.csv", camposLocacoes, listaLocacoes)
    return flag

def NovaLocacao():
    print("#"*20)
    locacao = {}
    locacao['Cpf'] = str(input("Digite o CPF do cliente:"))
    categorias = [1,2,3,4]
    categoria = 0
    while categoria not in categorias:
        apresentacao.limpaTela()
        print("#"*20)
        print("1. Econômico\n2. Intermediário\n3. Conforto\n4. Pickup")    
        print('#'*20)
        categoria = int(input("Opção -> "))
    cambios = [1,2]
    cambio = 0
    while cambio not in cambios:
        apresentacao.limpaTela()
        print("#"*20)
        print("Qual o câmbio desejado?\n")
        print("1. Manual\n2. Automático")    
        print('#'*20)
        cambio = int(input("Opção -> "))
    seguros = [1,2]
    seguro = 0
    while seguro not in seguros:
        apresentacao.limpaTela()
        print("#"*20)
        print("1. Com seguro\n2. Sem seguro")    
        print('#'*20)
        seguro = int(input("Opção -> "))
    match categoria:
        case 1:
            match cambio:
                case 1:
                    carros_disponiveis = mcar.carregar({'Categoria': 'Econômico', 'Cambio': 'Manual'}, True)
                case 2:
                    carros_disponiveis = mcar.carregar({'Categoria': 'Econômico', 'Cambio': 'Automático'}, True)
        case 2:
            match cambio:
                case 1:
                    carros_disponiveis = mcar.carregar({'Categoria': 'Intermediário', 'Cambio': 'Manual'}, True)
                case 2:
                    carros_disponiveis = mcar.carregar({'Categoria': 'Intermediário', 'Cambio': 'Automático'}, True)
        case 3:
            match cambio:
                case 1:
                    carros_disponiveis = mcar.carregar({'Categoria': 'Conforto', 'Cambio': 'Manual'}, True)
                case 2:
                    carros_disponiveis = mcar.carregar({'Categoria': 'Conforto', 'Cambio': 'Automático'}, True)
        case 4:
            match cambio:
                case 1:
                    carros_disponiveis = mcar.carregar({'Categoria': 'Pickup', 'Cambio': 'Manual'}, True)
                case 2:
                    carros_disponiveis = mcar.carregar({'Categoria': 'Pickup', 'Cambio': 'Automático'}, True)
    apresentacao.limpaTela()
    print("#"*20)
    if len(carros_disponiveis) == 0:
        print("Nenhum carro disponível")
        return False
    else:
        if seguro == 1:
            print(carros_disponiveis['Modelo','Cor', 'Diaria', 'Seguro', 'Km', 'Placa'])
        else:
            print(carros_disponiveis['Modelo','Cor', 'Diaria', 'Km', 'Placa'])
    apresentacao.EsperaEnter()
    apresentacao.limpaTela()
    locacao['Identificacao_Carro'] = int(input("Qual a identificação do carro escolhido?\n"))
    entrada = input("Data da locação (dia/mes/ano)? ")
    horario_entrada = input("Horario entrada (hh:mm): ")
    entrada = entrada + " " + horario_entrada
    locacao['Data_Inicial'] = datetime.datetime.strptime(entrada, "%d/%m/%Y %H:%M")
    camposCarro = list(carros_disponiveis[0].keys())
    achou = False
    while not(achou) :
        for carro in carros_disponiveis:
            if int(carro['Identificacao']) == Id_Carro :
                achou = True
                locacao['Km_Inicial'] = carro['Km']
        if not(achou) :
            apresentacao.limpaTela()
            print("Carro indisponível")
            Id_Carro = int(input("Digite novamente a identificação do carro: "))
    locacao['Data_Final'] = (0/0/0)
    locacao['Km_Final'] = 0
    locacao['Identificacao'] = locacao.obterProximoId_Locacao()
    cadastrar_locacao(locacao)
    #alterarDisponivel()

def EncerrarLocacao():
    apresentacao.limpaTela()
    print("#"*20)
    Identificacao = int(input("Qual a identificação da locação?"))
    print("#"*20)
    listaLocacoes = carregar_Locacao()
    camposLocacoes = list(listaLocacoes[0].keys())
    for locacoes in listaLocacoes:
        if int(locacoes['Identificacao']) == Identificacao :
            locacao = locacoes
    saida = input("Entrega da locação (dia/mes/ano)? ")
    horario_saida = input("Horario entrega (hh:mm): ")
    saida = saida + " " + horario_saida
    locacao['Data_Final'] = datetime.datetime.strptime(saida, "%d/%m/%Y %H:%M")
    locacao['Km_Final'] = input("Qual a quilometragem atual?")
    tempoDecorrido = diferenca_dias(locacao['Data_Inicial'], locacao['Data_Final'])
    listaCarros = mcar.carregar()
    camposCarro = list(listaCarros[0].keys())
    for carro in listaCarros:
        if int(carro['Identificacao']) == locacao['Identificacao_Carro'] :
            diaria = carro['Diaria']
            carro['Km'] = locacao['Km_Final']
    if tempoDecorrido <= 24:
        pagamento = diaria
    else:
        pagamento = (diaria/24)*tempoDecorrido
    print("O pagamento deve ser de R$", pagamento)
    #alterarDisponivel()