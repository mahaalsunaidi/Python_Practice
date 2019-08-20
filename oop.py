class Person:

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


class Student(Person):


class Lecturer(Person):
    def __init__(self, faculty, department, officeno, phoneno, email):
        self.faculty = faculty
        self.department = deparment
        self.officeno = officeno
        self.phoneno = phoneno
        self.email = email


if __name__ == '__main__':
    std1 = Student("Maha", "Female")
    lec1 = Lecturer("CCIS", "SE", "W361", "0096645382", "xxx@psu.edu.sa")
