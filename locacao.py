from pydoc import cli
import manipulaCSV as mcsv
import manipulaCarros as mcar
import datetime
import apresentacao
import manipulaClientes as mcli

def diferenca_dias(data1, data2):
    tempo_decorrido = data2 - data1
    if (tempo_decorrido.days > 0 ):
        [dummy, horas] =  str(tempo_decorrido).split(',')
        [horas, minutos, segundos] = horas.split(":")    
    else:
        [horas, minutos, segundos] = str(tempo_decorrido).split(":")
    dias = int(tempo_decorrido.days)
    return dias

def diferenca_horas(data1, data2):
    tempo_decorrido = data2 - data1
    if (tempo_decorrido.days > 0 ):
        [dummy, horas] =  str(tempo_decorrido).split(',')
        [horas, minutos, segundos] = horas.split(":")    
    else:
        [horas, minutos, segundos] = str(tempo_decorrido).split(":")   
    horas = int((tempo_decorrido/datetime.timedelta(hours=1))%24)
    return horas
  

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
            carrosExibidos = ['Modelo','Cor', 'Diaria', 'Seguro', 'Km', 'Placa']
            for carro in carros_disponiveis:
                apresentacao.ExibirCarro(carro, carrosExibidos )
        else:
            carrosExibidos = ['Modelo','Cor', 'Diaria', 'Km', 'Placa']
            for carro in carros_disponiveis:
                apresentacao.ExibirCarro(carro, carrosExibidos )
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
            if int(carro['Identificacao']) == locacao['Identificacao_Carro'] :
                achou = True
                locacao['Km_Inicial'] = carro['Km']
        if not(achou) :
            apresentacao.limpaTela()
            print("Carro indisponível")
            Id_Carro = int(input("Digite novamente a identificação do carro: "))
    locacao['Data_Final'] = datetime.datetime(1, 1, 1)
    locacao['Km_Final'] = 0
    locacao['Identificacao'] = obterProximoId_Locacao()
    cadastrar_locacao(locacao)

def EncerrarLocacao():
    apresentacao.limpaTela()
    print("#"*20)
    Identificacao = int(input("Qual a identificação da locação?"))
    print("#"*20)
    listaLocacoes = carregar_Locacao()
    camposLocacoes = list(listaLocacoes[0].keys())
    for locacoes in listaLocacoes:
        if int(locacoes['Identificacao']) == int(Identificacao) :
            locacao = locacoes
    saida = input("Entrega da locação (dia/mes/ano)? ")
    horario_saida = input("Horario entrega (hh:mm): ")
    saida = saida + " " + horario_saida
    locacao['Data_Final'] = datetime.datetime.strptime(saida, "%d/%m/%Y %H:%M")
    locacao['Km_Final'] = input("Qual a quilometragem atual?")
    mcsv.gravarDados("Locacoes.csv", camposLocacoes, listaLocacoes)
    data_inicial = datetime.datetime.strptime(locacao['Data_Inicial'], "%Y-%m-%d %H:%M:%S")
    horas = diferenca_horas(data_inicial, locacao['Data_Final'])
    dias = diferenca_dias(data_inicial, locacao['Data_Final'])
    listaCarros = mcar.carregar()
    camposCarro = list(listaCarros[0].keys())
    diaria = 0
    for carro in listaCarros:
        if int(carro['Identificacao']) == int(locacao['Identificacao_Carro']) :
            diaria = float(carro['Diaria'])
            carro['Km'] = locacao['Km_Final']
            mcsv.gravarDados("Carros.csv", camposCarro, listaCarros)   
    if dias <=0:
        pagamento = diaria
    else:
        pagamento = diaria*dias + (diaria*horas/24)
    print("O pagamento deve ser de R$", pagamento)
    
def RelatórioLocação() -> bool:
    apresentacao.limpaTela()
    print("#"*20)
    atual = input("Data atual (dia/mes/ano)? ")
    horario_atual = input("Horario atual (hh:mm): ")
    atual = atual + " " + horario_atual
    dataAtual = datetime.datetime.strptime(atual, "%d/%m/%Y %H:%M")
    listaLocacoes = carregar_Locacao()
    camposLocacoes = list(listaLocacoes[0].keys())
    RecebidoTotal = 0
    for locacoes in listaLocacoes:
        if int(locacoes['Km_Final']) == 0 :
            ide = locacoes['Identificacao_Carro']
            cpf = locacoes['Cpf']
            listaClientes = mcli.carregar()
            camposClientes = list(listaClientes[0].keys())
            for cliente in listaClientes:
                if cliente['CPF'] == cpf :
                    Nome = cliente['Nome']
            inicio = locacoes['Data_Inicial']
            listaCarros = mcar.carregar()
            camposCarro = list(listaCarros[0].keys())
            ValorTotal = 0
            for carro in listaCarros:
                if int(carro['Identificacao']) == int(ide) :
                    Modelo = carro['Modelo']
                    Categoria = carro['Categoria']
                    Placa = carro['Placa']
                    ValorTotal = float(carro['Diaria'])
            data_inicial = datetime.datetime.strptime(locacoes['Data_Inicial'], "%Y-%m-%d %H:%M:%S")
            horas = diferenca_horas(data_inicial, dataAtual)
            dias = diferenca_dias(data_inicial, dataAtual)
            if dias <=0:
                pagamento = ValorTotal
            else:
                pagamento = ValorTotal*dias + (ValorTotal*horas/24)
            RecebidoTotal = RecebidoTotal + pagamento
            print("Cpf: ", cpf)
            print("Nome do cliente: ", Nome)
            print("Início da locação: ", inicio)
            print("Modelo do carro: ", Modelo)
            print("Categoria do carro: ", Categoria)
            print("Placa do carro: ", Placa)
            print("A receber da locação: ", pagamento)
    print("Total a receber de todas as locações: ", RecebidoTotal)        
            
                    
            
            
            