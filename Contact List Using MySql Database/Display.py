import ContactList as cl

C = cl.ContactList()
choice = 0

while choice != 5:
    print("*********************************************************************************************")
    print("***                                Enter Choice                                           ***")
    print("***                                1 : Add New Contact                                    ***")
    print("***                                2 : Delete Contact                                     ***")
    print("***                                3 : View All Contacts                                  ***")
    print("***                                4 : Search a Contact                                   ***")
    print("***                                5 : Exit                                               ***")
    print("*********************************************************************************************")

    choice = int(input("Choice......: "))

    if choice == 1:
        C.New_Contact()
    elif choice == 2:
        C.Delete_Contact()
    
    elif choice == 3:
        C.View_Contacts()
    
    elif choice == 4:
        C.Search_Contacts()
    
    elif choice == 5:
        break
    
    else:
        print("Wrong Choice !!!!!!!!!!!!!!!!!!!!!!!!!!")
        continue
    
    c = input("*** Do You Want to Continue Y/N ***  ")

    if c == 'Y' or c == 'y':
        continue
    else:
        break