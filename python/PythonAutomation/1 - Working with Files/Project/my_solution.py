import csv
import datetime

products = {
    "P001": {"name": "Wireless Headphones", "price": 100},
    "P002": {"name": "Laptop Backpack", "price": 60},
    "P003": {"name": "Bluetooth Speaker", "price": 50},
    "P004": {"name": "USB Flash Drive", "price": 20},
    "P005": {"name": "Mobile Phone Case", "price": 15},
    "P006": {"name": "Wireless Mouse", "price": 30},
    "P007": {"name": "Laptop Stand", "price": 40},
    "P008": {"name": "HDMI Cable", "price": 15},
    "P009": {"name": "Smartphone", "price": 600},
    "P010": {"name": "External Hard Drive", "price": 100}
}

date_today = datetime.date.today()
product_sales = "PythonAutomation/3 - Working with Files/9 - Section Project - Intro/product_sales.txt"
product_sales_output = "PythonAutomation/3 - Working with Files/9 - Section Project - Intro/product_sales_output.csv"
product_list = []
insert_dates = []
curr_id = 1

# read the product ids and put them into a list
with open(product_sales, "r") as sales_date:
    content = sales_date.readlines()
    for line in content:
        product_list.append(line.strip())

# create a new list to hold the data for csv file
for product_id in product_list:
    item = []

    item.append(date_today)
    item.append(curr_id)
    item.append(product_id)
    item.append(products[product_id]["name"])
    item.append(products[product_id]["price"])

    insert_dates.append(item)

    curr_id += 1

# write data to csv file
with open(product_sales_output, 'w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(
        ["current_date", "sale_id", "product_id", "name", "price"]
    )
    csv_writer.writerows(insert_dates)
