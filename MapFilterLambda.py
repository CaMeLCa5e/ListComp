"""This is an outline of the properites of the map(), 
filter(), and lambda() functions.  
This functionality also applies to list comprehensions.  
"""

"""map() is a function applies a function to every member of an iterable 
and returns the result. 
"""
def square(x):
	return x**2
	
squares = map(square, range(10))
print squares

"""this is another example using the map() function.  
The function len() is applied to every item in the list. 
"""
names = ['Bill', 'Mary', 'Joe', 'Susan']
lengths = map(len, names)
print lengths


"""lambda() is used as an anonymous/nameless function that takes one argument.  
 rather than needing to create a function called square like in example 1, 
 lambda can replace this. """ 

print (lambda x: x**2)(5)

print (lambda x: x.startswith('G')) ('Greg')


"""filter() takes a function and applies a new function based on bool 
arguments that pass as True. Here is an example using names of people 
and only printing True values."""

people = ['Bill', 'Chris', 'Beth', 'Jamie', 'Sam', 'Susan', 'John']

# For evaluating people with J names, we would write:

def starts_with_j(name):
	if name[0] == 'C':
		return True
	return False 

# To run the function, we would write- 

starts_with_j_list = filter(starts_with_j, people)
print starts_with_j_list

# This should return: 'Jamie', and 'John'.

"""These examples can all be done in a similar manner by using list comprehensions.  
A list comprehension is outlined as:
[expression-involving-loop-variable for loop-variable in sequence]
"""

# example 1

squares = [x**2 for x in range(10) ]
print squares

# Example calling on names 
print [len(name) for name in names]

# Example using list comprehension instead of filter()

names = ['Bill', 'Mary', 'Joe', 'Susan', 'Sammy']
s_names = [name for name in names if name.startswith('S')]
print s_names




