class Person:
    def __init__(self, name, age):
        self.__name = name  
        self.__age = age    
    def get_name(self): return self.__name
    def set_name(self, name): self.__name = name
    def get_age(self): return self.__age
    def set_age(self, age): self.__age = age
    def show_info(self):
        print(f"Name: {self.__name}, Age: {self.__age}")
class Employee(Person):
    def __init__(self, name, age, emp_id, salary):
        super().__init__(name, age)  
        self.__emp_id = emp_id
        self.__salary = salary
    def get_emp_id(self): return self.__emp_id
    def get_salary(self): return self.__salary
    def show_info(self):
        super().show_info()
        print(f"Employee ID: {self.__emp_id}, Salary: ${self.__salary}")
    def compute_bonus(self, amount=500):
        return self.__salary + amount
class Manager(Employee):
    def __init__(self, name, age, emp_id, salary, department):
        super().__init__(name, age, emp_id, salary)
        self.__department = department
    def get_department(self): return self.__department
    def show_info(self):
        super().show_info()
        print(f"Department: {self.__department}")
class Developer(Employee):
    def __init__(self, name, age, emp_id, salary, language):
        super().__init__(name, age, emp_id, salary)
        self.__language = language
    def get_language(self): return self.__language
    def show_info(self):
        super().show_info()
        print(f"Programming Language: {self.__language}")
def main():
    persons = []
    employees = []
    managers = []
    developers = []
    while True:
        print("\nChoose an operation:")
        print("1. Create a Person")
        print("2. Create an Employee")
        print("3. Create a Manager")
        print("4. Create a Developer")
        print("5. Show Details (and test issubclass)")
        print("6. Exit")
        choice = input("\nEnter your choice: ")
        if choice == '1':
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            persons.append(Person(name, age))
            print(f"Person created: {name}, {age}")
        elif choice == '2':
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            emp_id = input("Enter Employee ID: ")
            salary = float(input("Enter Salary: "))
            employees.append(Employee(name, age, emp_id, salary))
            print(f"Employee created: {name}, Salary: ${salary}")
        elif choice == '3':
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            emp_id = input("Enter Employee ID: ")
            salary = float(input("Enter Salary: "))
            dept = input("Enter Department: ")
            managers.append(Manager(name, age, emp_id, salary, dept))
            print(f"Manager created in {dept}")
        elif choice == '4':
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            emp_id = input("Enter Employee ID: ")
            salary = float(input("Enter Salary: "))
            lang = input("Enter Programming Language: ")
            developers.append(Developer(name, age, emp_id, salary, lang))
            print(f"Developer created with {lang}")
        elif choice == '5':
            # Demonstrating issubclass() requirement easily
            print("\n--- Testing issubclass() ---")
            print("Is Manager a subclass of Employee?:", issubclass(Manager, Employee))
            print("Is Developer a subclass of Person?:", issubclass(Developer, Person))
            print("\n--- Listing All Records ---")
            for p in persons: p.show_info()
            for e in employees: e.show_info()
            for m in managers: m.show_info()
            for d in developers: d.show_info()
        elif choice == '6':
            print("\nExiting the system. All resources have been freed. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")
if __name__ == "__main__":
    main()