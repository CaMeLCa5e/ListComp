# #!/usr/bin/env python 

# """List comprehension in Python"""

# new_list = []
# for i in old_list:
# 	if filter(i):
# 		new_list.append(expression(i))

# #______

# new_list = [expression(i) for i in old_list if filter(i)]


# [expression for item in lst if x >= 3 ]

# fir item in lst:
# 	if conditional:
# 		expression 

# new_list = [expression (i) fir i in old_list if filter(i)]


x = [i for i in range(10)]
print x

squares = []

for x in range(10):
	squares.append(x**2)

print squares
[0,1,2,3,4,5,6,7,8]

squares = [x**2 for x in range(10)]

print squares
[0,2,3,4,5,6,7,8,9,0]






list1 = [2,3,4,5]

multiplied = [item*3 for item in list1]

print multiplied
[9,12,15]

listOfWords = ['this', 'is', 'a', 'list']

items = [word[0]for word in listOfWords]

print items


x.lower() for x in ['a', 'B', 'C']
print x

[x.upper() for x in ['a', 'b', 'c']]
























