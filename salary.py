# How to calculate the increased salary of the worker whose salary and raise rate is entered on Python?

newsalary = 0
salary = input("enter new salary : ")
hike = input("salary raise rate(%) : ")
newsalary = int(salary)+(int(salary)*int(hike)/100)
print("increased salary : ",newsalary)