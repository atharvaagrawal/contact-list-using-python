import ContactList as cl

C = cl.ContactList()
choice = 0

while choice != 6:
    print("*********************************************************************************************")
    print("***                                Enter Choice                                           ***")
    print("***                                1 : Add New Contact                                    ***")
    print("***                                2 : Update a Contact                                   ***")
    print("***                                3 : Delete Contact                                     ***")
    print("***                                4 : View All Contacts                                  ***")
    print("***                                5 : Search a Contact                                   ***")
    print("***                                6 : Exit                                               ***")
    print("*********************************************************************************************")

    choice = int(input("Choice......: "))

    if choice == 1:
        C.New_Contact()

    elif choice == 2:
        C.Update_Contact()
    
    elif choice == 3:
        C.Delete_Contact()
    
    elif choice == 4:
        C.View_Contacts()
    
    elif choice == 5:
        C.Search_Contacts()
    
    elif choice == 6:
        break
    
    else:
        print("Wrong Choice !!!!!!!!!!!!!!!!!!!!!!!!!!")
        continue
    
    f = open("Contacts.txt","w")
    f.writelines(str(C.Contacts))
    f.close()
    
    c = input("*** Do You Want to Continue Y/N ***  ")

    if c == 'Y' or c == 'y':
        continue
    else:
        break