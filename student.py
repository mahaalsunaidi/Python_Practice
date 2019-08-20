class Student:

    def __init__(self, ID, name, faculty, major, course, avg):
        self.ID = ID
        self.name = name
        self.faculty = faculty
        self.major = major
        course = {}
        self.avg = avg

    def printinfo(self, ID, name, faculty, major):
        return self.ID + " " + self.name + " " + self.faculty + " " + self.major

    def average(self):
        return


if __name__ == '__main__':
    std1 = Student("113334", "Atheer", "CCIS", "SE")
    std.printinfo()
