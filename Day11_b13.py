# Introduction of function
''' Always keep in mind about the code resuability concept: '''
# How to define a funcation ?
'''For defining a function we have to user key word calles as "def". '''
# Req :- my function needs to greet the user. # code resusability!
def greet_user():
    ''' Display a simple grieting''' # Doc string ---> commenting inside a funcation.
    print("hello") # logic--!
greet_user() # function call
# echancment of the code : good to have you back agin.
"welcom Chetan"
def greet_user(username): # define function 
# username ---> parrmeter passing
    '''Display a simple greeting message to the user'''
    print("Good to have you back", username.title())
greet_user('chetan') # function call 
#  chetan ---> argument passing 
# Run time argument passing

# Introduction of arguments
def descibe_pet(animal_type,pet_name): # 2 parameter i have passed
    '''Display information about a pet'''
    print(f'\n I have a {animal_type}.') # logic to get better format 
    print(f'I have {animal_type} is name {pet_name.title()}.')
descibe_pet('Cat','Tom')
descibe_pet('dog','tommy') # Multiple call of a funcation 
# check output 
''' I have only pass one argument then this type errorL:-)
descibe_pet(tommy)
Traceback (most recent call last):
  File "<string>", line 28, in <module>
NameError: name 'tommy' is not defined
'''
descibe_pet('tommy','dog') # check output and check wrong sentence
descibe_pet(pet_name = 'Tommy', animal_type = 'Dog') # check output 
# Is know as keyword argu 
# argu --> argument
# Introduction of defult value : 
''' While declaring the defult value we have keep to keep it at the end of the funcation.'''
def descibe_pet(pet_name,animal_type='Dog'):
    print(f'\n I have a {animal_type}.')
    print(f'I have {animal_type} is name {pet_name.title()}.')
descibe_pet('tommy')
descibe_pet('cat','tom') # argu only missging cases at will be considering the defult value.
# create function 
# req ---> add two number:
print("\n New")
def sum(a,b):
    print(a) or print(b)
    c = a + b 
    print(" Sum of two number = ", c)
sum(4,6)
