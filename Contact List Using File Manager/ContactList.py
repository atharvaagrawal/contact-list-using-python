class ContactList:
    #============================VARIABLES===================================
    Contacts = {}

    #=============================METHODS====================================
    #=============================METHOD START==================================
    def __init__(self):
        
        f = open("Contacts.txt","r")
        s = f.readline()
        if s == "":
            pass
        else:
            self.Contacts = eval(s)
    #=============================METHOD End====================================    
    
    #=============================METHOD START==================================
    def New_Contact(self):
        
        f = open("Contacts.txt","a")

        info = {'Mobile':None,'Address':None,'Email':None,'Home':None,'Company':None,'BirthDate':None}
        Name = input("Enter Name...   : ")
        mobile = input("Enter mobile Number...  : ")
        address = input("Enter address...  : ")
        email = input("Enter email address...  : ")
        home = input("Enter home number...  : ")
        company = input("Enter company name...  : ")
        birthdate = input("Enter birthdate...  : ")

        while len(mobile) != 10:
            print("Invalid Mobile Number ")
            mobile = input("ReEnter Mobile Number...  :")

        
        if len(mobile) == 10:
            info['Mobile'] = mobile
            info['Address'] = address
            info['Email'] = email
            info['Home'] = home
            info['Company'] = company
            info['BirthDate'] = birthdate

        self.Contacts[Name] = info
        print("\n Contact Added Succesfully.....................")

        f.writelines(str(self.Contacts))
        f.close()
 
    #=============================METHOD END====================================    
    #=============================METHOD START==================================
    def Delete_Contact(self):
        
        f = open("Contacts.txt","a")
        ctd = input("Enter Contact Name to delete... : ")
        if ctd in self.Contacts:
            del self.Contacts[ctd]
            print("Contact Deleted Succesflly.......................")
        else:
            print("Invalid Contact!!!!!!!!!")
        f.writelines(str(self.Contacts))
        f.close()
 
    #=============================METHOD END====================================    
    #=============================METHOD START==================================
    def Search_Contacts(self):
        
        name = input("Enter Name to search....... : ")
        for s in self.Contacts:
            if name in s:
                print("Name         :   ",s)
                print("Mobile No    :   ",self.Contacts[s]['Mobile'])
                print("Home         :   ",self.Contacts[s]['Home'])
                print("Email        :   ",self.Contacts[s]['Email'])
                print("Address      :   ",self.Contacts[s]['Address'])
                print("Birth Date   :   ",self.Contacts[s]['BirthDate'])
                print("Company      :   ",self.Contacts[s]['Company'])

            print()
            print()
            print()

    #=============================METHOD END====================================    
    #=============================METHOD START==================================
    def View_Contacts(self):
        print("\n********************************* CONTACTS *******************************************\n")
        for x in self.Contacts:
            print("Name         :   ",x)
            print("Mobile No    :   ",self.Contacts[x]['Mobile'])
            print("Home         :   ",self.Contacts[x]['Home'])
            print("Email        :   ",self.Contacts[x]['Email'])
            print("Address      :   ",self.Contacts[x]['Address'])
            print("Birth Date   :   ",self.Contacts[x]['BirthDate'])
            print("Company      :   ",self.Contacts[x]['Company'])

            print()
            print()
            print()

    #=============================METHOD END====================================    
    #=============================METHOD START==================================
    def Update_Contact(self):

        f = open("Contacts.txt","a")
        name = input("Enter Name of Contact To Be Updated....  : ")
        
        if name in self.Contacts:
            print("Select Choice \n 1 : Update Name \n 2 : Update Mobile No \n 3 : Update Home No \n 4 : Update Email \n 5 : Update Address \n 6 : Update Birth Date \n 7 : Update Company \n 8 : Update All")
            ch = int(input())

            if(ch == 1):
                nm = input("Enter New Name... : ")
                self.Contacts[nm] = self.Contacts[name]
                del self.Contacts[name]
                f.writelines(str(self.Contacts))
                print("Updated Succesfully......................................")

            elif(ch == 2):
                mobile = input("Enter Mobile Number...  : ")
                while len(mobile) != 10:
                    print("Invalid Mobile Number ")
                    mobile = input("ReEnter Mobile Number...  :")
                self.Contacts[name]['Mobile'] = mobile
                f.writelines(str(self.Contacts))
                print("Updated Succesfully......................................")

            elif(ch == 3):
                home = input("Enter home number...  : ")
                self.Contacts[name]['Home'] = home
                f.writelines(str(self.Contacts))
                print("Updated Succesfully......................................")

            elif(ch == 4):
                email = input("Enter email address...  : ")
                self.Contacts[name]['Email'] = email
                f.writelines(str(self.Contacts))
                print("Updated Succesfully......................................")

            elif(ch == 5):
                address = input("Enter address...  : ")
                self.Contacts[name]['Address'] = address
                f.writelines(str(self.Contacts))
                print("Updated Succesfully......................................")
                
            elif(ch == 6):
                birthdate = input("Enter birthdate...  : ")
                self.Contacts[name]['BirthDate'] = birthdate
                f.writelines(str(self.Contacts))
                print("Updated Succesfully......................................")

            elif(ch == 7):
                company = input("Enter company name...  : ")
                self.Contacts[name]['Company'] = company
                f.writelines(str(self.Contacts))
                print("Updated Succesfully......................................")

            elif(ch == 8):
                info = {'Mobile':None,'Address':None,'Email':None,'Home':None,'Company':None,'BirthDate':None}
                Name = input("Enter new Name...   : ")
                mobile = input("Enter mobile Number...  : ")
                address = input("Enter address...  : ")
                email = input("Enter email address...  : ")
                home = input("Enter home number...  : ")
                company = input("Enter company name...  : ")
                birthdate = input("Enter birthdate...  : ")

                while len(mobile) != 10:
                    print("Invalid Mobile Number ")
                    mobile = input("ReEnter Mobile Number...  :")

        
                if len(mobile) == 10:
                    info['Mobile'] = mobile
                    info['Address'] = address
                    info['Email'] = email
                    info['Home'] = home
                    info['Company'] = company
                    info['BirthDate'] = birthdate
                    self.Contacts[Name] = info
                    del self.Contacts[name]
                    print("Updated Succesfully......................................")
            else:
                print("Wrong Choice....")

            f.close()            
    #=============================METHOD END====================================