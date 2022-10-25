from functions import close_app, intro_prsentation
import menu

app_build = True


# intro_prsentation()

while app_build == True:

    # call function list menu
    option_menu = menu.main_principal()

    # close application
    if option_menu == 0:
        app_build = close_app()

    # create databases
    if option_menu == 1:
        menu.create_database()

    # list collections, databases, remove colections, documents and filtered documents
    if option_menu == 2:
        menu.menu_list_data()
