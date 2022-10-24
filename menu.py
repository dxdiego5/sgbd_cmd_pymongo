import funcMongoDB
from functions import cleanup_cmd, list_collections_of_db


def main_principal():

    cleanup_cmd()

    options = ['0', '1', '2']

    print(45*'-')
    print('[ 1 ] <- Criar banco de dados')
    print('[ 2 ] <- Mais opções: ')
    print('\n')
    print('[ 0 ] <- Encerar aplicação.')
    print(45*'-')

    option_menu = input('Digite a opção que deseja:  ')

    # valid menu options selected
    if option_menu not in options:
        return main_principal()
    else:
        return int(option_menu)


# submenu options 7
def menu_list_data():

    name_dbs = funcMongoDB.list_databases()

    cleanup_cmd()

    print(45*'-')
    print('Banco de dados disponíveis: \n')

    print(funcMongoDB.list_databases())

    print('\n[ 1 ] <- Para voltar ao menu prncipal: ')
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

    print(45*'-')
    print('[ 1 ] <- Para voltar ao menu prncipal:\n')
    print('[ ENTER ] <- Para criar o banco de dados:')
    print(45*'-')
    
    option = input('Digite aqui: ')

    if option == '1':
        return '1'
    else:
        bd_valid = False
        msg_error = ''
        while bd_valid == False:
            cleanup_cmd()
            print('\n')
            print(msg_error)
            print('Digite o nome do banco que deseja criar: ')
            
            dbname = input('Digite aqui: ')

            if dbname in funcMongoDB.list_databases() or dbname.count(' ') > 0:
                    msg_error = f'Banco de dados "{dbname}" ja existe ou contem caracter invalidos como o espaços, tente outro nome! \n'
            else:
                funcMongoDB.create_collection(dbname)
                bd_valid = True   