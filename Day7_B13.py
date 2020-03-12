# Introduction to user input
# Accepting the user input
Massage = input("Tell me something and your hobbies : ")
print(Massage) # user input
Name = input("Enter your name")
print("\n Welcome back to ",Name," Python tutorial's")

Age = input("How are you young")
print(Age)
Age = int(Age) # type casting ---> we arecasting the data frome str to int
print(Age)
print(Age>20) # print true or false

# Case Studt of buliding simple voting application : ( If condiction will also be included )
# 18 year's is voting criteriae : 18 or 18 above -- He/She is eligibles to vote
# Age is less than 18 year's ---> not eligible to vote.
# Start
Age = input("Enter your age : ")
if age == 18:
	print("\n You are eligible to vote")
else:
	print("\n You aren't eligible to vote")

