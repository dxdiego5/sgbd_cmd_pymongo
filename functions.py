import os
import funcMongoDB
from time import sleep

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
    print('\n')
    print('Version 1.0 ')
    print(16*'-', 'MongoDOS', 16*'-', '\n')

    return False

# List databases and collections
def menu_list_collections_of_db(dbname):

    cleanup_cmd()

    print(16*'-', 'MongoDOS', 16*'-', '\n')
    print(
        f'O BANCO de dados "{dbname.upper()}", tem as seguintes COLEÇÕES abaixo (\U0001F447):')

    print('\n')
    print(funcMongoDB.list_collections_db(dbname))
    print('\n')

    print('Escolha uma das OPÇÕES abaixo (\U0001F447), OU digite "S" para voltar ao MENU PRINCIPAL: \n')
    print('[ 1 ] \U00002B05  \U0001F4BE NOVA coleção:\n')
    print('[ 2 ] \U00002B05  \U00002757 REMOVER coleção:\n')
    print('[ 3 ] \U00002B05  \U0001F4BE NOVO documento:\n')
    print('[ 4 ] \U00002B05  \U00002757 REMOVER documento:\n')
    print('[ 5 ] \U00002B05  \U0001F50E BUSCAR documento:\n')
    print(
        f'[ 6 ] \U00002B05  \U00002757 DELETAR o BANCO (\U0001F449) "{dbname.upper()}": \n')
    print(16*'-', 'MongoDOS', 16*'-', '\n')

    option = input('Digite aqui (\U0001F449):')

    if option.lower() == 's':
        return

    elif option == '1':
        menu_crate_collection(dbname)

    elif option == '2':
        menu_delete_collection(dbname)

    elif option == '3':
        menu_create_document(dbname)

    elif option == '4':
        menu_delete_document(dbname)

    elif option == '5':
        menu_find_document(dbname)

    elif option == '6':
        menu_delete_base(dbname)
    else:
        # return menu principal
        return

