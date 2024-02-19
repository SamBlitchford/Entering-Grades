# ___________________________________________
# CmpSci 132 | Sam Blitchford | Spring 2024
# ___________________________________________
class CmpS132Grades:
    gradeList = []
    validGrades = []
    invalidGrades = []
    gradeTotal = 0
    invalidTotal = 0
    validTotal = 0
    lowest = 0
    highest = 0
    average = 0
    gradeLetters = []
    scores = [93.0, 90.0, 87.0, 83.0, 80.0, 77.0, 70.0, 60.0]
    letters = ["A", "A-", "B+", "B", "B-", "C+", "C", "D", "F"]
    gradePoints = [4.00, 3.67, 3.33, 3.00, 2.67, 2.33, 2.00, 1.00, 0.00]
    gradePointsTotal = 0

    def __init__(self, gradeList):
        self.gradeList = gradeList
        for score in gradeList:
            if 0 <= score <= 100:
                self.validGrades.append(score)
            else:
                self.invalidGrades.append(score)
            self.gradeTotal += score
        for score in self.validGrades:
            self.validTotal += score
        for score in self.invalidGrades:
            self.invalidTotal += score
        self.lowest = sorted(self.validGrades)[0]
        self.highest = sorted(self.validGrades)[-1]
        self.average = self.validTotal / len(self.validGrades)
        for score in self.validGrades:
            pos = 0
            lastNum = 100
            for number in self.scores:
                if lastNum >= score >= number:
                    self.gradeLetters.append(self.letters[pos])
                    break
                elif pos == 7:
                    self.gradeLetters.append('F')
                pos += 1
                lastNum = number
            pos = 0
            for grade in self.gradeLetters:
                for letter in self.letters:
                    if grade == letter:
                        self.gradePointsTotal += self.gradePoints[pos]
                        pos = 0
                        break
                    pos += 1

    def getGradePoints(self):
        print(self.gradePointsTotal)

    def getGPA(self):
        print(self.gradePointsTotal / (len(self.validGrades) * 3))

    def getAverage(self):
        return self.average

    def getLowestScore(self):
        return self.lowest

    def getHighestScore(self):
        return self.highest

    def __str__(self):
        return ("Initial List: " + str(self.gradeList) + "\nGrade Total: " + str(self.gradeTotal) + "\nValid List: " +
                str(self.validGrades) + "\nInvalid List: " + str(self.invalidGrades))


def enterGrades():
    grade = ""
    gradeList = []
    while not grade == -1:
        grade = int(input("Enter Grade:\n"))
        if not 0 <= grade <= 100:
            print("Invalid Number")
        gradeList.append(grade)

    gradeList.pop(-1)
    return gradeList
