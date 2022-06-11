names = ['Peter Parker', 'Clark Kent' , 'Brauce Wayne']
heroes = ['Spiderman', 'Superman', 'Batman']

#Connect 2 lists
for name,hero in zip(names ,heroes):
    print(f'{name} is actually {hero}')

#print lndex list
names = ['Dana', 'Moshe', 'Avi']
for index, name in enumerate(names , start=1):
    print(index,name)


#print sqaure number of list
nums = [11, 30, 44, 54]

for num in nums:
    square = num ** 2
    print(square)