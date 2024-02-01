class learners:
    def __init__(self, firname, lastname):
        self.jina = firname
        self.alaa = lastname

    def student(self):
        print(self.jina, self.alaa)


name = learners("Atieno", "Allela")
name.student()


# create a class that takes up three inputs in the child class

class Mtu:
    # invoke
    def __init__(self, username):
        self.username = username

    # another function to retrieve name

    def getusername(self):
        return self.username

    def isstudent(self):
        return False


class StudentInfo(Mtu):
    def isstudent(self):
        return True


std = Mtu("Hope")
print(std.getusername(), std.isstudent())

std = StudentInfo("Hope2")
print(std.getusername(), std.isstudent())
