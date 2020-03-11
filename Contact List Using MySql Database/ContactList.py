import mysql.connector
class ContactList:
    #=============================METHODS=================================== 
    #=============================METHOD START==============================
    def New_Contact(self):    
        try:
            connection = mysql.connector.connect(host='localhost', database='ContactDB', user='Atharva',
                                                password='Atharva@007')
            cursor = connection.cursor()
            name = input("Enter Name...   : ")
            mobile = input("Enter mobile Number...  : ")
            address = input("Enter address...  : ")
            email = input("Enter email address...  : ")
            company_name = input("Enter company name...  : ")
            birthdate = input("Enter birthdate...  : ")

            while len(mobile) != 10:
                print("Invalid Mobile Number ")
                mobile = input("ReEnter Mobile Number...  :")

            
            if len(mobile) == 10:
                cursor.execute(""" INSERT INTO contacts VALUES(%s,%s,%s,%s,%s,%s)""",(name,mobile,address,email,company_name,birthdate))

            print("\n Contact Added Succesfully.....................")
            connection.commit()
        except mysql.connector.Error as error:
            connection.rollback()  # rollback if any exception occured
            print("Failed  Contacts table {}".format(error))
        finally:
            if (connection.is_connected()):
                cursor.close()
                connection.close()
    #=============================METHOD END====================================    
    #=============================METHOD START==================================
    def Delete_Contact(self):
        try:
            connection = mysql.connector.connect(host='localhost', database='ContactDB', user='Atharva',
                                                password='Atharva@007')
            cursor = connection.cursor()

            ctd = input("Enter Contact Name to delete... : ")

            cursor.execute(""" Delete from contacts where name=%s""",(ctd,))
            
            
            if cursor.rowcount > 0:
                print("Contact Deleted Succesflly.......................")
            else:
                print("Invalid Contact!!!!!!!!!")
            connection.commit()
        except mysql.connector.Error as error:
            connection.rollback()  # rollback if any exception occured
            print("Failed  Contacts table {}".format(error))
        finally:
            if (connection.is_connected()):
                cursor.close()
                connection.close()
        
    #=============================METHOD END====================================    
    #=============================METHOD START==================================
    def Search_Contacts(self):
        try:
            connection = mysql.connector.connect(host='localhost', database='ContactDB', user='Atharva',
                                                password='Atharva@007')
            cursor = connection.cursor()
            name = input("Enter Name to search....... : ")
            cursor.execute(""" Select * from contacts where name=%s """,(name,))
            r = cursor.fetchall()

            print("\n Contact Founds:",r)
            
        except mysql.connector.Error as error:
            connection.rollback()  # rollback if any exception occured
            print("Failed  Contacts table {}".format(error))
        finally:
            if (connection.is_connected()):
                cursor.close()
                connection.close()
            
    #=============================METHOD END====================================    
    #=============================METHOD START==================================
    def View_Contacts(self):
        print("\n********************************* CONTACTS *******************************************\n")
        try:
            connection = mysql.connector.connect(host='localhost', database='ContactDB', user='Atharva',
                                                password='Atharva@007')
            cursor = connection.cursor()
            cursor.execute(" Select * from contacts ")

            all_contacts = cursor.fetchall()
            for x in all_contacts:
                print("Name         :   ",x[0])
                print("Mobile No    :   ",x[1])
                print("Email        :   ",x[2])
                print("Address      :   ",x[3])
                print("Birth Date   :   ",x[4])
                print("Company      :   ",x[5])

                print()
                print()
                print()
        except mysql.connector.Error as error:
            connection.rollback()  # rollback if any exception occured
            print("Failed  Contacts table {}".format(error))
        finally:
            if (connection.is_connected()):
                cursor.close()
                connection.close()
    #=============================METHOD END====================================    
   