import database


MENU_PROMPT = """
--Coffee Bean App--

Please choose an option:

1) Add new bean
2) See all beans
3) Find bean by name
4) See wich preparation is best for a bean
5) Exit

Your selection: 
"""

def menu():
    connection = database.connect()
    database.create_table(connection)
    
    while(user_input := input(MENU_PROMPT)) != "5":
        if user_input == "1":
            add_new_bean(connection)
            
        elif user_input == "2":
            see_all_beans(connection)
                
        elif user_input == "3":
            find_bean_by_name(connection)
            
        elif user_input == "4":
            see_preparation(connection)
         
        else:
            print("You are shit")
            
            
            
def add_new_bean(connection):   
    name = input("Enter bean name: ")
    method = input("Enter bean method: ")
    rating = int(input("Enter your rating (0-100): "))
    database.add_bean(connection, name, method, rating)


def see_all_beans(connection):
    beans = database.get_all_beans(connection)
    for bean in beans:
        print(f"({bean[1]}) ({bean[2]}) - {bean[3]}/100")


def find_bean_by_name(connection):
    name = input("Enter name: ")
    beans = database.get_beans_by_name(connection, name)
    if not beans:
        print("not found")
    else:    
        for bean in beans:
            print(f"({bean[1]}) ({bean[2]}) - {bean[3]}/100")


def see_preparation(connection):
    name = input("Enter bean name: ")
    best_method = database.get_best_preparation_for_bean(connection, name)
    print(f"The best preparation for {name} is {best_method[2]}")
        
menu()
    
    