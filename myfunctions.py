# print("Atieno Allela")
import module as k

# keyword is def - definition , function name , parameters
print(k.sub(9, 6))


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
def calc(x, y, z):
    print(x * y * z)


calc(10, 8, 4)
calc(19, 8, 4)


# writing a reusable function

def welcome_message(firstname, lastname):
    print(f"Hello {firstname} {lastname} welcome to eMobilis Class on Python Fundamentals")


welcome_message("Godius", "Kirwa")
welcome_message("Hope", "Cherono")


# write function that takes up fname , lname and age and displays when called

# functions can either perform a task or return a value

def calcit(x):
    return 10 * x


print(calcit(19))
print(calcit(8))
print(calcit(9))


# return to give value of two numbers

def addition(x, y):
    return x + y


z = addition(5, 9)
print(z)

name = input("What is your name ?")
weight = float(input("Enter weight here : "))
height = float(input("Enter height here : "))


def bmicalc(name, weight, height):
    my_bmi = weight / (height * height)
    if (my_bmi <= 20):
        return f" {name} is underweight", my_bmi
    elif (my_bmi <= 30):
        return f" {name} need to eat more proteins ", my_bmi
    elif (my_bmi <= 40):
        return f" {name} needs to  workout ", my_bmi
    else:
        return f" {name} needs to a doctor ", my_bmi


my_bmi = bmicalc(name, weight, height)
print(f"{my_bmi}")


# write a grading function based on input from user that calculates the average of three subjects
# Accept name and print name
# A - 85 , B  - 70 , C - 60 ,D - 50 , E- 40

def avg_grade(marks):
    tots = len(marks)
    total_score = sum(marks)
    avg = total_score / tots
    return avg


# function to grade

def grading(avg):
    if avg >= 85:
        grade = "A"
    elif avg >= 70:
        grade = "B"
    elif avg >= 60:
        grade = "C"
    elif avg >= 50:
        grade = "D"
    elif avg <= 40:
        grade = "E"
    else:
        print("Value below entry points")


marks = [80, 73, 78, 21, 89, 59, 49]
avg = avg_grade(marks)
print("Allelas average grade is ", avg)
