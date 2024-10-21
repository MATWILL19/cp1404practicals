"""Menus"""

# get name
# display menu
# get choice
# while choice != Q
#    if choice == H
#        display "hello" name
#    else if choice == G
#        display "goodbye" name
#    else
#        display invalid message
#    display menu
#    get choice
# display finished message

username = input("Enter name: ")
print("(H)ello")
print("(G)oodbye")
print("(Q)uit")
menu_choice = input("")
while menu_choice != "Q":
    if menu_choice == "H":
        print("Hello " + username)
    elif menu_choice == "G":
        print("Goodbye " + username)
    else:
        print("Invalid")
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")
    menu_choice = input("")
print("Finished")