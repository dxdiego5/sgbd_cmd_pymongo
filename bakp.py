import os
import funcMongoDB
from time import sleep
from pprint import pprint

# intro start aplicattion build
def intro_prsentation():
    print(16*'-', 'MongoDOS', 16*'-', '\n')
    print('Olá meu nome é Mongo DOS \U0001f600 !')
    sleep(2)
    print('O meu criador é o Diego Felip da Silva Bez')
    sleep(3)
    print('ele dedicou o seu tempo para me criar então faça bom proveito!')
    sleep(4)
    print('\n', 16*'-', 'MongoDOS', 16*'-', '\n')
    for time_start_app in range(5, 0, -1):
        cleanup_cmd()
        print(16*'-', 'MongoDOS', 16*'-', '\n')
        print(
            f'Aplicação iniciará em {time_start_app} \U0000231B segundo aguarde ... \n')
        print(16*'-', 'MongoDOS', 16*'-', '\n')
        sleep(1)

# clean a cmd comand line
def cleanup_cmd():
    os.system('clear')

# closed application
def close_app():
    mongo_dos = """
.___  ___.   ______   .__   __.   _______   ______       _______   ______        _______.
|   \/   |  /  __  \  |  \ |  |  /  _____| /  __  \     |       \ /  __  \      /       |
|  \  /  | |  |  |  | |   \|  | |  |  __  |  |  |  |    |  .--.  |  |  |  |    |   (----`
|  |\/|  | |  |  |  | |  . `  | |  | |_ | |  |  |  |    |  |  |  |  |  |  |     \   \    
|  |  |  | |  `--'  | |  |\   | |  |__| | |  `--'  |    |  '--'  |  `--'  | .----)   |   
|__|  |__|  \______/  |__| \__|  \______|  \______/     |_______/ \______/  |_______/"""

    cleanup_cmd()

    print(16*'-', 'MongoDOS', 16*'-', '\n')
    print('Obrigado por usar o Mongo DOS, Bay Bay ...\n')

    print(16*" ", "\U0001f600", "\U0001f600", "\U0001f600")

    print(mongo_dos)
    print('\n')

    print('\U000000A9 Todos os direitos reservados')
    print('Desenvolvedor - Diego Felipe Da Silva Bez')

    print('\n', 16*'-', 'MongoDOS', 16*'-', '\n')

    return False