# find document
def menu_find_document(dbname):
    select_colection_valid = False
    while select_colection_valid == False:
        cleanup_cmd()
        print(16*'-', 'MongoDOS', 16*'-', '\n')
        print(
            f'O BANCO é: "{dbname.upper()}", tem as seguintes COLEÇÕES abaixo (\U0001F447): \n')
        print(funcMongoDB.list_collections_db(dbname))
        print('\n')
        print(16*'-', 'MongoDOS', 16*'-', '\n')

        print('Informe o NOME da COLEÇÃO que deseja ACESSAR OU digite a letra "S" para voltar ao MENU anterior:')
        option = input('Digite aqui (\U0001F449):')

        if option.lower() == 's':
            select_colection_valid = True
            return menu_list_collections_of_db(dbname)

        elif option in funcMongoDB.list_collections_db(dbname):

            option_valid = False
            while option_valid == False:
                collection = option
                cleanup_cmd()
                print(16*'-', 'MongoDOS', 16*'-', '\n')
                print(
                    f'O BANCO é: "{dbname.upper()}", a COLEÇÃO é "{collection.upper()}": \n')

                print('[ 1 ] \U00002B05  Voltar ao MENU anterior \n')
                print('[ 2 ] \U00002B05  \U0001F50E LISTAR todos os DOCUMENTOS  \n')
                print(
                    '[ 3 ] \U00002B05  \U0001F50E LISTAR por FILTRO de CHAVE e VALOR  \n')
                print(16*'-', 'MongoDOS', 16*'-', '\n')

                option = input('Digite aqui (\U0001F449):')

                if option.lower() == '1':
                    option_valid = True
                    return menu_list_collections_of_db(dbname)

                elif option == '2':
                    cleanup_cmd()

                    limit_valid = False
                    while limit_valid == False:

                        cleanup_cmd()

                        print(16*'-', 'MongoDOS', 16*'-', '\n')
                        print(
                            f'LISTAR todos os DOCUMENTOS  do BANCO "{dbname.upper()}" da COLEÇÃO "{collection.upper()}" \n')
                        print(16*'-', 'MongoDOS', 16*'-', '\n')

                        limited = input(
                            'Informe um LIMITE de retorno de DADOS da PESQUISA: \n')

                        if str.isnumeric(limited):
                            cleanup_cmd()
                            info = funcMongoDB.list_all_document(
                                dbname, collection, int(limited))
                            limit_valid = True

                    for num, data in enumerate(info):
                        print('\n')
                        print(16*'-', 'MongoDOS', 'DOCUMETO NUMERO:',
                              num+1, 16*'-', '\n')
                        print(data)
                        print('\n')
                        print('\n')

                    print(25*'>', ' Aperte QUALQUER tecla para VOLTAR '.upper(), 25*'<')
                    print(25*'>', ' Aperte QUALQUER tecla para VOLTAR '.upper(), 25*'<')
                    print(25*'>', ' Aperte QUALQUER tecla para VOLTAR '.upper(), 25*'<')
                    input('Digite aqui (\U0001F449):')

                elif option == '3':
                    cleanup_cmd()
                    print(16*'-', 'MongoDOS', 16*'-', '\n')
                    print(
                        f'FILTRAR DOCUMENTOS  do BANCO "{dbname.upper()}" da COLEÇÃO "{collection.upper()}" \n')
                    print(16*'-', 'MongoDOS', 16*'-', '\n')

                    key = input('Informe aqui a CHAVE (\U0001F449):  \n')
                    value = input('Informe aqui o VALOR (\U0001F449): \n')

                    limit_valid = False
                    while limit_valid == False:
                        cleanup_cmd()
                        limited = input(
                            'Informe um LIMITE de retorno de DADOS da PESQUISA: \n')

                        if str.isnumeric(limited):
                            cleanup_cmd()
                            limit_valid = True
                            info = funcMongoDB.filtered_document(
                                dbname, collection, key, value, int(limited))

                            for num, data in enumerate(info):
                                print('\n')
                                print(16*'-', 'MongoDOS',
                                      'DOCUMETO NUMERO:', num+1, 16*'-', '\n')
                                print(data)
                                print('\n')
                                print('\n')

                            print(
                                25*'>', ' Aperte QUALQUER tecla para VOLTAR '.upper(), 25*'<')
                            print(
                                25*'>', ' Aperte QUALQUER tecla para VOLTAR '.upper(), 25*'<')
                            print(
                                25*'>', ' Aperte QUALQUER tecla para VOLTAR '.upper(), 25*'<')
                            input('Digite aqui (\U0001F449):')

# delete document menu
def menu_delete_document(dbname):

    select_colection_valid = False
    while select_colection_valid == False:
        cleanup_cmd()

        print(16*'-', 'MongoDOS', 16*'-', '\n')
        print(
            f'O BANCO é: "{dbname.upper()}", tem as seguintes COLEÇÕES abaixo (\U0001F447):\n')

        print(funcMongoDB.list_collections_db(dbname))

        print('\n')
        print(16*'-', 'MongoDOS', 16*'-', '\n')
        print('\n')

        print('Informe o NOME da COLEÇÃO que deseja ACESSAR para DELETAR algum DOCUMENTO OU digite a letra "S" para voltar ao MENU: \n')
        option = input('Digite aqui (\U0001F449):')

        if option.lower() == 's':
            select_colection_valid = True
            return menu_list_collections_of_db(dbname)

        elif option in funcMongoDB.list_collections_db(dbname):
            collection = option
            cleanup_cmd()
            print(16*'-', 'MongoDOS', 16*'-', '\n')
            print(f'O BANCO é: "{dbname.upper()}", a COLEÇÃO selecionada é "{collection.upper()}"\n \nfiltre os DOCUMENTOS que deseja DELETAR por CHAVE e VALOR conforme abaxio (\U0001F447)')
            print('\n')
            print(16*'-', 'MongoDOS', 16*'-')
            print('\n')

            key = input(f'Digite aqui (\U0001F449) a CHAVE: ')
            print('\n')

            value = input(f'Digite aqui (\U0001F449) o VALOR: ')
            print('\n')

            doc_condition_delete = False
            while doc_condition_delete == False:
                cleanup_cmd()
                print(16*'-', 'MongoDOS', 16*'-', '\n')

                print(f'A CHAVE que deseja FILTRAR é: "{key}": ')
                print(f'O VALOR que deseja FILTRAR é: "{value}": ')
                print('\n')
                print(16*'-', 'MongoDOS', 16*'-', '\n')

                option = input(
                    'Inform a letra "S" para CONFIRMAR A EXCLUSÃO OU a letra "N" para CANCELAR e voltar ao MENU anterior:')

                if option.lower() == 'n':
                    doc_condition_delete = True

                elif option.lower() == 's':
                    doc_condition_delete = True
                    info = funcMongoDB.delete_document(
                        dbname, collection, key, value)

                    for i in range(5, 0, -1):
                        cleanup_cmd()
                        print(16*'-', 'MongoDOS', 16*'-', '\n')
                        print(info, ' \U00002705 \n')
                        print(16*'-', 'MongoDOS', 16*'-', '\n')
                        print(
                            f'Retornando ao MENU  anterior {i} \U0000231B segundos')
                        sleep(1)

            return menu_list_collections_of_db(dbname)
        else:
            pass

