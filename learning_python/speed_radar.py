'''
A radar checks whether vehicles pass on the road within the 80km/h speed limit.
If it is above the limit, the driver must pay a fine of 7 times the difference between the speed that he was
trafficking and the speed limit.
'''

def calculate_speed_difference(vehicle_speed, speed_limit):
    return (vehicle_speed - speed_limit)

def calculate_fine_value(speed_difference, base_multiplier):
    return (speed_difference * base_multiplier)

print('\nSPEED RADAR')

vehicle_speed = int(input('\nVehicle speed (Km/h): '))

speed_limit = 80
base_multiplier = 7

speed_difference = calculate_speed_difference(vehicle_speed, speed_limit)
fine_value = calculate_fine_value(speed_difference, base_multiplier)

if vehicle_speed > speed_limit:
    print(f'\nThe vehicle was {speed_difference}Km/h above the speed limit and got fined!')
    print(f'The fine value is ${fine_value} !\n')

else:
    print('\nThe vehicle was trafficking within the speed limit!\n')
