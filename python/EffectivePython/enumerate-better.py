# enumerate
# iterator
# lazy generator
boys = ['yaya', 'bard', 'yoshi']
it = enumerate(boys)
print(next(it))
print(next(it))

# second para is the start index!
for i, boy in enumerate(boys, 1):
    print(i, boy)
