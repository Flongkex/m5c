inventory = {"Felix": ("123", ["Bannan","Äpple", "Kossa"])}
alive = True
def login(user_name, password):
    if user_name in inventory:
        if password == inventory[user_name][0]:
            return True
        else:
            print("Wrong password")
    else:
        print("No user found...")
        if input("Add user or try again? a/b: ") == "a":
            signup(user_name, password)
        else:
            pass
        
        
def validate(user_input):
    return user_input[0].lower()
    
   
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
            
            #logout(user_name)
            break
    
def menu1():
    print("a) login")
    print("b) quit")
    user_input = validate(str(input("")))
    if user_input == "a":
        user_name = input("användarnamn: ")
        password = input("lösen: ")
        ok = login(user_name,password)
        
        if ok:
            menu2(user_name)
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
    #print(inventory[key][1])

def add_item(key):
    item = input("Add: ")
    print(item)
    inventory[key][1].append(item)
    

    
while alive:
    alive = menu1()
#print(inventory[("Felix")][1])
#view_inventory("Felix")
#login("Niklas", "123")
#add_item("Niklas", "Godis")
#view_inventory("Niklas")

    