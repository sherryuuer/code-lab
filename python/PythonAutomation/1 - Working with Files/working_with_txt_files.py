# bash should in PythonAutomation/1 - Working with Files
file_path = 'dad_jokes.txt'
# 打开txt文件，不使用with
file = open(file_path, 'r')
content = file.read()
# print(content)
file.close()

# 读取txt文件的每一行
with open(file_path, 'r') as file:
    lines = file.readlines()

    for line in lines:
        pass
        # print(line.strip())

# 写入文件
# additional_lines = ['Stars up above,\n', 'Whisper words of love']

# with open(file_path, 'a') as file:
#     file.write('The sun is bright,\n')
#     file.write('On this lovely night,\n')
#     file.writelines(additional_lines)

# 写入一个新的txt文件
with open('poem.txt', 'w') as file:
    file.write('Roses are red,\n')
    file.write('Violets are blue,\n')
    file.write('Sugar is sweet,\n')
    file.write('And so are you!,\n')
