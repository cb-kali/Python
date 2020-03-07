# Introduction of list
# syntax list = ['str',int,]
# Creact a list
Lang = ['Python','C++','Java','Php','C','Kotlin','Ruby']
print(Lang)
# I want print C++ 
print(Lang[1]) # In progrmaing start 0
# This is '+' indexing 
# I want print Kotlin usind '-' indexing 
print(Lang[-2]) # '-' Indexing start -1
# Check data type Lang
print(type(Lang))

# I want append my list 
Lang.append('Html')
print(Lang) # Check
# I want remove Html
Lang.remove('Html')
print(Lang) # Check
# I want insert a one element in 2nd position (0,1,2)
Lang.insert(2,'Html')
print(Lang)
# how to modify element I Updata 'C'
Lang[-3] = 'Swift'
print(Lang) # Check

