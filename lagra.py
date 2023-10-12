
class Lagra:
    def __init__(self):
        self.users = {"Felix": "123"}
        self.inventory = {"Felix": ["Bannan", "Äpple", "Kossa"]}  # denna var bara för test ska tömmas sen
        self.current_user = None
        self.alive = True

    def validate_user_login(self, user_name, password):
        if user_name in self.inventory:
            if password == self.users[user_name]:
                self.current_user = user_name
                return True
            else:
                return False
        else:
            print("User was not found")
            if input("Add user or try again? a/b: ") == "a":
                self.signup(user_name, password)
                return True
            else:
                pass

    # Ändrar användarens input till lite bokstav för att undvika fel
    def validate(self, user_input):
        return user_input[0].lower()

    # Skapar en ny key med tomt inventory i dictonaryn,
    def signup(self, user_name, password):
        self.users[user_name] = password
        self.inventory[user_name] = []
        self.current_user = user_name

    def menu2(self):
        while True:
            print("a) Add item")
            print("b) View Inventory")
            print("c) logout")

            user_input = self.validate(input())

            if user_input == "a":
                self.add_item()
                return True
            elif user_input == "b":
                self.view_inventory()
                return True
            elif user_input == "c":
                self.logout()
                return False
                # menu1()

    def signin(self):
        while True:
            user_name = input("användarnamn: ")
            password = input("lösen: ")

            successful_login = self.validate_user_login(user_name, password)
            if successful_login:
                print(f"Välkommen {self.current_user}\n")
                stay_logged_in = self.menu2()
                if stay_logged_in:
                    break

            else:
                prompt_retry = input("Incorrect password... \n Try again? (y/n) ")
                if prompt_retry == "n":
                    break

    def menu1(self):
        print("a) login")
        print("b) quit")
        user_input = self.validate(input())
        if user_input == "a":
            return True

        else:
            return False

    def logout(self):
        self.current_user = None

    # Printar hur många items vi har och sedan printas alla items ut radvis
    def view_inventory(self):
        user_inventory = self.inventory[self.current_user]
        print(f"These are your {len(user_inventory)} items")
        for i, n in enumerate(user_inventory):
            print(f"{i+1}) {n}")

    def add_item(self):
        item = input("Add: ")
        self.inventory[self.current_user].append(item)

    def start(self):
        while self.alive:
            if self.current_user:
                self.menu2()
            else:
                if self.menu1():
                    print(self.current_user)
                    self.signin()
                else:
                    break
    

g = Lagra()

g.start()
# print(inventory[("Felix")][1])
# view_inventory("Felix")
# login("Niklas", "123")
# add_item("Niklas", "Godis")
# view_inventory("Niklas")

    