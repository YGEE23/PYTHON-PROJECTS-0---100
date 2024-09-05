#Basic Shopping List
'''
Instructions:

Allow the user to add items to the shopping list.
Allow the user to view the current list of items.
Provide an option to remove an item from the list.
Allow the user to clear the entire list.
Implement a menu to navigate these options.
The program should continue running until the user chooses to exit.

'''

# List of items in the shopping list
shopping_list = ['banana', 'apple', 'slides', 'milk', 'sugar','bread', 'beverages']

# formatted list horizontally
formated_list = ', '.join(shopping_list)

# Adding to the list    
def add():
    add_list = str(input("Enter name of item to add or press r to return to menu: ")).strip().lower()
    shopping_list.append(add_list)
    
# cancel the add operation
    if add_list == 'r':
        shopping_menu()

# View the list
def view():
    print("Your shopping list: ")
    for item in shopping_list:
        print(item)

# clear shopping list
def clear():
    shopping_list.clear()
    print("Shopping list has been cleared!")

# delete an item on the list
def delete ():
    # below prompts user to correctly input an existing item to delete

    while True:
        item_to_delete = input("Enter name of item to delete and r to return back to menu: ").strip().lower()
        if item_to_delete in shopping_list:
            shopping_list.remove(item_to_delete)
            print(f"{item_to_delete} was deleted from the shopping list.")
            break
        # prompts user to cancle delete operation
        elif item_to_delete == 'r':
            break
        else:
            print(f"Error: {item_to_delete} is not on the shopping list, please try again")



def shopping_menu():
    while True:

        print("\n What do you want to do to your shopping list?\n")

        print(" [1] to add to list")
        print(" [2] to view list")
        print(" [3] to delete items in list")
        print(" [4] to clear list")
        print(" [q] to quit \n")

        user_input = input("Enter your choice [1/2/3/4/q]: ").strip().lower()

        if user_input == '1':
            add()
            print(f"{user_input} have been added to the list!")

        elif user_input == '2':
            view()

        elif user_input == '3':
            delete()

        elif user_input == '4':
            clear()

        elif user_input == 'q':
            print("Goodbye!")
            break
    else:
        print("Invalide input, please enter a valid option")

if __name__ == '__main__': 
    shopping_menu()