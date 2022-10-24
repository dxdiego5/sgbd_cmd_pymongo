import funcMongoDB
from functions import cleanup_cmd, list_collections_of_db
import time


def main_principal():

    cleanup_cmd()

    options = ['0', '1', '2']

    # print(45*'-')
    # print('Olá meu nome é Mongo_Dos \U0001f600 !')
    # time.sleep(2)
    # print('O meu criador é o Diego Felip da Silva Bez')
    # time.sleep(3)
    # print('ele dedicou o seu tempo para me criar então fassa bom proveito!')
    # time.sleep(3)
    # print('A aplicação iniciará em 5 segundo aguarde ...')
    # print(45*'-')
    # time.sleep(5)
    # cleanup_cmd()

    print(45*'-', '\n')
    print('[ 1 ] <- Criar banco de dados:')
    print('[ 2 ] <- Mais opções: ')
    print('[ 0 ] <- Encerar aplicação: \n')
    print(45*'-')

    option_menu = input('Digite aqui uma das opções acima:  ')

    # valid menu options selected
    if option_menu not in options:
        return main_principal()
    else:
        return int(option_menu)


# submenu options
def menu_list_data():

    cleanup_cmd()

    name_dbs = funcMongoDB.list_databases()

    print(45*'-')
    print('Banco de dados disponíveis: \n')

    print(funcMongoDB.list_databases())

    print('[ 1 ] <- Voltar ao menu prncipal: ')
    print(45*'-')
    print('\n******** Digite o nome do banco acima que vc deseje ver as collections: \n')
    db_name = input('Digite aqui:')

    if db_name != '1':
        if db_name in name_dbs:
            response_info = list_collections_of_db(db_name)
            if response_info == '1':
                return menu_list_data()
        else:
            return menu_list_data()


def create_database():
    cleanup_cmd()

    print(45*'-', '\n')
    print('[ 1 ] <- Voltar ao menu prncipal:')
    print('[ ENTER ] <- Criar o banco de dados: :\n')
    print(45*'-')

    option = input('Digite aqui: ')

    if option == '1':
        return '1'
    else:
        bd_valid = False
        msg_error = ''
        while bd_valid == False:
            cleanup_cmd()
            print(msg_error)
            print('\n')
            dbname = input('Qual nome do banco que deseja criar: ')

            if dbname in funcMongoDB.list_databases() or dbname.count(' ') > 0:
                msg_error = f'Banco de dados "{dbname}" ja existe ou contem caracter inválidos como o espaços, tente outro nome! \n'
            else:
                funcMongoDB.create_collection_and_database(dbname)

                cleanup_cmd()
                print('\n')
                print(f'Banco de dados "{dbname}" criado com sucesso!')
                time.sleep(2)
                bd_valid = True
