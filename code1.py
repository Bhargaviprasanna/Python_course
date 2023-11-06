# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
print("This is a first statement")

# using seperator
print("1st statement", "2nd statement", sep="------")

# using end
print("3rd statement should be followed by 4rth", end="**")
print("this is 4rth statement")

# A single line comment and multi line comment
''' this is a multi line 
comment '''

# input from user
user_input  = input()
print(" user_input = ", user_input)
print(" user_input data_type = ", type(user_input))
