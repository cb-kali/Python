# Adding white space to strings
print("Normal")
print("\tNormal")
# \t -----> use to tab delimeter
print("\n\tNormal\n\tNormal1")
# \n -----> use to new line delimeter
print("Example of t and n  use in one line : ")
print("Name : \n\t Chetan \n\t Udit \n\t Aman \n\t Anjali")

# strinpping of white space !
Fav_Lang = " Python" # left side space
print(Fav_Lang)
Fav_Lang1 = "C++ " # right side space
print(Fav_Lang1) # check above Fav_Lang and This

# Show to eliminate the space
print(Fav_Lang.lstrip()) # The lstrip() method removes any leading characters (space is the default leading character to remove)
print(Fav_Lang.rstrip()) # The rstrip() method removes any trailing characters (characters at the end a string), space is the default trailing character to remove.
print(Fav_Lang.strip()) # The strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end) characters (space is the default leading character to remove)

# Introduction to opration is number
# int ----> integer
print(3+5) # print use for print this statment

# squaring of the number
print(4**2)
# Decimal --> techniacl name ---> Float data type
# How to check data types
A = 30
B = 20
X = A+B
print(X)
print(type(X)) # check data types
a = "xyz"
print(type(a)) # i'm using print because print datatypes
# str --> string
