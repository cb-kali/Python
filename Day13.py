'''
 Introduction to python class:
 Class --> it's like a blueprint of codedesing.
 class
 method --> A function writen inside a class is called a method.
 attributes --> a variable writen inside a class is called an attributes.
 Introduction of a class/object
'''
# req:-
'''
You have to create a class, it should your name as an input, it should your name as an input, it should great you as well at the end
'''
class Greet: # create name
    '''Creating a greet class for greeting an user '''
    def create_name(self,name):
        self.name = name
    def display_name(self):
        print(self.name)
    def greet_user(self):
        print(f'Hello, good to you are again in training class {self.name}')
'''
Object is the key... any thing you wanted to touch inside a class number other option
'''
# Object creation
superman = Greet()
superman.create_name('chetan')
superman.display_name()
superman.greet_user()
# OOPs concept --> object
# New object
a = Greet()
a.create_name('Anu')
a.display_name()
a.greet_user()
