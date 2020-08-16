''' Input an integer number and tell if it's a prime number, printing its dividers. '''

def count_dividers_quantity(input_number):
    dividers_quantity = 0
    for n in range(1, input_number + 1):
        print(n, end= '; ')
        if input_number % n == 0:
            dividers_quantity += 1
    return dividers_quantity

def verify_if_is_prime(input_number, total_of_dividers):
    if total_of_dividers > 2:
        print(f'\n\n{input_number} is divisible by {total_of_dividers} numbers, so IT IS NOT a prime number!')
    else:
        print(f'\n\n{input_number} is divisible by {total_of_dividers} numbers, so IT IS a prime number!')

def print_dividers(input_number):
    print(f'{input_number} is divisible by: ', end= '' )
    for n in range(1, input_number +1):
        if input_number % n == 0:
            print(f'{n}', end= '; ')

print('\nPRIME NUMBER VERIFIER\n')

input_number = int(input('Input a number: '))

total_of_dividers = count_dividers_quantity(input_number)
verify_if_is_prime(input_number, total_of_dividers)
print_dividers(input_number)
print('\n')
