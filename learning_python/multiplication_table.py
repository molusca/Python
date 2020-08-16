print('\n ===== MULTIPLICATION TABLE =====')
number = int(input('Table\'s number: '))
print('='*25)


def calculate_multiplications(number):
    for multiplicand in range(11):
        results = number * multiplicand
        print(f'{number} x {multiplicand} = {results}')

calculate_multiplications(number)

print('='*25)
