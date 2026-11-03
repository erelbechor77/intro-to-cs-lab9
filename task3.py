
from dataclasses import dataclass

@dataclass
class Course :
    name: str
    credits: int
    final_grade: int 
    passing_grade: int = 60 # Default passing grade is 60

def check_eligibility(student_courses, min_credits):
    total_credits=0
    for course in student_courses:
        if course.final_grade >= course.passing_grade:
            total_credits += course.credits
    if total_credits >= min_credits:
        return True
    else:
        return False
course1=Course( "Mathematics", 5, 75 )
course2=Course( "History", 3, 80 )
course3=Course( "Science", 4, 80 )
student_courses=[course1, course2, course3]
print(check_eligibility(student_courses, 10))
