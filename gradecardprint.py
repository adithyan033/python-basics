def find_grade(mark):
    if mark < 25:
        return "F"
    elif mark < 45:
        return "E"
    elif mark < 50:
        return "D"
    elif mark < 60:
        return "C"
    elif mark <= 80:
        return "B"
    else:
        return "A"


regno = input("Enter Register Number: ")

marks = []

for i in range(1, 6):
    m = int(input("Enter mark for subject " + str(i) + ": "))
    marks.append(m)

print("\nRegister Number:", regno)
print("Subject   Mark   Grade")

for i in range(5):
    grade = find_grade(marks[i])
    print("Subject", i + 1, " ", marks[i], "   ", grade)