def list_collections_of_db(dbname):

    cleanup_cmd()

    print(16*'-', 'MongoDOS', 16*'-', '\n')
    print(f'O BANCO de dados "{dbname.upper()}", tem as seguintes COLEÇÕES abaixo (\U0001F447):')
        
    print('\n')
    print(funcMongoDB.list_collections_db(dbname))
    print('\n')

    print('Escolha uma das OPÇÕES abaixo (\U0001F447), OU digite "S" para voltar ao MENU principal: \n')
    print('[ 1 ] \U00002B05  \U0001F4BE NOVA coleção:\n')
    print('[ 2 ] \U00002B05  \U00002757 REMOVER coleção:\n')
    print('[ 3 ] \U00002B05  \U0001F4BE NOVO documento:\n')
    print('[ 4 ] \U00002B05  \U00002757 REMOVER documento:\n')
    print('[ 5 ] \U00002B05  \U0001F50E BUSCAR documento:\n')
    print(f'[ 6 ] \U00002B05  \U00002757 DELETAR o BANCO (\U0001F449) "{dbname.upper()}": \n')
    print(16*'-', 'MongoDOS', 16*'-', '\n')

    option = input('Digite aqui (\U0001F449):')

    if option.lower() == 's':
        return '1'

    if option == '2':
        select_colection_valid = False
        while select_colection_valid == False:
            cleanup_cmd()
            print(45*'-')
            print(
                f'O banco de dados: "{dbname.upper()}", tem as seguintes collections abaixo: \n')

            print(funcMongoDB.list_collections_db(dbname))

            print('\n')
            print('[ 1 ] <- Para voltar ao menu de seleção de lista de banco de dados:')
            print(45*'-')
            print('\n')

            collection = input(
                'Digite o nome da collection que deseja remover: ')

            if collection == '1':
                return '1'

            if collection in funcMongoDB.list_collections_db(dbname):
                funcMongoDB.delete_collection(dbname, collection)
                # valid if size list collection equals a zero
                if len(funcMongoDB.list_collections_db(dbname)) <= 0:
                    select_colection_valid = True

    if option == '3':
        # create collection
        cleanup_cmd()
        print(45*'-')
        print(
            f'O banco de dados selecionado é: "{dbname.upper()}": \n')

        print('\n')
        print('[ 1 ] <- Para voltar ao menu de seleção de lista de banco de dados:')
        print(45*'-')
        print('\n')
        print('Digite o nome da collection que deseja criar no banco: ')
        collection = input('Digite aqui: ')

        if collection == '1':
            return '1'
        else:
            funcMongoDB.create_collection_and_database(dbname, collection)
            return '1'

    if option == '4':

        select_colection_valid = False
        while select_colection_valid == False:
            cleanup_cmd()

            print(45*'-')
            print(
                f'O banco de dados: "{dbname.upper()}", tem as seguintes collections abaixo: \n')

            print(funcMongoDB.list_collections_db(dbname))

            print('\n')
            print('[ 1 ] <- Para voltar ao menu de seleção de lista de banco de dados:')
            print(45*'-')
            print('\n')

            collection = input(
                'Digite o nome da collection que deseja remover um documento: ')

            if collection == '1':
                return '1'

            if collection in funcMongoDB.list_collections_db(dbname):
                cleanup_cmd()
                print(
                    f'O banco de dados é: "{dbname.upper()}", a collection selecionada é "{collection.upper()}": \n')
                print('\n')
                print(
                    '[ 1 ] <- Para voltar ao menu de seleção de lista de banco de dados: \n')
                print('[ ENTER ] para continuar a deleção do documento:')
                print(45*'-')
                print('\n')

                option = input('Digite aqui: ')
                print('\n')

                if option == '1':
                    return '1'

                print(
                    'Digite o nome da chave que dejesa filtrar para deleção do documento:')
                key_data = input('Digite aqui: ')

                print('\n')

                print('Digite o valor da chave que deseja filtrar:')
                value = input('Digite aqui: ')

                funcMongoDB.delete_document(
                    dbname, collection, key_data, value)

    if option == '5':
        cleanup_cmd()
        print(45*'-')
        print(f'O banco de dados é: "{dbname.upper()}":')
        print('\n')
        print(funcMongoDB.list_collections_db(dbname))
        print('\n')
        print('[ 1 ] <- Para voltar ao menu de seleção de lista de banco de dados:')
        print(45*'-')
        print('\n')

        print('Digite o nome da collection que deseja adicionar um novo documento: ')
        collection = input('Digite aqui:')

        if collection == '1':
            return '1'

        if collection in funcMongoDB.list_collections_db(dbname):

            data = {}
            end_create = False
            index = 1
            while end_create == False:
                cleanup_cmd()
                print(
                    f'O banco de dados é: "{dbname.upper()}", a colection selecionada é {collection.upper()}: \n')

                key = input(f'Digite a "{index}" chave aqui: ')
                value = input(f'Digite o "{index}" valor aqui: ')

                print('\n')
                print('[ 1 ] - Para sair e não salvar: ')
                print('[ 2 ] - Para salvar e sair: ')
                print(
                    '[ ENTER ] - Para continuar cadastrado chaves e valores do mesmo documento: \n')

                option_break = input('Digite aqui: ')

                data[key] = value

                if option_break == '1':
                    end_create = True
                    list_collections_of_db(dbname)
                elif option_break == '2':
                    end_create = True

                index += 1

            if len(data) > 0 and option_break == '2' and end_create == True:
                funcMongoDB.create_document(dbname, collection, data)
                list_collections_of_db(dbname)
                input('asdad')

    if option == '6':

        select_colection_valid = False
        while select_colection_valid == False:
            cleanup_cmd()
            print(45*'-')
            print(
                f'O banco de dados: "{dbname.upper()}", tem as seguintes collections abaixo: \n')

            print(funcMongoDB.list_collections_db(dbname))

            print('\n')
            print('[ 1 ] <- Para voltar ao menu de seleção de lista de banco de dados:')
            print(45*'-')
            print('\n')

            collection = input(
                'Digite o nome da collection que deseja buscar algum documento: ')

            if collection == '1':
                return '1'

            if collection in funcMongoDB.list_collections_db(dbname):
                cleanup_cmd()
                print(
                    f'O banco de dados é: "{dbname.upper()}", a colection selecionada é {collection.upper()}: \n')
                print(
                    '[ 1 ] <- Para voltar ao menu de seleção de lista de banco de dados:')
                print('[ 2 ] <- Listar todos os documentos')
                print('[ 3 ] <- Listar por filtro de chave e valor')

                option_select = input('Digite a opcao')

                if option_select == '1':
                    return '1'

                if option_select == '2':
                    cleanup_cmd()

                    limit_valid = False
                    while limit_valid == False:
                        cleanup_cmd()
                        limited = input(
                            'Digite um limite de retorno de dados da pesquisa: \n')

                        if str.isnumeric(limited):
                            cleanup_cmd()
                            info = funcMongoDB.list_all_document(
                                dbname, collection, int(limited))
                            limit_valid = True

                    for num, data in enumerate(info):
                        print(25*' ', 'Documento numero:', num+1, 25*' ', '\n')
                        pprint(data)
                        print('\n')
                        print(70*'#')
                        print('\n')

                    print(25*'>', ' Aperte [ enter ] para voltar ', 25*'<')
                    input()

                if option_select == '3':
                    cleanup_cmd()
                    key = input('Digite a chave para a pesquisa: \n')
                    value = input('Digite o valor para a pesquisa: \n')

                    limit_valid = False
                    while limit_valid == False:
                        cleanup_cmd()
                        limited = input(
                            'Digite um limite de retorno de dados da pesquisa: \n')

                        if str.isnumeric(limited):
                            cleanup_cmd()
                            limit_valid = True
                            info = funcMongoDB.filtered_document(
                                dbname, collection, key, value, int(limited))
                            for num, data in enumerate(info):
                                print(25*' ', 'Documento numero:',
                                      num+1, 25*' ', '\n')
                                pprint(data)
                                print('\n')
                                print(70*'#')
                                print('\n')

                            print(
                                25*'>', ' Aperte [ enter ] para voltar ', 25*'<')
                            input()
    
    if option == '7':
        # drop database
        funcMongoDB.delete_database(dbname)
        return '1'
    else:
        # Return menu principal
        pass
