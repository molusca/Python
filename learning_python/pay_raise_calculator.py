print('\nWelcome to the salary raise calculator!')

current_salary = float(input('\nHow much is your current salary worth?: $'))
increase = float(input('How much will your salary increase?(%): '))

def calculate_raise_percentage(increase):
    return increase / 100

def calculate_final_salary(current_salary, raise_percentage):
    return current_salary + (current_salary * raise_percentage)

raise_percentage = calculate_raise_percentage(increase)
final_salary = calculate_final_salary(current_salary, raise_percentage)

print('\nWith a {}% increase, your salary goes from ${} to ${:.2f}.\n'.format(increase, current_salary, final_salary))
