file = open(r"C:\Users\sherr\Desktop\code-lab\python-io\file.txt")
lines = file.readlines()
print(lines)
file.close()
# output:
# ['this is a test file.\n', ':)\n', 'I want to test if it works.\n', 'that is all.\n']
# output is a list!

with open(r"C:\Users\sherr\Desktop\code-lab\py-io\file.txt", mode="r") as f:
    contents = f.readlines()
print(contents)
