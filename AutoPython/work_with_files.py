# read file content
# read lines
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
