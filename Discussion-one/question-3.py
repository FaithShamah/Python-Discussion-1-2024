#Question 3
# Using loop of your choice, WITI  has tasked you to automate a simple grading system. 
# As a python student, write a program using functions and conditions to display the grades that 
# the students will be receiving. 
# The grades are:
# 90% - 100%  Grade is A
# 80% - 89% Grade is   B
# 70% - 79% Grade is   C                                                        
# 60% - 69%  Grade is  D                  
# 50% - 59%  Grade is  E  
# < 50%                Fail 
         #soln
def get_grade(score):
    """Function to determine the grade based on score."""
    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif 60 <= score < 70:
        return 'D'
    elif 50 <= score < 60:
        return 'E'
    else:
        return 'Fail'

def display_grades(scores):
    """Function to display grades for a list of scores."""
    for score in scores:
        grade = get_grade(score)
        print(f'Score: {score} - Grade: {grade}')

def main():
    """Main function to run the grading system."""
    # List of student scores
    student_scores = [95, 82, 76, 65, 54, 45, 88, 92, 71, 40]
    
    print("Student Grades:")
    display_grades(student_scores)

if __name__ == "__main__":
    main()
