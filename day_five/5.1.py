student_heights = input("Input a list of student heights: ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])


# total_heigt = sum(student_heights)
# this is how it work
total_height = 0
for height in student_heights:
    total_height += height
print(total_height)

# numberOfStudents = len(student_heights)
# this is how the above function works
numberOfStudents = 0
for student in student_heights:
    numberOfStudents += 1
print(numberOfStudents)
