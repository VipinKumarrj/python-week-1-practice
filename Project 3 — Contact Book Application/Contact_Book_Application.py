

while True:
    print("1. Personal Contact")
    print("2. Business Contact")
    print("3. Exit")
    
    a=int(input("Select an option 1-3: "))
    
    if a==1 or a==2:
            while True:
                print("1. Add Contact")
                print("2. View Contact")
                print("3. Update Contact")
                print("4. Search Contact")
                print("5. Delete Contact")
                
                b=int(input("Select an option 1-5: "))
                
                if b==1:
                    c=input("Enter New Contact Name: ")
                    d=int(input("Enter Mobile number: "))
                    e=input("Enter Email ID: ")
                    print("SAVED DETAILS")
                elif b==2:
                    f=input("Enter Name: ")
                    print("Mobile number: 923*****56")
                    print("Email ID: ja****.com")
                elif b==3:
                    while True:
                        print("1. Edit Name: ")
                        print("2. Edit phone number: ")
                        print("3. Edit email address: ")
                        
                        g=int(input("Select an option 1-3: "))
                        
                        if g==1:
                            h=input("Edit Name: ")
                            print(h)
                        if g==2:
                            i=input("Edit phone number: ")
                            print(i)
                        if g==3:
                            j=input("Edit Email ID: ")
                            print(j)
                        print("SAVED EDITED DETAILS") 
                        break
                elif b==4:
                    k=input("Enter Name: ")
                    print("Mobile number: 923*****56")
                    print("Email ID: ja****.com")
                elif b==5:
                    l=input("Enter Name: ")
                    while True:
                        print("1. Contact Deleted")
                        print("2. NO, Contact Deleted")
                        
                        m=int(input("Select an option 1-2: "))
                        
                        if m==1:
                            print("Contact Deleted")
                        elif m==2:
                            print("NO CHANGES")
                        break    
                break
            
    elif a==3:
        print("Exiting from Contact Book")
    break    
        
    

        
        