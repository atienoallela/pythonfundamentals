classnames = ["Zeal", "Francis", "Shelmith", "Adam", "Daphne"]

for i in classnames:
    if i == "Adam":
        break
    print(i)

for j in classnames:
    print(j)

# looping through a string

for a in "Allela":
    print(a)

users = ["Da", "De", "Di"]

print("Users created are ", users)

while True:
    new_user = input("Do you want to add more users? (Y/N)").upper()

    if new_user == "N":
        break
    elif new_user == "Y":
        user = input("Enter new user details :")
        users.append(user)
    else:
        print("Chose any of the options given")

for usersera in users:
    print(usersera)
