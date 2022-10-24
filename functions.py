import os
import funcMongoDB


def cleanup_cmd():
    os.system('clear')


def close_app():
    cleanup_cmd()

    print(45*'-')
    print('Obrigado por usar a nossa aplicação, Bay Bay \n')

    print("               ", "\U0001f600", "\U0001f600", "\U0001f600")
    print(45*'-')

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

                index +=1

            if len(data) > 0 and option_break == '2' and end_create == True:
                funcMongoDB.create_document(dbname, collection, data)
                list_collections_of_db(dbname)

    else:
        # Return menu principal
        pass
