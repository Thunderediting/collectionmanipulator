print("welcome to the student data organizer!")
subjects_offered = ["Maths", "Science", "English", "Computer Science"]
students={}
while True:
  print("\nSelect an option\n")
  print("1. Add students")
  print("2. Display all students")
  print("3. update student information")
  print("4. delete student")
  print("5. display subjects offered")
  print("6. exit\n")
  w=input("enter your choice: ")
  if w=="1":
    print("\nEnter the student details here \n")
    student_id=int(input("enter the student id: "))
    student={
      "id": student_id,
      "name": input("Name: "),
       "age": int(input("age: ")),
      "grade": input("Grade: "),
      "subjects" : input("Subjects (comma - seperated):"),
      "dob" : input("Date of birth(YYYY-DD-MM): "),
    }
    students[student_id] = student
    print("student added succesfully\n")
  elif w=="2":
    print("students name are given below\n")
    print(student["name"])
  elif w=="3":
    print("Upadate your student information here")
    student_id=int(input("enter the student id: "))
    if student_id in students:
      student=students[student_id]
      print("\n what you would like to update?")
      print("1. name")
      print("2. age")
      print("3. grade")
      print("4. subjects")
      print("5. dob")
      choice=input("Enter your choice: ")
      if choice=="1":
         student["name"]=(input("Enter the new name: "))
      elif choice=="3":
          student["grade"]=input("Enter the  new grade: ")
      elif choice=="2":
        student["age"]=int(input("Enter the age: "))
      elif choice=="4":
        student["subjects"]=input("Enter the new subjects: ").split(",")
      elif choice=="5":
        student["dob"]=input("Enter your new date of birth(YYYY-MM-DD: )")
      else:
        print("invalid choice")
        continue
    else:
      print("student id not found")
  elif w=="4":
    student_id=int(input("Enter the student id: "))
    if student_id in students:
      del students[student_id]
      print("Student id is deleted sucessfully")
    else:
      print("student id does nor found")
  elif w=="5":
    print("all of the subjects displayed here: ")
    for subjects in subjects_offered:
      print(subjects)
  elif w=="6":
    print("THANNK YOU FOR THE STUDENTS DETAIL")
    break
  else:
    print("Invalid choice")
    



