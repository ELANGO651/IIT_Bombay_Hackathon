def calculate_grades(marks):
    
    # Calculates the number of students in each grade and the boundary marks for each grade.
    
    # Args:
    #     marks (list): A list of student marks.
        
    # Returns:
    #     tuple: A tuple containing the number of students in each grade and the boundary marks for each grade.
    
    num_students = len(marks)
    num_students_A = num_students // 5  # Number of students in grade A (1/5 of total students)
    num_students_B = 2 * num_students_A  # Number of students in grade B (2/5 of total students)
    num_students_C = 2 * num_students_A  # Number of students in grade C (2/5 of total students)
    num_students_D = num_students - (num_students_A + num_students_B + num_students_C)  # Number of students in grade D
    
    # Sort the marks in descending order
    sorted_marks = sorted(marks, reverse=True)
    
    boundary_mark_A = sorted_marks[num_students_A - 1]  # Boundary mark for grade A
    boundary_mark_B = sorted_marks[num_students_A + num_students_B - 1]  # Boundary mark for grade B
    boundary_mark_C = sorted_marks[num_students_A + num_students_B + num_students_C - 1]  # Boundary mark for grade C
    
    return (num_students_A, num_students_B, num_students_C, num_students_D, boundary_mark_A, boundary_mark_B, boundary_mark_C)


# Read input from user
n = int(input()) # Number of students
if (5<= n <=100): #Given Constrain
    marks = list(map(int, input().split()))  # Marks of students

    # Calculate grades
    grades_info = calculate_grades(marks)

    # Print the number of students in each grade
    print(grades_info[0])
    print(grades_info[1])
    print(grades_info[2])
    print(grades_info[3])

    # Print the boundary marks for each grade
    print(grades_info[4])
    print(grades_info[5])
    print(grades_info[6])
else:
      print("Enter the value with in the constrain 5<= n <=100")