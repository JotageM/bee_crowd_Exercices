salary = float(input())
if salary <= 400.00:
    increasy_salary = 1.15
    new_salary = salary * increasy_salary
    percentual = "15 %"
elif salary > 400.00 and salary <= 800.00:
    increasy_salary = 1.12
    new_salary = salary * increasy_salary
    percentual = "12 %"
elif salary > 800.00 and salary <= 1200.00:
    increasy_salary = 1.10
    percentual = "10 %"
    new_salary = salary * increasy_salary
elif salary > 1200.00 and salary <= 2000.00:
    increasy_salary =1.07
    new_salary = salary * increasy_salary
    percentual = "7 %"
elif salary > 2000.00:
    increasy_salary = 1.04
    new_salary = salary * increasy_salary
    percentual = "4 %"
print(f"Novo salario: {new_salary:.2f}")
print(f"Reajuste ganho: {(new_salary - salary):.2f}")
print(f"Em percentual: {percentual}")