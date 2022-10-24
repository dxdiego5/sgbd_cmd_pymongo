from functions import close_app
import menu

app_build = True

while app_build == True:

    # call function list menu
    option_menu = menu.main_principal()

    # Close application
    if option_menu == 0:
        app_build = close_app()

    # create databases
    if option_menu == 1:
        menu.create_database()

    # list collections, databases and remove colections
    if option_menu == 2:
        menu.menu_list_data()
