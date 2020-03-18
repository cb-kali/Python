# Looping through all the value in the dictionary:
user_0 = {'UserName':'Chetan','FirstName':'Chetan','LastName':'Bansal'}
print(user_0)
# Data type
type(user_0)
# Normal for loop cond :
'''
for tempvar in mainvar:
    print(tempvar)
'''
for key,value in user_0.items():
    print(f"\n key : {key}")
    print(f" value : {value}")
# Same example but diffrent tempvar :
for a,b in user_0.items():
    print(f"\n key : {a}")
    print(f"\n value : {b}")
# Req ---> I want to get only key, no value are needed
for a in user_0.keys():
    print("Key : ",a)
# Req ---> I want to get only values, no key are needed
for b in user_0.values():
    print("Value : ",b)
Fav_lang ={"Chetan":"Python","Roshan":"Java","Aman":"C","Vishal":"C++"}
print(Fav_lang)
# req ---> To print and loop through the dict is a particular order:
for name in sorted(Fav_lang.keys()):
    print(name.title())
# Introduction to while loop :
# Write a table of 2 using while loop 
num = 2 # Declration of a value
while num <= 20:
    print(num)
    num += 2
