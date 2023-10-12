inventory = {"Felix": ("123", ["Bannan","Äpple", "Kossa"])} # denna var bara för test ska tömmas sen
alive = True

# 
def login(user_name, password):
    if user_name in inventory:
        if password == inventory[user_name][0]:
            return True
        else:
            return False
    else:
        print("No user found...")
        if input("Add user or try again? a/b: ") == "a":
            signup(user_name, password)
        else:
            pass
        
        
# Ändrar användarens input till lite bokstav för att undvika fel
def validate(user_input):
    return user_input[0].lower()
    
   
# Skapar en ny key med tomt inventory i dictonaryn, 
def signup(user_name, password):
    inventory[user_name] = (password, [])   

def menu2(user_name):
    while True:
        print("a) Add item")
        print("b) View Inventory")
        print("c) logout")
        
        user_input = validate(str(input("")))
        
        if user_input == "a":
            add_item(user_name)
        elif user_input == "b":
            view_inventory(user_name)
        elif user_input == "c":
            return False
            #menu1()
            #logout(user_name)
            
    
    
def signin():
        while True:
            user_name = input("användarnamn: ")
            password = input("lösen: ")
        
            ok1 = login(user_name,password)
            if ok1:
                ok3 = menu2(user_name)
                if ok3 == False:
                    break
            else:
                ok2 = input("Incorrect password... \n Try again? (y/n) ")
                if ok2 == "n":
                    break
            
                    

def menu1():
    print("a) login")
    print("b) quit")
    user_input = validate(str(input("")))
    if user_input == "a":
        return True
            
    else:
        return False
    
    

def logout():
    pass

def view_inventory(key):
    i = 1
    print(f"These are your {len(inventory[key][1])} items")
    for n in inventory[key][1]:
        print(i, n)
        i+=1
    

def add_item(key):
    item = input("Add: ")
    print(item)
    inventory[key][1].append(item)
    

    
while alive:
    if menu1():
        signin()
    else:
        break
    

#print(inventory[("Felix")][1])
#view_inventory("Felix")
#login("Niklas", "123")
#add_item("Niklas", "Godis")
#view_inventory("Niklas")

    