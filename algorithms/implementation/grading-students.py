def solve(grades):
    for grade in grades:
        if grade < 38:
            print(grade)
        else:
            temp = grade
            while temp % 5 != 0:
                temp += 1
            if temp - grade < 3:
                grade = temp
            print(grade)
            

n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))
