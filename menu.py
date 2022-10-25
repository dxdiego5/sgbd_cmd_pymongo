from pprint import pprint
import funcMongoDB
from functions import cleanup_cmd, menu_list_collections_of_db
from time import sleep

def main_principal():

    cleanup_cmd()

    options = ['0', '1', '2']
        
    cleanup_cmd()
    print(16*'-', 'MongoDOS', 16*'-', '\n')
    print('[ 1 ] \U00002B05  Novo banco de dados:')
    print('[ 2 ] \U00002B05  Mais opções:')
    print('[ 0 ] \U00002B05  Encerar aplicação:')
    print('\n')
    print('Version 1.0')
    print(16*'-', 'MongoDOS', 16*'-','\n')
    print('Escolha uma das opções acima (\U0001F446):\n')
    option_menu = input('Digite aqui (\U0001F449):')


    # valid menu options selected
    if option_menu not in options:
        return main_principal()
    else:
        return int(option_menu)

# submenu more options
def menu_list_data():

    cleanup_cmd()

    name_dbs = funcMongoDB.list_databases()

    print(16*'-', 'MongoDOS', 16*'-', '\n')
    print('Lista de BANCO de dados disponíveis abaixo (\U0001F447): \n')
    pprint(name_dbs)
    print('\n')
    print(16*'-', 'MongoDOS', 16*'-', '\n')


    print('Informe o NOME do banco que deseja ACESSAR OU digite a letra "S" para voltar ao MENU principal: \n')
    option = input('Digite aqui (\U0001F449):')

    if option.lower() == 's':
        return


    elif option in name_dbs:
        # if dbname selected true
        dbname = option
        response_info = menu_list_collections_of_db(dbname)
        if response_info == '1':
            return menu_list_data()
    else:
        return menu_list_data()

def create_database():

    cleanup_cmd()

    db_valid = False
    msg_error = ''
    while db_valid == False:
        cleanup_cmd()
        print(16*'-', 'MongoDOS', 16*'-', '\n')

        if len(msg_error) > 0:
            print(f'\U00002757 {msg_error} \U00002757 \n \n')

        print('Digite nome do BANCO que deseja criar OU digite a letra "S" para voltar ao MENU principal: \n')
        print(16*'-', 'MongoDOS', 16*'-', '\n')

        option_menu = input('Digite aqui (\U0001F449):')

        if option_menu.lower() == 's':
            return '1'
        else:
            dbname = option_menu
            if dbname in funcMongoDB.list_databases() or dbname.count(' ') > 0:
                msg_error = f'Banco de dados "{dbname}" ja existe ou contém carácter inválidos, tente outro nome'
            else:
                # if dbname for valid create a new database
                funcMongoDB.create_collection_and_database(dbname)

                for i in range(5,0,-1):
                    cleanup_cmd()
                    print(16*'-', 'MongoDOS', 16*'-', '\n')
                    print(f'BANCO de dados "{dbname}" criado com SUCESSO \U00002705 \n')
                    print(16*'-', 'MongoDOS', 16*'-', '\n')
                    print(f'Retornando ao MENU em {i} \U0000231B segundos')
                    sleep(1)
                db_valid = True