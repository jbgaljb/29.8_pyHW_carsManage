import sqlite3
import pandas as pd
import json

# init db connection
def dbInit():
    # cars table
    conCars = sqlite3.connect("cars.py")
    curCars = conCars.cursor()

    # customers table
    conCustomers = sqlite3.connect("customers.py")
    curCustomers = conCustomers.cursor()

    return curCars, curCustomers, conCars, conCustomers

def SampleTablesInit(curCars, curCustomers):
    # initializing tables

    curCars.execute("""CREATE TABLE IF NOT EXISTS cars(
                    customer_id,
                    car_id,
                    brand,
                    model,
                    color
                    )""")
    curCustomers.execute("""CREATE TABLE IF NOT EXISTS customers(
                    id,
                    full_name,
                    telephone,
                    email
                    )""")

def demoDataToTables(conCars, conCustomers):
    # load jsons
    with open ('carsDemo.json', 'r') as file: carsData = json.load(file)
    with open ('customersDemo.json', 'r') as file: customersData = json.load(file)

    # loading to data frames
    carsDF = pd.DataFrame(carsData['cars'])
    customersDF = pd.DataFrame(customersData['customers'])

    # appending to sql tables
    carsDF.to_sql('cars', conCars, if_exists='append', index=False)
    customersDF.to_sql('customers', conCustomers, if_exists='append', index=False)

    conCars.commit()
    conCustomers.commit()

    conCars.close()
    conCustomers.close()

def main():
    curCars, curCustomers, conCars, conCustomers = dbInit()
    SampleTablesInit(curCars, curCustomers)
    demoDataToTables(conCars, conCustomers)

if __name__ == "__main__":
    main()