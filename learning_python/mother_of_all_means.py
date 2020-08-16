def calculate_geometric_average(input_values):
    multiplications = 1
    for item in input_values:
        multiplications *= item
    results = (multiplications) ** (1 / len(input_values))
    return results

def calculate_weighted_average(input_values):
    weight_products = []
    sum_of_products = 0
    sum_of_weights = 0

    for item in input_values:
        item_weight = float(input(f'Input the value\'s "{item}" wheight : '))
        weight_products.append(item * item_weight)
        sum_of_weights += item_weight

    for product in weight_products:
        sum_of_products += product

    results = ((sum_of_products) / (sum_of_weights))
    return results

def calculate_harmonic_average(input_values):
    harmonic_sum = 0
    for item in input_values:
        harmonic_sum += (1 / item)

    results = len(input_values) / (harmonic_sum)
    return results

def calculate_arithmetic_mean(input_values):
    sum_of_values = 0
    for item in input_values:
        sum_of_values += item
    results = (sum_of_values) / len(input_values)
    return results


print('\nAVERAGE CALCULATOR\n')

print('Availabe averages: \nA - Geometric Average \nB - Weighted Average \nC - Harmonic Average \nD - Arithmetic Mean\n')

type_of_average = str(input('Select average type: (A, B, C or D): ')).strip().lower()
value_quantity = int(input('Number of values: '))
print("")


input_values = []

for number in range(1, value_quantity + 1):
    value = float(input(f'Insert value {number}: '))
    if value < 0:
        print('\nERROR!!! VALUES CAN\'T BE LOWER THAN ZERO!\n')
        quit()
    else:
        input_values.append(value)

if type_of_average == 'a' or type_of_average == 'geometric':
    geometric_results = calculate_geometric_average(input_values)
    print('\nThe geometric average of the input values is equal to {:.2f} !\n'.format(geometric_results))

elif type_of_average == 'b' or type_of_average == 'weighted':
    weighted_results = calculate_weighted_average(input_values)
    print('\nThe weighted average of the input values is equal to {:.2f} !\n'.format(weighted_results))

elif type_of_average == 'c' or type_of_average == 'harmonic':
    harmonic_average = calculate_harmonic_average(input_values)
    print('\nThe harmonic average of the input values is equal to {:.2f} !\n'.format(harmonic_average))

elif type_of_average == 'd' or type_of_average == 'arithmetic':
    arithmetic_mean = calculate_arithmetic_mean(input_values)
    print('\nThe arithmetic mean of the input values is equal to {:.2f} !\n'.format(arithmetic_mean))
