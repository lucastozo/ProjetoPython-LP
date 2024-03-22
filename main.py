import manipulaCSV as mcsv
import manipulaClientes as mcli
import manipulaCarros as mcar
import apresentacao

def main():
    while True:
        opcao = apresentacao.MenuPrincipal()
        match opcao:
            case 1:
                opcaoLocacoes = 0
                while opcaoLocacoes != 9:
                    opcaoLocacoes = apresentacao.MenuLocacoes()
                    match opcaoLocacoes:
                        case 1:
                            print("Chamar Nova locação")
                        case 2:
                            print("Chamar Finalizar locação")
                        case 3:
                            print("Relatório de carros locados")
                    apresentacao.EsperaEnter()
            case 2:
                opcaoClientes = 0
                while opcaoClientes != 9:
                    opcaoClientes = apresentacao.MenuClientes()
                    match opcaoClientes:
                        case 1:
                            print("Chamar Cadastrar cliente")
                        case 2:
                            print("Chamar Alterar cliente")
                        case 3:
                            print("Chamar Excluir cliente")
                        case 4:
                            print("Chamar Localizar locações")
                    apresentacao.EsperaEnter()
            case 3:
                opcaoCarros = 0
                while opcaoCarros != 9:
                    opcaoCarros = apresentacao.MenuCarros()
                    apresentacao.limpaTela()
                    match opcaoCarros:
                        case 1:
                            carro = apresentacao.CadastrarCarro()
                            if mcar.cadastrar(carro):
                                print("Carro cadastrado com sucesso")
                            else:
                                print("Erro ao cadastrar carro")
                        case 2:
                            id = int(input("Digite o ID do carro que deseja alterar: "))
                            if mcar.alterar(id):
                                print("Carro alterado com sucesso")
                            else:
                                print("Carro não encontrado ou não foi alterado")
                        case 3:
                            id = int(input("Digite o ID do carro que deseja excluir: "))
                            if mcar.excluir(id):
                                print("Carro excluido com sucesso")
                            else:
                                print("Carro não encontrado ou não foi excluido")
                        case 4:
                            if mcar.disponibilizarCarrosParaVenda():
                                print("Operação realizada com sucesso")
                            else:
                                print("Não há carros disponíveis para venda")
                        case 5:
                            escolha = -1
                            while escolha < 0 or escolha > 4:
                                apresentacao.limpaTela()
                                print("Escollha a categoria do carro")
                                print("1. Econômico\n2. Intermediário\n3. Conforto\n4. Pickup")
                                escolha = int(input("Opção -> "))
                            apresentacao.limpaTela()

                            categorias = ['Econômico', 'Intermediário', 'Conforto', 'Pickup']
                            categoria = categorias[escolha-1]
                            mcar.listarCarrosPorCategoria(categoria)
                    if opcaoCarros != 9:
                        apresentacao.EsperaEnter()
            case 9:
                break

    '''
    print("*"*30)
    print("Exemplo de carregamento de dados de um arquivo csv")
    listaClientes = mcli.carregar()
    print(listaClientes)
    print("*"*30)
    print()
    print("*"*30)
    print("Exemplo de leitura dos campos e armazenamento em um arquivo csv")
    mcli.cadastrar(listaClientes)
    print("*"*30)
    print()
    print("*"*30)
    print("Exemplo de exclusão de um cliente e armazenamento em um arquivo csv")
    cpf = input("Qual cpf do cliente que deseja excluir? ")
    if  mcli.excluir(listaClientes, cpf) == True:
        print("Cliente excluido com sucesso")
    else:
        print("Cliente não encontrado")
    print()
    print("*"*30)
    print("Exemplo de leitura dos campos e armazenamento em um arquivo csv")
    print("*"*30)
    listaCarros = mcar.carregar()
    mcar.cadastrar(listaCarros)
    '''
# Inicio do programa 
if __name__ == "__main__":
    main()