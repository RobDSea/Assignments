# Collect User Input
name = input("What is your First and Last name? ")
print("Student Name: " + name)
course_name = input("What is your course name? ")
print("Course Name: " + course_name)
first_exam_score = float(input("What is your first exam score? "))
print("First Exam Score: " + str(first_exam_score))
second_exam_score = float(input("What is your second exam score? "))
print("Second Exam Score: " + str(second_exam_score))

# Calculate Average Score
average_score = (first_exam_score + second_exam_score) / 2
print("Average Score: " + str(average_score))

# Determine Final Letter Grade
letter_grade = ""
if average_score >= 90:
    letter_grade = 'A'
elif average_score >= 80:
    letter_grade = 'B'
elif average_score >= 70:
    letter_grade = 'C'
elif average_score >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'
print("Final Grade: " + letter_grade)

# Determine Pass or Fail
pass_status = ""
if letter_grade == 'A' or letter_grade == 'B' or letter_grade == 'C':
    pass_status = "Passed"
else:
    pass_status = "Failed"
print("Pass/Fail Status: " + pass_status)

# Personalized Feedback Message
feedback_message = ""
if letter_grade == 'A':
    feedback_message = "Excellent work, " + name + "! You have earned an ‘A’ in " + course_name + ". Keep it up!"
elif letter_grade == 'B':
    feedback_message = "Good job, " + name + "! You have earned a ‘B’ in " + course_name + ". Well done!"
elif letter_grade == 'C':
    feedback_message = "You passed, " + name + ". Your grade is ‘C’ in " + course_name + ". Keep working hard!"
elif letter_grade == 'D':
    feedback_message = "You need to put in more effort, " + name + ". Your grade is ‘D’ in " + course_name + ". Please try harder next time."
elif letter_grade == 'F':
    feedback_message = "Unfortunately, you did not pass, " + name + ". Your grade is ‘F’ in " + course_name + ". Please seek help to improve your performance."

print(feedback_message)
