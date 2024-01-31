print("My name is Allela")
# the data type of line one is a string
print(15 + 20)
# line 3 is addition of 15 and 20
# line 4 we learnt how to subtract
print(10.5 - 10.3)
# division in python
print(24 / 6)
# multiplication in python
print(5 * 6)
# modulus
print(16 % 3)

classes = 5
students = 24
print(students)
print(classes * students)

accounts = 3360
year = 12
results = accounts * year
print(results)
# print(type(results))
# print results in a string
print("I have saved up to $" + str(results) + " in " + str(year))

# list as an array
# characteristics of a list
# Allows duplicate data , is ordered and can be changed

studentnames = ["Martin", "Shelmith", "Zeal", "Daphne", "Francis", "Lewis", "Francis", "Adam", "Wisdom"]
print(studentnames)
print(len(studentnames))
print(studentnames[4])
print(studentnames[-1])
print(studentnames[2:5])
# inserting values at a specific position
studentnames.insert(1, "Newton")
print(studentnames)
# extending a list

stude = ["Evans", "Godius", "Vincent", "Caleb", "Lewis", "JR"]

studentnames.extend(stude)
print(studentnames)
# removing object from list
studentnames.remove("JR")
print(studentnames)
studentnames.pop(2)
print(studentnames)
del studentnames[1]
print(studentnames)
# tuple as an array
# characteristics of a tuple is that it is ordered and UNCHANGEABLE
# tuples use normal brackets while lists use square brackets
# allows for multiple data types

studenttup = ("Martin", "Shelmith", "Zeal", "Daphne", "Francis", "Lewis", "Francis", "Adam", "Wisdom")
studentage = (17, 18, 14, 14, 13, 15, 16, 13, 14)
print(studenttup)

classnames = list(studenttup)
print(classnames)
# dictionaries are ordered , changeable and dont allow duplicates
# used when you pair values

denise = {
    "firsname": "Allela",
    "lastname": "Atieno",
    "age": 16,
    "devices": ["MacBook", "ThinkPad", "A dog"]
}
print(denise)
jemmy = dict(firstname="Jemimah", lastname="Kavyu", age=22)
print(jemmy)
individual = jemmy.get("age")
jemmy["height"] = "short"
print(jemmy)

#sets are unchangeables and unordered
#with sets I will use curly brackets

studentset = {17, 18, 14, 14, 13, 15, 16, 13, 14}
print(studentset)

