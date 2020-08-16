def calculate_discount_percentage(discount):
    return discount / 100

def calculate_final_value(product_value, discount_percentage):
    return product_value - (product_value * discount_percentage)

print('\nDISCOUNT CALCULATOR')

product_value = float(input('\nProduct value: $'))
discount = float(input('Discount offered?(%): '))

discount_percentage = calculate_discount_percentage(discount)
final_value = calculate_final_value(product_value, discount_percentage)

print(f'\nThe product value with {discount}% discount goes from ${product_value} to ${final_value} !\n')