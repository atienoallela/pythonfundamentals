class mit:
    def __init__(self, lesson, week):
        self.classwork = lesson
        self.time = week

    def students(self):
        print(self.classwork,self.time)

name = mit("Python","3")
name.students()