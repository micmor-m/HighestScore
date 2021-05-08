# Get scores from user
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

max_val = 0
for n in range(0, len(student_scores)):
    if student_scores[n] > max_val:
        max_val = student_scores[n]

print(max_val)