''' Read the first term and the common difference of an Arithmetic Progression and show its n-th first terms '''

print('\nTERMS OF AN ARITHMETIC PROGRESSION\n')

first_term = int(input('Input AP first term: '))
common_difference = int(input('Input AP common difference: '))
nth_term = int(input('Input AP n-th term: '))

if first_term < nth_term:
    print("")
    for c in range(first_term, nth_term, common_difference):
        print(c, end= '; ')

else:
    print("")
    for c in range(nth_term, first_term, common_difference):
        print(c, end= '; ')
