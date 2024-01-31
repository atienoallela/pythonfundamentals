# print("Atieno Allela")

# keyword is def - definition , function name , parameters

def username():
    print("Allela")


username()


# passing arguements in my function

def full_name(fname, lname):
    print(fname + " " + lname)


full_name("Atieno", "Allela")
full_name("Junior", "Allela")
full_name("Cavin", "Allela")

# write a function that takes in three arguments and prints it out ..Data type for these args are integers
def calc(x,y,z):
    print(x*y*z)

calc(10,8,4)
calc(19,8,4)

#writing a reusable function

def welcome_message(firstname,lastname):
    print(f"Hello {firstname} {lastname} welcome to eMobilis Class on Python Fundamentals")

welcome_message("Godius","Kirwa")
welcome_message("Hope","Cherono")

#write function that takes up fname , lname and age and displays when called 
