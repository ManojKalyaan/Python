student_heights = input("Input a list of student heights\n").split(", ")

for n in range (0,len(student_heights)):
    student_heights[n]=int(student_heights[n])

print (student_heights)

sum = 0
tot = 0

for height in student_heights:
    sum += height
    tot += 1

avg = round((sum/tot),2)

print (f"average is {avg}")