# new document
def menu_create_document(dbname):

    collection_selected_condition = False
    while collection_selected_condition == False:

        cleanup_cmd()
        print(16*'-', 'MongoDOS', 16*'-', '\n')
        print(
            f'O BANCO de dados selecionado é: "{dbname.upper()}", segue abaixo (\U0001F447) as COLEÇÕES disponíveis:')

        print('\n')
        print(funcMongoDB.list_collections_db(dbname))
        print('\n')
        print(16*'-', 'MongoDOS', 16*'-', '\n')

        print('Informe qual o NOME da COLEÇÃO que deseja adicionar um NOVO DOCUMENTO OU digite a letra "S" para voltar ao MENU anterior: \n')
        option = input('Digite aqui (\U0001F449):')

        if option.lower() == 's':
            collection_selected_condition = True
            return menu_list_collections_of_db(dbname)

        collection = option
        if collection in funcMongoDB.list_collections_db(dbname):
            data = {}
            end_create = False
            index = 1
            while end_create == False:
                cleanup_cmd()
                print(16*'-', 'MongoDOS', 16*'-', '\n')
                print(
                    f'O BANCO de dados é: "{dbname.upper()}", a COLEÇÃO é: "{collection.upper()}" \n')
                print(16*'-', 'MongoDOS', 16*'-', '\n')

                key = input(f'Informe a CHAVE NUMERO "{index}" aqui: ')
                value = input(f'Informe o VALOR NUMERO "{index}" VALOR aqui: ')

                print('\n')

                print('[ 1 ] \U00002B05  SAIR e NÃO SALVAR: \n')
                print('[ 2 ] \U00002B05  SALVAR e SAIR: \n')
                print('[ ENTER ] \U00002B05  Precione QUALQUER TECLA (exeto 1 e 2 ja tem FUNÇÕES ESPECIAIS) para CONTINUAR CADASTRANDO chaves e valores no mesmo DOCUMENTO: \n')

                option = input('Digite aqui (\U0001F449):')

                data[key] = value

                if option == '1':
                    end_create = True
                    menu_list_collections_of_db(dbname)
                elif option == '2':
                    end_create = True

                index += 1

            if len(data) > 0 and option == '2' and end_create == True:
                funcMongoDB.create_document(dbname, collection, data)
                for i in range(5, 0, -1):
                    cleanup_cmd()
                    print(16*'-', 'MongoDOS', 16*'-', '\n')
                    print(f'O DOCUMENTO foi CRIADO com SUCESSO \U00002705 \n')
                    print(16*'-', 'MongoDOS', 16*'-', '\n')
                    print(f'Retornando ao MENU  {i} \U0000231B segundos')
                    sleep(1)

                menu_list_collections_of_db(dbname)

