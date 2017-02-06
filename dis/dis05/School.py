class Instructor:
    degree = "PhD (Magic)" # this is a class attribute
    def __init__(self, name):
        self.name = name # this is an instance attribute
    def lecture(self, topic):
        print("Today we're learning about " + topic)

dumbledore = Instructor("Dumbledore")

class Student:
    instructor = dumbledore
    def __init__(self, name, ta):
        self.name = name
        self.understanding = 0
        ta.add_student(self)
    def attend_lecture(self, topic):
        Student.instructor.lecture(topic)
        print(Student.instructor.name + " is awesome!")
        self.understanding += 1
    def visit_office_hours(self, staff):
        staff.assist(self)
        print("Thanks, " + staff.name)

class TeachingAssistant:
    def __init__(self, name):
        self.name = name
        self.students = {}
    def add_student(self, student):
        self.students[student.name] = student
    def assist(self, student):
        student.understanding += 1

def test():
    '''
    >>> snape = TeachingAssistant("Snape")
    >>> harry = Student("Harry", snape)
    >>> harry.attend_lecture("potions")
    Today we're learning about potions
    Dumbledore is awesome!
    >>> hermione = Student("Hermione", snape)
    >>> hermione.attend_lecture("herbology")
    Today we're learning about herbology
    Dumbledore is awesome!
    >>> hermione.visit_office_hours(TeachingAssistant("Hagrid"))
    Thanks, Hagrid
    >>> harry.understanding
    1
    >>> snape.students["Hermione"].understanding
    2
    >>> Student.instructor = Instructor("Umbridge")
    >>> Student.attend_lecture(harry, "transfiguration")
    Today we're learning about transfiguration
    Umbridge is awesome!
    '''
    pass
