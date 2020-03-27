# Introduction parent and child classes --> technical name super and sub classes
''' Reg: 2 people in a dev team
a task 1:
b tsak 2:
Req: A has to create 2 variable(attributes) inside a class
'''
class parent:
    var1 = 'Hey I am var1'
    var2 = 'Hey I am var2'
# b also has 2 to crate these attributes only!
class child(parent): # pass the parent as the parameter in the child class
    pass # do donthing just accept asitis

xobj = child()
print(xobj.var1)
# This wholwe process is termed as inheritence.
# Question: How to over ride the superclass
class child(parent):
    var2 = 'I have been modfied now'
aobj = parent()
print(aobj.var1)
print(aobj.var2)
bobj = child()
print(bobj.var1)
print(bobj.var2)
# Accessing multiple superclasses:
class Dad:
    x = 'Hey I am dad class'
class Mom:
    y = 'Hey I am mom class'
class son (Dad,Mom):
    z = 'Hey I am son class'

aobj = son()
print(aobj.x)
print(aobj.y)
print(aobj.z)
