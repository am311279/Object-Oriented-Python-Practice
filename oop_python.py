#Part 1 - Class Definitions
class Student:
    def __init__(self, name, email, grades):
        self.name = name
        self.email = email
        self.grades = grades
    
    #Method to add a grade to the grades list
    def add_grades(self, grade):
        self.grades.append(grade)
    
    #Method to get the average of all grades
    def average_grade(self):
        total = 0
        for grade in self.grades:
            total += grade
        return total/len(self.grades)
    
    #Method to print out the student info
    def display_info(self):
        print(f"Student Name: {self.name}.")
        print(f"Student Email: {self.email}.")
        print("Grades: ")
        for grade in self.grades:
            print(grade)

    #Method to return the grades as a tuple
    def grades_tuple(self):
	    return tuple(self.grades)

#Part 2 - Working with Objects	
print("\nPart 2")	
#create 3 student objects
student_1 = Student("David", "david@gmail.com", [91, 72, 63])
student_2 = Student("Mary", "mary@gmail.com", [54, 82, 43])
student_3 = Student("Jack", "jack@gmail.com", [74, 82, 73])

#add 2 new grades to each student
student_1.add_grades(97)
student_1.add_grades(82)

student_2.add_grades(57)
student_2.add_grades(60)

student_3.add_grades(47)
student_3.add_grades(69)

#create a list to hold 3 student objects
students = [student_1, student_2, student_3]

#loop each student object in the students list and print out the
#student info and the average grade for each student
for student in students:
    student.display_info()
    print(f"Average grade for {student.name}: {student.average_grade()}")
	
#Part 3 - Dictionary & Set Integration
#Declare a dictionary with student's email as key and student object as value
print("\nPart 3")
student_dict = {
"david@gmail.com": "student_1",
"mary@gmail.com": "student_2",
"jack@gmail.com": "student_3"
}

#function to retrieve student object(value) using email(key) 
def get_student_by_email(email):
    return student_dict.get(email)

#declare a list to insert student's grades	
grades_from_all_students = []

#loop each student 
for student in students:
#loop each grade in each student grades list and append to grades_from_all_students
    for student.grade in student.grades:
        grades_from_all_students.append(student.grade)
#Convert list to set
grades_from_all_students_set = set(grades_from_all_students)

#Print out all grades from grades_from_all_students_set
for grade in grades_from_all_students_set:
    print(grade)
	
#Part 4 - Tuple Practice
print("\nPart 4")
#Change the first value of grades_tuple using try and except 
try:
    grades_tuple = student_1.grades_tuple()
    grades_tuple[0] = 10
except TypeError as e:
    print(e)
	
#Part 5 - List Operations
print("\nPart 5")
#Loop each student in the students list and remove the last grade from each student
for student in students:
    student.grades.pop()
    print(student.grades)

#Loop each student in the students list and print out the first and last grade of each student 
#and also print out the the number of grades for each student
for student in students:
    print(f"\nFirst Grade of {student.name}: {student.grades[0]}")
    print(f"Last Grade of {student.name}: {student.grades[len(student.grades)-1]}")
    print(f"The number of grades for {student.name}: {len(student.grades)}")
	
#Part 6 - Bonus
print("\nPart 6")
#import re module from python
import re
#define the format to chack 
format = r"^[\w\.-]+@[\w\.-]+\.com$"
#Loop each student in the students list and compare each student email with the format defined
for student in students:
    if re.match(format, student.email):
	    print(f"{student.name}'s email is valid")

#Initialize the count variable for counting the grades above 90		
count = 0

#Loop each student in the students list
for student in students:
#Loop every grade in the grades list of each student 
    for student.grade in student.grades:
#Check if grade is above 90 and increment the count variable
	    if student.grade > 90:
		    count+=1
#Print out the number of grades above 90
print(f"{count} grades are above 90")
	
    



    

