def meters_to_centimeters(meters):
    return meters * 100

def meters_to_milimeters(meters):
    return meters * 1000


meters = float(input('\nInput value in METERS: '))

centimeters = meters_to_centimeters(meters)
milimeters = meters_to_milimeters(meters)

print(f'\n{meters}m correspond to: \n {centimeters}cm \n {milimeters}m\n')
