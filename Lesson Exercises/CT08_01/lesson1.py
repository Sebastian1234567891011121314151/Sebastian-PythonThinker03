# red = 1
# blue= 2
# green= 3
# total= red*3+blue*5+green*4

# print("The total cost is, $"+str(total))


# score_one = 80 
# score_two = 90 
# score_three = 75

# total = score_one + score_two +score_three

# average_score = total / 3

# student_name = "Alex"

# print("Average score for " + student_name + " is: " + str(average_score))



score = int(input("Enter your score."))
grade=""
if (score >= 75):
    grade="A"
elif (score>=60):
    grade="B"
elif (score>=50):
    grade="C"
else:
    grade="F"

print(grade)




