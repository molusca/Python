print('Welcome to the Area Calculator!\n')

height = float(input('Object height: '))
width = float(input('Object width: '))

def calculate_area(height, width):
    return height * width

area_meters = calculate_area(height, width)

print('The area is equal to: {:.2f}m²\n'.format(area_meters))
