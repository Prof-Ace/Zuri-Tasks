class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        print(f" name-{name}, age-{age}, track-{tracks}, score-{score}")

    def changeName(self, newname):
        self.changeName = newname
        print(f" The name of the new student is {newname}")
    def changeAge(self, age):
        print(f" The student is  {age} years old")
    def addTrack(self, tracks):
        print(f" The student is in the {tracks} track")
    def getScore(self, score):
        print(f" And the student scored {score}")
        
        
        
Bob = Student(name="Bob",age= 26, tracks=["FE","BE"], score=20.90)

# Expected methods
Bob.changeName("Peter")
Bob.changeAge(34)
Bob.addTrack("UI/UX")
Bob.getScore(20.90)