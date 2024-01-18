class Employee:
    """Common base class for all employees"""
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tasks = {}
        Employee.empCount += 1

    def display_emp_count(self):
        "Displays the number of employees"
        print(f"Total number of employee(s) is {Employee.emp_count}")

    def display_employee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

    def __del__ (self):
        Employee.empCount -=1


    def update_salary(self, new_salary):
        self.salary = new_salary

##    def add_task(self, task_name):
##        self.tasks[task_name] = "New"   # needs tasks defined before (in __init__)
##
##    def update_tasks(self, task_name, status):
##        self.tasks[task_name] = status
    def modify_task(self, task_name, status="New"):
        self.tasks[task_name]=status

    def display_task(self, status):
        print(f"Taskuri cu statusul {status}")
        for name in self.tasks.keys():
            if self.tasks[name] == status:
                print(name)

## x = 6 
## y = 15 

class Manager(Employee):

    mgr_count = 0

    def __init__(self,name, salary, departament):
        super().__init__(name, salary)
        self.departament = f"B02_{departament}"
        Manager.mgr_count += 1
##6%3=0
    def display_employee(self):
        print("Nume: ", self.name)  

    def marire_salariu_minim(self):
        if self.salary < 3000:
            self.salary = 3000


y = 15 

managers = []

Manager1 = Manager("Stefan", 3000, "dep1")
managers.append(Manager1)
Manager2 = Manager("Ionel", 2500, "dep2")
managers.append(Manager2)
Manager3 = Manager("Marin", 4900, "dep3")
managers.append(Manager3)
Manager4 = Manager("Pavel", 6000, "dep4")
managers.append(Manager4)
Manager5 = Manager("Alex", 6689, "dep5")
managers.append(Manager5)

for i in managers:
    i.display_employee()

print(f"Nr. de angajati: {managers[1].empCount}")
print(f"Nr. de manageri: {managers[3].mgr_count}")


for i in managers:
    i.marire_salariu_minim()

for i in managers:
    i.display_employee()



    

    
