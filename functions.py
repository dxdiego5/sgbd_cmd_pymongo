import os
import funcMongoDB
import time
from pprint import pprint


def intro_prsentation():
    print(16*'-', 'MongoDOS', 16*'-', '\n')
    print('Olá meu nome é Mongo DOS \U0001f600 !')
    time.sleep(2)
    print('O meu criador é o Diego Felip da Silva Bez')
    time.sleep(3)
    print('ele dedicou o seu tempo para me criar então faça bom proveito!')
    time.sleep(3)
    print('\n', 16*'-', 'MongoDOS', 16*'-', '\n')
    for time_start_app in range(5, 0, -1):
        cleanup_cmd()
        print(16*'-', 'MongoDOS', 16*'-', '\n')
        print(
            f'A aplicação iniciará em {time_start_app} segundo aguarde ... \n')
        print(16*'-', 'MongoDOS', 16*'-', '\n')
        time.sleep(1)


def cleanup_cmd():
    os.system('clear')


def close_app():
    cleanup_cmd()

    print(16*'-', 'MongoDOS', 16*'-', '\n')
    print('Obrigado por usar o Mongo DOS, Bay Bay ...\n')

    print("                 ", "\U0001f600", "\U0001f600", "\U0001f600")
    print('\n', 16*'-', 'MongoDOS', 16*'-', '\n')

    return False


def list_collections_of_db(dbname):

    cleanup_cmd()

    print(45*'-')
    print(
        f'O banco de dados: "{dbname.upper()}", tem as seguintes collections abaixo: \n')

    print(funcMongoDB.list_collections_db(dbname))

    print('\n')
    print('[ 1 ] <- Para voltar ao menu de seleção de lista de banco de dados:')
    print(45*'-')
    print('[ 2 ] <- Para remover uma coleção:')
    print('[ 3 ] <- Para criar uma coleção:\n')

    print('[ 4 ] <- Para remover documentos:')
    print('[ 5 ] <- Para criar um documento:')
    print('[ 6 ] <- Para buscar documentos:')

    print('\n****** Tecle [ enter ] voltar ao menu prncipal: ')
    print(45*'-')
    print('\n')

    option = input('Digite aqui: ')

    if option == '1':
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
                                print(25*' ', 'Documento numero:', num+1, 25*' ', '\n')
                                pprint(data)
                                print('\n')
                                print(70*'#')
                                print('\n')

                            print(25*'>', ' Aperte [ enter ] para voltar ', 25*'<')
                            input()
    else:
        # Return menu principal
        pass
