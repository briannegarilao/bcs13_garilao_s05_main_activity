# briannegarilao

# Students database
students = {}

print("READ ME FIRST!")
print("Please assume that the grade that you will put on each assessment is percentage 100/100")
print('This is because this program wont be able to calculate each of the assessment as we don\'t know the maximum '
      'grade for each of them \n')

# loop for each student
for i in range(5):

    # get the Name of student
    name = input(f"Student {i+1} name: ")
    gradesCP = 0
    gradesSA = 0
    gradesFE = 0

    # loop for getting Class Participation
    for j in range(5):
        gradesCP += float(input("Class participation {}: ".format(j + 1)))

    # loop for getting Summative Assessment
    for k in range(3):
        gradesSA += float(input("Summative assessment {}: ".format(k + 1)))

    # loop for getting Summative Assessment
    for m in range(1):
        gradesFE = float(input("Final exam {}: ".format(m + 1)))

    gradesCP = (gradesCP / 5) * 0.3
    gradesSA = (gradesSA / 3) * 0.3
    gradesFE *= 0.4
    total_grade = gradesCP + gradesSA + gradesFE
    letter_grade = 'a'

    # Letter Grade converter
    if total_grade >= 90:
        letter_grade = "A"
    elif total_grade >= 80:
        letter_grade = "B"
    elif total_grade >= 70:
        letter_grade = "C"
    elif total_grade >= 60:
        letter_grade = "D"
    else:
        letter_grade = "F"

    students[name] = total_grade, letter_grade


# Print header
print(f"{'Name':<15} {'Total Grade':<15} {'Letter Grade':<10}")

# Loop through dictionary items and print in columns
for name, grades in students.items():
    total_grade = grades[0]
    letter_grade = grades[1]
    print(f"{name:<15} {total_grade:<15.2f} {letter_grade:<10}")
