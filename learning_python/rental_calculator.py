'''
This car rental company charges a fixed amount of $60.00/day + $0.15/km traveled
Make a program that calculate the rent price 
'''

def calculate_daily_value(rent_days):
      return rent_days * 60

def calculate_km_value(km_traveled):
      return km_traveled * .15

print('\nWELCOME TO VEHICLE RENT CALCULATOR!')

rent_days = int(input('How many days did you rent the vehicle?: '))
km_traveled = float(input('How many KM did you traveled with the vehicle?: '))

daily_value = calculate_daily_value(rent_days)
km_value = calculate_km_value(km_traveled)
total_value = daily_value + km_value

print('\nThe value of {} days is ${:.2f}, the mileage traveled ({}km) adds ${:.2f} to the final price. \n\nTOTAL CHARGE: ${:.2f} !\n'.format(rent_days, daily_value, km_traveled, km_value, total_value))
