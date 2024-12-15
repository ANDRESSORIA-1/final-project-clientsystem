import pickle

class Person:
    def __init__(self, person_name='', dob='', gender=''):
        self.person_name = person_name
        self.dob = dob
        self.gender = gender

    def add_person(self):
        self.person_name = input("Enter Name: ")
        self.dob = input("Enter Date of Birth (YYYY-MM-DD): ")
        self.gender = input("Enter Gender (M/F): ")

    def display_person(self):
        print(f"Name: {self.person_name}")
        print(f"Date of Birth: {self.dob}")
        print(f"Gender: {self.gender}")


class Client(Person):
    def __init__(self, person_name='', dob='', gender='', phone_number='', email_address='', client_id=''):
        super().__init__(person_name, dob, gender)
        self.client_id = client_id
        self.phone_number = phone_number
        self.email_address = email_address

    def add_client(self):
        self.add_person()
        self.client_id = input("Enter Client ID: ")
        self.phone_number = input("Enter Phone Number: ")
        self.email_address = input("Enter Email Address: ")
        print("-------Client Added Successfully---------")

    def display_client(self):
        self.display_person()
        print(f"Client ID: {self.client_id}")
        print(f"Phone Number: {self.phone_number}")
        print(f"Email Address: {self.email_address}")


Clients = []

def save_clients(file_name, clients_list):
    try:
        with open(file_name, 'wb')as file:
            pickle.dump(clients_list,file)
            print("Clients Saved Succsfully")
    except Exception as e:
        print(f"Error Savings Clients:{e}")

def load_clients(file_name):
    try:
        with open(file_name,'rb')as file:
            return pickle.load(file)
    except FileNotFoundError:
        print("No saved clients found. Starting with an empty list.")
        return []
    except EOFError:
        print("File is empty or corrupted. Starting with an empty list.")
        return []
    except Exception as e:
        print(f"Error loading clients: {e}")
        return []


def menu():
    print("--- Menu ---")
    print("1. Add a Client")
    print("2. Display Clients")
    print("3. Modify Client")
    print("4. Exit")

Clients= load_clients("clients.dat")

while True:
    menu()
    choice = input("Enter a choice (1-4): ")

    if choice == "4":
        save_clients("clients.dat",Clients)
        print("Thanks for using the system!")
        break

    elif choice == "1":
        c = Client()
        c.add_client()

        if any(client.client_id == c.client_id for client in Clients):
            print("Client ID already exists. Please use a unique ID.")
        else:
            Clients.append(c)

    elif choice == "2":
        if not Clients:
            print("No clients to display.")
        else:
            for client in Clients:
                client.display_client()

    elif choice == "3":
        user_to_modify = input("Enter Client ID to modify: ")
        if not Clients:
            print("No clients available.")
            continue

        found = None
        for client in Clients:
            if client.client_id == user_to_modify:
                found = client
                break

        if found:
            print("Client found! Please enter new details.")
            found.add_client()
        else:
            print("Client not found.")

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")



