from enum import Enum
import sqlite3
import uuid

class Selection(Enum):
    ADD = 1
    DELETE = 2
    VIEW = 3
    EXIT = 6

def checkCustomerExists(id):
    cursorCustomers.execute("""SELECT id FROM customers""")
    result = cursorCustomers.fetchall()
    for idC in result:
        if(idC[0] == id):
            return True
    return False

def addCars():
    id = input("provide the customer id: ")
    if(checkCustomerExists(id)):
        
        brand = input("provide the brand name: ")
        model = input("provide the model name: ")
        color = input("provide the color: ")
        car_id = str(uuid.uuid4())

        cursorCars.execute("""
        INSERT INTO cars (customer_id, car_id, brand, model, color) 
                                VALUES (?, ?, ?, ?, ?)""", (id, car_id, brand, model, color))

        connCars.commit()
    else:
        print("Bite me, there is no customer with this ID")
    

def deleteCars():
    
    car_id = input("Provide the car ID to be deleted: ")
    cursorCars.execute("DELETE FROM cars WHERE car_id = ?", (car_id,))
    connCars.commit()
    
    # Check if the delete was successful by checking the number of affected rows
    if cursorCars.rowcount == 0:
        print(f"No car found with car_id provided")
    else:
        print(f"Car with ID {car_id} was deleted.")


# prints all cars
def viewCars():
    cursorCars.execute("SELECT * FROM cars")
    cars = cursorCars.fetchall()

    column_names = [description[0] for description in cursorCars.description]

    # Print column names
    print("Cars Table:")
    print(" | ".join(column_names))
    print("-" * 40)  # Separator for better readability
    
    # Print each row of data
    for car in cars:
        print(" | ".join(str(value) for value in car))


def addCustomers():
    name = input("provide the customer name: ")
    email = input("provide the email: ")
    phone = input("provide the phone number: ")
    id = str(uuid.uuid4())
    cursorCustomers.execute("""
    INSERT INTO customers (id, full_name, telephone, email) 
                            VALUES (?, ?, ?, ?)""", (id, name, phone, email))

    connCustomers.commit()

def deleteCustomers():
        
    customer_id = input("Provide the customer ID to be deleted: ")
    cursorCustomers.execute("DELETE FROM customers WHERE id = ?", (customer_id,))
    connCustomers.commit()
    
    # Check if the delete was successful by checking the number of affected rows
    if cursorCustomers.rowcount == 0:
        print(f"No customer found with ID provided")
    else:
        print(f"Customer with ID {customer_id} was deleted.")

# prints all customers
def viewCustomers():
    cursorCustomers.execute("SELECT * FROM customers")
    customers = cursorCustomers.fetchall()

    column_names = [description[0] for description in cursorCustomers.description]

    # Print column names
    print("Customers Table:")
    print(" | ".join(column_names))
    print("-" * 40)  # Separator for better readability
    
    # Print each row of data
    for customer in customers:
        print(" | ".join(str(value) for value in customer))


def printMenu():
    for option in Selection:
        print(f"{option.value}. {option.name.lower()}")

def chooseOption(): 
    return input("which option do you choose (choose a number)? ")

def menu(carsOrCustomers): # the param takes a string: 'car' or 'customer'
    printMenu()
    choice = chooseOption()
    if (int(choice) == 4): exit()
    globals().get(f"{Selection(int(choice)).name.lower()}{carsOrCustomers}")()

def connectToDB():
    global connCars, cursorCars, connCustomers, cursorCustomers

    connCars = sqlite3.connect('cars.py') 
    cursorCars = connCars.cursor()

    connCustomers = sqlite3.connect('customers.py') 
    cursorCustomers = connCustomers.cursor()

def main():
    connectToDB()

    while True:
        print("is the action you would like to perform related to cars or customers?")
        carsOrCustomers = input("choose 'Cars' or 'Customers': ")
        menu(carsOrCustomers)

if __name__ == "__main__":
    main()