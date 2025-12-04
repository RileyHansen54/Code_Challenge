student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(range(1, 10))

total_score = sum(student_scores)
avg_score = total_score/len(student_scores)

print("avg is",int(avg_score))
summ=0
for x in student_scores:
    summ += x

print(summ)
print(total_score)

max = 0

for x in student_scores:
    if max < x:
        max = x

print (max)
#max2 = max(student_scores)