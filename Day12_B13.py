# Introduction of Return value's :
# Req --> To get neat formated name:
def get_formatted_name(First_name,Last_name):
    '''Return a full name neately formated'''
    full_name = f'{First_name} {Last_name} '
    return full_name.title() # To control the output 
print(get_formatted_name('chetan','bansal'))
# Return a dictionary :
def build_person(First_name,Last_name):
    '''Return a dicti of info about a person'''
    person = {'first': First_name,'last': Last_name} # creating a dicti and key by parameter as their values
    return person # retuning person!
print(build_person('chetan','bansal'))
print(build_person('udit','sharma'))
# Passing a list to funcation :
def greet(names):
    '''print a simple greeting message to the student in the list'''
    for name in names:
        msg = f'Hello, thanks for joining me {name.title()}'
        print(msg)
student = ['Udit','Roshan','Chahat','Nitin']
greet(student)
# New
def make_pizza(toping):
    '''Print the list of topping that have been reuested'''
    print(toping)
make_pizza('corn')
'''
make_pizza('corn','olives')
Error :-)
Traceback (most recent call last):
  File "<string>", line 29, in <module>
TypeError: make_pizza() takes 1 positional argument but 2 were given
'''
# Passing arbitary number of argument's
def make_pizza(*toping):
    '''Print the list of topping that have been reuested'''
    print(toping)
make_pizza('corn','olives') # check output now 
