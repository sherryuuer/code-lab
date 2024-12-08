import csv

input_file = "PythonAutomation/3 - Working with Files/8 - Transferring and Transforming Data in Text Files/dad_jokes.csv"
output_file = "PythonAutomation/3 - Working with Files/8 - Transferring and Transforming Data in Text Files/dad_jokes_categoried.csv"


def rating_category(rating):
    rating = int(rating)

    if rating <= -3:
        category = 'abysmal'
    elif rating <= -1:
        category = 'awful'
    else:
        category = 'bad'

    return category


# my solution
with open(input_file, "r") as input_file:
    line_generator = csv.reader(input_file)

    column_names = next(line_generator)
    column_names.append("rating_category")

    with open(output_file, "a", newline='') as output_file:
        csv_writer = csv.writer(output_file)

        csv_writer.writerow(column_names)

        for row in line_generator:
            row.append(rating_category(row[2]))
            csv_writer.writerow(row)

            print(f"wrote line {row} to output file.")
