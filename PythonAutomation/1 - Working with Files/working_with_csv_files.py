import csv

# 切换位置到当前目录 PythonAutomation/1 - Working with Files
with open('dad_jokes.csv', 'r') as csv_file:
    csv_generator = csv.reader(csv_file)  # csv_file is a object as parameter

    # 这一行输出了 header
    print(next(csv_generator))  # generator
    # print(csv_generator)

    for row in csv_generator:
        joke = row[1]
        rating = row[2]
        print(f'"{joke}"; this joke has a rating of {rating}.')

# 写入文件
# 目的在于理解语言中的类，对象，方法
import csv

with open('expensive_pets.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file)

    csv_writer.writerow(['name', 'species', 'favorite_snack', 'monthly_cost'])
    csv_writer.writerow(['Max', 'Dog', 'bacon strips', 4754])

    csv_writer.writerows([['Julius', 'Cat', 'catnip', 3215],
                          ['Cal', 'Cat', 'anything edible', 71142],
                          ['Lena', 'Cat', 'Sheba', 142],
                          ['Bruiser', 'Featherfin Catfish', 'fish pellets', 54]])
