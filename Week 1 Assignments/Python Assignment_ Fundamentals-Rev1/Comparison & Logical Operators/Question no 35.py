# Use the or operator to check if a user is either "Admin" or "Superuser". 

x = input("Who are you? ")

if x.lower() == "admin" or x.lower() == "superuser":

    if x.lower() == "admin":    
        
        print("User is Admin")

    else:

        print("User is Superuser")

else:

    print("User is no one")