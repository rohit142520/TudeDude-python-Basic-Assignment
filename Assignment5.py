# creat a dictionary with student name  and their marks
student_marks ={"Rohan": 85,
                "Rahul": 95,
                "Sumit": 88,
                "Ashish": 67,
                "Preet": 56
}
search_name = input("Enter the student's name: ")
Result = student_marks.get(search_name,"Student name not found in the record.")
if isinstance(Result,int):
    print(f"{search_name}'s marks: {Result}")
else:
    print(Result)