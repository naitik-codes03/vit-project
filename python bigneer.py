# Project Title: VIT Bhopal 1st Semester CGPA Predictor Tool
# Created by 1st Sem Student for Python Course Project
# created by: [NAITIK MISHRA]
def get_grade_and_points(my_marks, highest_marks, avg_marks):
    # Validation checks for inputs
    if my_marks > 100 or highest_marks > 100 or avg_marks > 100:
        print("Warning: Marks cannot be greater than 100. Calculating with current input.")
    
    # Highest aur Average se Class SD ka andaza lagana(prediction) , because actual SD nahi pata hai, we don't have access to all students' marks.
    estimated_sd = (highest_marks - avg_marks) / 2
    if estimated_sd <= 0:
        estimated_sd = 1.0  # Division by zero error se bachne ke liye
        
    # Relative Grade limits ka formula
    s_limit = avg_marks + (1.5 * estimated_sd)
    a_limit = avg_marks + (1.0 * estimated_sd)
    b_limit = avg_marks + (0.5 * estimated_sd)
    c_limit = avg_marks
    d_limit = avg_marks - (0.5 * estimated_sd)
    e_limit = avg_marks - (1.0 * estimated_sd)

     
    
    # Grade aur VIT Grade Point tay karne ka logic .. 
    if my_marks < 40 or my_marks < e_limit:
        return "F", 0
    elif my_marks >= s_limit:
        return "S", 10
    elif my_marks >= a_limit:
        return "A", 9
    elif my_marks >= b_limit:
        return "B", 8
    elif my_marks >= c_limit:
        return "C", 7
    elif my_marks >= d_limit:
        return "D", 6
    else:
        return "E", 5

def main():
    print("=============================================")
    print("      VIT BHOPAL 1st SEMESTER GPA CALCULATOR9(PREDICTIVE) ")
    print("=============================================\n")
    
    # Subjects aur unke specific credits ka dictionary
    subjects = {
        "Math": 4,
        "Python": 4,
        "EVS": 2,
        "English": 2
    }
    
    total_credit_points = 0
    total_credits = sum(subjects.values()) # Total 12 credits hain yahan
    
    predicted_grades = {}
    
    # Har subject ka details user (student) se lena enter marks, highest marks aur average marks
    for sub, credit in subjects.items():
        print(f"--- Enter details for {sub} ({credit} Credits) ---")
        my_marks = float(input("Your Marks: "))
        highest_marks = float(input("Class Highest Marks: "))
        avg_marks = float(input("Class Average Marks: "))
        print()
        
        # Function ko call karke grade aur points lena
        grade, points = get_grade_and_points(my_marks, highest_marks, avg_marks)
        
        # Credit * Grade Point ko total me jodna
        total_credit_points += (points * credit)
        predicted_grades[sub] = grade
        
    # Final Result / Dashboard screen par show karna
    print("=============================================")
    print("              FINAL REPORT CARD              ")
    print("=============================================")
    for sub, grade in predicted_grades.items():
        print(f"{sub:<10} | Grade: {grade}")
    print("---------------------------------------------")
    
    # GPA nikalne ka formula
    gpa = total_credit_points / total_credits
    print(f"Your Predicted Semester GPA is: {round(gpa, 2)}")
    print("=============================================")

if __name__ == "__main__":
    main()
