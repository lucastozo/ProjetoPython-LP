import manipulaCSV as mcsv
import locacao
import apresentacao


def carregar() ->list: 
    '''
    Carrega o arquivo de Cliente.csv numa lista
    
    Retorno
    -------
    Retorna uma lista vazia caso o arquivo não exista ou 
    uma lista de dicionários contendo os dados dos clientes
    '''
    lista = mcsv.carregarDados("Clientes.csv")
    return lista
    

def cadastrar() -> bool :
    
    '''
    Rotina para cadastrar um novo cliente

    Parâmetros
    ----------
    listaClientes: Lista atual dos clientes

    Retorno
    -------
    Retorna True se o cliente foi cadastrado com sucesso
    '''
    print("Cadastramento de um novo cliente ")
    camposCliente = ["CPF","Nome","Nascimento","Idade","Endereco","Cidade","Estado"]
    cliente = {}
    for campo in camposCliente:
        cliente[campo] = input(f"{campo}:")
    listaClientes = carregar()
    listaClientes.append(cliente)
    return mcsv.gravarDados('Clientes.csv', camposCliente, listaClientes )

def atualizar() -> bool :
    '''
    Rotina para alterar um cliente

    Parâmetros
    ----------
    listaClientes: Lista atual dos clientes

    Retorno
    -------
    Retorna True se o cliente foi alterado com sucesso
    '''
    camposCliente = ["CPF","Nome","Nascimento","Idade","Endereco","Cidade","Estado"]
    cpf_cliente_a_ser_atualizado = input("Digite o CPF do cliente que deseja atualizar\n")
    cliente_encontrado = False
    listaClientes = carregar()
    for cliente in listaClientes:
        if cliente["CPF"] == cpf_cliente_a_ser_atualizado :
            cliente_encontrado = True
            opcao_menu_cliente = 0
            while opcao_menu_cliente != 9 :
                opcao_menu_cliente = apresentacao.MenuAtualizarClientes()
                match opcao_menu_cliente:
                    case 1:
                        cliente["CPF"] = input("Digite o novo CPF:\n")
                    case 2:
                        cliente["Nome"] = input("Digite o novo Nome:\n")
                    case 3:
                        cliente["Nascimento"] = input("Digite a nova Data de Nascimento:\n") 
                    case 4:
                        cliente["Idade"] = input("Digite a nova Idade:\n") 
                    case 5:
                        cliente["Endereco"] = input("Digite o novo Endereco:\n") 
                    case 6:
                        cliente["Cidade"] = input("Digite a nova Cidade:\n") 
                    case 7:
                        cliente["Estado"] = input("Digite o novo Estado:\n")
    if cliente_encontrado :
        return mcsv.gravarDados('Clientes.csv', camposCliente, listaClientes )
    else :
        return False
        
def excluir(cpf : str ) -> bool :
    '''
    Excluir um cliente da lista de clientes e atualiza o arquivo CSV
    '''
    cliente_encontrado = False
    listaClientes = carregar()
    camposCliente = list(listaClientes[0].keys())
    for cliente in enumerate(listaClientes):
        if cliente['CPF'] ==  cpf :
            cliente_encontrado = True
            listaClientes.pop(cliente)
    if cliente_encontrado :
        return mcsv.gravarDados("Clientes.csv", camposCliente, listaClientes)
    else :
        return False
    
def locacoes(cpf : str) -> bool :
    '''
    Localizar as locações de um cliente
    '''
    locacao_encontrada = False
    listaLocacoes = locacao.carregar_Locacao()
    for loc in listaLocacoes:
        if loc["Cpf"] ==  cpf :
            print("#"*20)
            for campo in loc :
                print(f"{campo} : " + loc[campo])
            print("#"*20)
            locacao_encontrada = True
    if locacao_encontrada :
        return True
    else :    
        return False
    
    
            
    