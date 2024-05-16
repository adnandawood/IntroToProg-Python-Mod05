import json

# Defining data constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Defining data constants
FILE_NAME: str = "Enrollments.json"

# Defining data variables and constants
student_first_name: str = ""
student_last_name: str = ""
course_name: str = ""
student_data: dict = {}
students: list = []
json_data: str = ""
file = None
menu_choice: str 

try:
    file = open(FILE_NAME, "r")
    students = json.load(file)
    file.close()
except Exception as e:
    print("Error: There was a problem with reading the file.")
    print("Please check that the file exists and that it is in JSON format.")
    print("-- Technical error message --")
    print(e)

while True:
    print(MENU)
    menu_choice = input("What would you like to do: ")
    if menu_choice == "1":
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should only contain alphabets.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should only contain alphabets.")
            course_name = input("Please enter the name of the course: ")
            student_data = {
                "FirstName": student_first_name,
                "LastName": student_last_name,
                "CourseName": course_name
            }
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            print(e)
            print("-- Technical Error Message --")
            print(e.__doc__)
            print(e)
        except Exception as e:
            print("Error: There was a problem with your entered data.")
            print("-- Technical Error Message --")
            print(e.__doc__)
            print(e)
        continue

    elif menu_choice == "2":
        print("-" * 50)
        for student in students:
            print(f'Student {student["FirstName"]} {student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)
        continue

    elif menu_choice == "3":
        try:
            with open(FILE_NAME, "w") as file:
                json.dump(students, file)
            print("The following data was saved to file:")
            for student in students:
                print(f'Student {student["LastName"]} is enrolled in {student["CourseName"]}')
        except Exception as e:
            print("Error: There was a problem with writing to the file.")
            print("Please check that the file is not open by another program.")
            print(e)
        continue

    elif menu_choice == "4":
        break

    else:
        print("Please only choose option 1, 2, 3, or 4")

print("Program Ended")