# delete database
def menu_delete_base(dbname):
    delete_base_condition = False
    while delete_base_condition == False:

        cleanup_cmd()

        print(16*'-', 'MongoDOS', 16*'-', '\n')
        print(
            f' Tem CERTEZA que deseja DELETAR o BANCO "{dbname.upper()}" \U00002753\U00002753\U00002753, Digite a letra ("S" para SIM) OU ("N" para NÃO) e voltar ao MENU anterior: \n')
        print(16*'-', 'MongoDOS', 16*'-', '\n')

        option = input('Digite aqui (\U0001F449):')

        if option.lower() == 's':
            funcMongoDB.delete_database(dbname)
            delete_base_condition = True

            for i in range(5, 0, -1):
                cleanup_cmd()
                print(16*'-', 'MongoDOS', 16*'-', '\n')
                print(
                    f'BANCO de dados "{dbname.upper()}" foi DELETADO com SUCESSO \U00002705 \n')
                print(16*'-', 'MongoDOS', 16*'-', '\n')
                print(f'Retornando ao MENU  {i} \U0000231B segundos')
                sleep(1)
            return

        elif option.lower() == 'n':
            delete_base_condition = True
            return menu_list_collections_of_db(dbname)

# create collection
def menu_crate_collection(dbname):

    cleanup_cmd()

    print(16*'-', 'MongoDOS', 16*'-', '\n')
    print(f'O BANCO de dados selecionado é: "{dbname.upper()}": \n')
    print(16*'-', 'MongoDOS', 16*'-', '\n')

    print('Informe um NOME pra criar uma NOVA COLEÇÃO OU digite a letra "S" para voltar ao MENU anterior:: \n')
    option = input('Digite aqui (\U0001F449):')

    if option.lower() == 's':
        pass
    else:
        collection = option
        funcMongoDB.create_collection_and_database(dbname, collection)
        for i in range(5, 0, -1):
            cleanup_cmd()
            print(16*'-', 'MongoDOS', 16*'-', '\n')
            print(
                f'A COLEÇÃO "{collection}" foi CRIADO com SUCESSO \U00002705 \n')
            print(16*'-', 'MongoDOS', 16*'-', '\n')
            print(f'Retornando ao MENU  {i} \U0000231B segundos')
            sleep(1)

    menu_list_collections_of_db(dbname)

# delete collection
def menu_delete_collection(dbname):
    select_colection_condition = False
    while select_colection_condition == False:
        cleanup_cmd()
        print(16*'-', 'MongoDOS', 16*'-', '\n')
        print(
            f'O BANCO de dados "{dbname.upper()}", tem as seguintes COLEÇÕES abaixo (\U0001F447): \n')

        print(funcMongoDB.list_collections_db(dbname))

        print('\n')
        print(16*'-', 'MongoDOS', 16*'-', '\n')

        option = input(
            'Informe qual o nome da COLEÇÃO que deseja DELETAR OU digite "S" para voltar ao MENU anterior: ')

        if option.lower() == 's':
            select_colection_condition = True
            return menu_list_collections_of_db(dbname)

        else:
            collection = option
            if collection in funcMongoDB.list_collections_db(dbname):
                funcMongoDB.delete_collection(dbname, collection)
                for i in range(5, 0, -1):
                    cleanup_cmd()
                    print(16*'-', 'MongoDOS', 16*'-', '\n')
                    print(
                        f'A COLEÇÃO "{collection}" do BANCO "{dbname}" foi DELETADO com SUCESSO \U00002705 \n')
                    print(16*'-', 'MongoDOS', 16*'-', '\n')
                    print(
                        f'Retornando ao MENU  anterior {i} \U0000231B segundos')
                    sleep(1)

                # valid if size list collection equals a zero
                if len(funcMongoDB.list_collections_db(dbname)) <= 0:
                    select_colection_condition = True