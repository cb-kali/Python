courses = ['CEH','Python','Red_Hat','Web_Developer','CCNA','Java']
# I want count element in a list then I use len
print(len(courses)) # To find out the number of element are there in our list 

# Introduction of For Loop ** Is a important topice
# Loop ----> Which will be incuring underitself
# Terminalogy for understuding for loop :
# Main variable ----> courses
# Temp variable ----> any_name or any_character I choose 'a'
# Creating the indentation ----> : --> colen

for a in courses:
	print(a)

# Syntax ---> for temp_variable (a) in main_variable (courses):
#	print(temp_variable) var = variable

# Enharcenment of the for loop with the actual req :

for a in courses:
	print(f"{a}, These courses best for me ")

# Making numcrical list by using the for loop
# Bulti in method ----> range() ---> start value and stop value

for num in range(1,10): # Last number (10) is alway exclusive
	print(num)

numbers = list(range(1,20))
print(numbers)

# I want to print only even number for 1-100
even_number = list(range(2,100,2))
print(even_number)
# rang(start_value, stop_value, step_count) 
# I want to print only odd number for 1-100
odd_number = list(range(1,100,2))
print(odd_number)

# Find out min value in odd number
print(min(odd_number))
# Find out max value in odd number
print(max(odd_number))
# I want sum of all odd number in 1-100
print(sum(odd_number))

# Type and print element 
OS = ['Window','Linux','Mac']
print(type(OS))
print(OS[0:2])

