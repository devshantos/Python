salary =int(input("Enter your salary: "))
experience = float(input("Enter your experience: "))

if experience > 5 :
    bonus = 0.05
    net_salary = salary + salary * bonus
    print("You salary is ", net_salary)
