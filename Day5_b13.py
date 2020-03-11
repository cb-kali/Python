# Removing element from the list
# Syntax del.list[index_value]
Lang = ['Python','C','C++','Java','Html','Php','Ruby']
print(Lang)
del Lang[4] # remove Html
print(Lang) # check
# Removing an element by using pop method
# Syntax list.pop() and list.pop(index_value)
print(Lang.pop()) # It's remove last elment
print(Lang.pop(3)) # It's remove index_value element
print(Lang)
# Organising list
Name = ['Udit','Chetan','Aman','Anu','Roshan','Akash']
print(Name)
''' req : we want to organis the list in an alphabetic oder 
A-Z''' # This is  also comment
# Two type's first temp and second perment
# Temp -----> sorted
print(sorted(Name)) # check this above list
# Perment ----> sort
Name.sort() # It's also same but it perment
print(Name)
#print(Name) # check
# How to do the reverse sorting:
Name.sort(reverse=True)
print(Name)
