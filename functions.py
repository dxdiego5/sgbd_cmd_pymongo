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

    print('Escolha uma das OPÇÕES abaixo (\U0001F447), OU digite "S" para voltar ao MENU anterior: \n')
    print('[ 1 ] \U00002B05  \U0001F4BE NOVA coleção:\n')
    print('[ 2 ] \U00002B05  \U00002757 REMOVER coleção:\n')
    print('[ 3 ] \U00002B05  \U0001F4BE NOVO documento:\n')
    print('[ 4 ] \U00002B05  \U00002757 REMOVER documento:\n')
    print('[ 5 ] \U00002B05  \U0001F50E BUSCAR documento:\n')
    print(f'[ 6 ] \U00002B05  \U00002757 DELETAR o BANCO (\U0001F449) "{dbname.upper()}": \n')
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
        # REMOVER documento
        pass
    elif option == '5':
        # BUSCAR documento
        pass
    elif option == '6':
        menu_delete_base(dbname)
    else:
        # return menu principal
        return


# new document
def menu_create_document(dbname):

    collection_selected_condition = False
    while collection_selected_condition == False:

        cleanup_cmd()
        print(16*'-', 'MongoDOS', 16*'-', '\n')
        print(f'O BANCO de dados selecionado é: "{dbname.upper()}", segue abaixo (\U0001F447) as COLEÇÕES disponíveis:')

        print('\n')
        print(funcMongoDB.list_collections_db(dbname))
        print('\n')
        print(16*'-', 'MongoDOS', 16*'-', '\n')

        print('Informe qual o NOME da COLEÇÃO que deseja adicionar um NOVO DOCUMENTO OU digite a letra "S" para voltar ao MENU anterior: \n')
        option = input('Digite aqui (\U0001F449):')

        if option.lower() == 's':
            collection_selected_condition = True
            return list_collections_of_db(dbname)

        collection = option 
        if collection in funcMongoDB.list_collections_db(dbname):
            data = {}
            end_create = False
            index = 1
            while end_create == False:
                cleanup_cmd()
                print(16*'-', 'MongoDOS', 16*'-', '\n')
                print( f'O BANCO de dados é: "{dbname.upper()}", a COLEÇÃO é: "{collection.upper()}" \n')
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
                    list_collections_of_db(dbname)
                elif option == '2':
                    end_create = True

                index += 1

            if len(data) > 0 and option == '2' and end_create == True:
                funcMongoDB.create_document(dbname, collection, data)
                for i in range(5,0,-1):
                    cleanup_cmd()
                    print(16*'-', 'MongoDOS', 16*'-', '\n')
                    print(f'O DOCUMENTO foi CRIADO com SUCESSO \U00002705 \n')
                    print(16*'-', 'MongoDOS', 16*'-', '\n')
                    print(f'Retornando ao MENU  {i} \U0000231B segundos')
                    sleep(1)

                list_collections_of_db(dbname)







# delete database
def menu_delete_base(dbname):
    delete_base_condition = False
    while delete_base_condition == False:
        
        cleanup_cmd()
        
        print(16*'-', 'MongoDOS', 16*'-', '\n')
        print(f' Tem CERTEZA que deseja DELETAR o BANCO "{dbname}" \U00002753\U00002753\U00002753, Digite a letra ("S" para SIM) OU ("N" para NÃO) e voltar ao MENU anterior: \n')
        print(16*'-', 'MongoDOS', 16*'-', '\n')

        option = input('Digite aqui (\U0001F449):')
        
        if option.lower() == 's':
            funcMongoDB.delete_database(dbname)
            delete_base_condition = True
           
            for i in range(5,0,-1):
                cleanup_cmd()
                print(16*'-', 'MongoDOS', 16*'-', '\n')
                print(f'BANCO de dados "{dbname}" foi DELETADO com SUCESSO \U00002705 \n')
                print(16*'-', 'MongoDOS', 16*'-', '\n')
                print(f'Retornando ao MENU  {i} \U0000231B segundos')
                sleep(1)
            return
        
        elif option.lower() == 'n': 
            delete_base_condition = True
            return list_collections_of_db(dbname)

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

    list_collections_of_db(dbname)  

# delete collection
def menu_delete_collection(dbname):
    select_colection_condition = False
    while select_colection_condition == False:
        cleanup_cmd()
        print(16*'-', 'MongoDOS', 16*'-', '\n')
        print(f'O BANCO de dados "{dbname.upper()}", tem as seguintes COLEÇÕES abaixo (\U0001F447): \n')

        print(funcMongoDB.list_collections_db(dbname))

        print('\n')
        print(16*'-', 'MongoDOS', 16*'-', '\n')

        option = input('Informe qual o nome da COLEÇÃO que deseja DELETAR OU digite "S" para voltar ao MENU anterior: ')
            

        if option.lower() == 's':
            select_colection_condition = True
            return list_collections_of_db(dbname)
        
        else:
            collection = option
            if collection in funcMongoDB.list_collections_db(dbname):
                funcMongoDB.delete_collection(dbname, collection)
                for i in range(5,0,-1):
                    cleanup_cmd()
                    print(16*'-', 'MongoDOS', 16*'-', '\n')
                    print(f'A COLEÇÃO "{collection}" do BANCO "{dbname}" foi DELETADO com SUCESSO \U00002705 \n')
                    print(16*'-', 'MongoDOS', 16*'-', '\n')
                    print(f'Retornando ao MENU  anterior {i} \U0000231B segundos')
                    sleep(1)

                # valid if size list collection equals a zero
                if len(funcMongoDB.list_collections_db(dbname)) <= 0:
                    select_colection_condition = True