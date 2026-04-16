import re
a = input("Enter password: ")

if len(str(a))<8:                
    print("Password too short")
else:
    b = re.search(r'[a-z]', a)    
    c = re.search(r'[A-Z]', a)      
    d = re.search(r'[0-9]', a)    
    e = re.search(r'[@#$%^&*]', a)    


    if b and c and d and e:
        print("Strong Password")
    elif b and c and d:                
        print("Medium password")
    else:
        print("Weak Password")
