'''
Develop a program that reads the name, age and sex of 5 person. At the end of the program, show:

- The average age of the group
- Name of the older man
- How many women are under 20
'''

print('\nperson RESEARCH')

sum_of_ages = 0
older = 0
younger = 0
women_ages = 0

def ask_name():
    name = str(input('Input your name: '))
    return name

def ask_gender():
    ask_gender = input('Type your gender (male/female): ').strip().lower()
    gender = ask_gender[0:3]
    return gender

def ask_age():
    age = int(input('Input your age: '))
    return age  

def calculate_age_average(sum_of_ages):
    return sum_of_ages / 5

for person in range(1, 6):
    print(f'\nPerson {person}/ 5:')

    name = ask_name()
    gender = ask_gender()
    age = ask_age()

    sum_of_ages += age 

    if gender == 'mal':
        if person == 1:
            younger = age
            older = age
            mans_name = name 
        elif person > 1:
            if age > older:
                older = age
                mans_name = name
            elif age < younger:
                younger = age
    elif gender == 'fem':
        if age < 20:
            women_ages += 1

age_average = calculate_age_average(sum_of_ages)

print('\n- The average age of the group is {:.1f} years old!'.format(age_average))
print(f'\n- {mans_name} is the older man! He has {older} years old.')
print(f'\n- {women_ages} of the women has less than 20 years old!\n')   