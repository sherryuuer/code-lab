# read file content
# read lines
import csv
with open('file.txt', 'r') as file:
    lines = file.readlines()

    for line in lines:
        print(line.strip())

# append to file
additional_lines = ['new line 1,\n', 'new line 2']

with open('file.txt', 'a') as file:
    # file.write('new line 1,\n')
    # file.write('new line 2,\n')
    file.writelines(additional_lines)

# read csv
with open('file.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)
    for row in csv_reader:
        joke = row[1]
        rating = row[2]
        print(f'"{joke}" has a rating of {rating}.')

# write csv
