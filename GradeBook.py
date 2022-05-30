def get_grade(s1, s2, s3):
    score = (s1 + s2 + s3)/3
    grade = ""
    if 90 <= score and score <= 100:
        grade = "A"
    elif 80 <= score and score <= 90:
        grade = "B"
    elif 70 <= score and score <= 80:
        grade = "C"
    elif 60 <= score and score <= 70:
        grade = "D"
    elif 0 <= score and score <= 60:
        grade = "F"
    return grade
print (get_grade(95, 90, 93))