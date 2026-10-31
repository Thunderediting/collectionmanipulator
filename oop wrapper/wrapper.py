print("--python OOP project: Employee Management System--")
class person:
    def get(self):
        self.name=input("enter the name ")
        self.age=int(input("enter the age"))

        
    def details(self):
        print("name: ", self.name)
        print("Age: ", self.age)
class employee(person):
    def get(self):
        super().get()
        self.id=input("Enter the employee id")
        self.salary=int(input("enter the employee the salary"))
    def details(self):
        super().details()
        print("ID: ",self.id)
        print("Salary: ",self.salary)
        
class num(employee):
    def get(self):
        super().get()
        self.department=input("Enter department: ")
    def details(self):
        super().details()
        print("Department: ",self.department)
p = None 
q= None
v= None
while True:
    print("choose an operation:\n")
    print("1. create a person")
    print("2. create a employee")
    print("3. create a manager")
    print("4. show details")
    print("5. exit")
    z=int(input("Enter the choice:"))
    if z == 1:
        p=person()
        p.get()
        print("person created with name",p.name,"and age",p.age)
    elif z== 2:
        q=employee()
        q.get()
        print("Employees created with name :",q.name,"age :",q.age,"ID :",q.id,"salary :",q.salary)
    elif z == 3:
        v=num()
        v.get()
        print("Manager created with name :",v.name,"age :",v.age,"ID :",v.id,"salary :",v.salary,"and deparment:",v.department)

    elif z == 4:

        print("\nChoose details to show:")
        print("1. Person")
        print("2. Employee")
        print("3. Manager")
        sub=int(input("Enter the choice: "))
        if sub == 1:
                    if p is not None:
                                     print("\nPerson Details:")
                                     p.details()
                    else:
                          print("Person record not found!")

        elif sub == 2:
                      if q is not None:
                                       print("\nEmployee Details:")
                                       q.details()
                      else:
                           print("Employee record not found!")

        elif sub == 3:
                      if v is not None:
                                       print("\nManager Details:")
                                       v.details()
                      else:
                           print("Manager record not found!")
        else:
               print("invalid choice")
    elif z == 5:
                print("\nExiting the system. All resources have been freed.")
                print("\nGoodbye!")
                break
    else:
        print("invalid choice")