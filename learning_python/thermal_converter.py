def convert_celsius_to_farenheit(celsius):
    return (1.8 * celsius) + 32

def convert_celsius_to_kelvin(celsius):
    return celsius + 273

print('\nTHERMAL CONVERSOR FROM ºC TO FARENHEIT AND KELVIN!')

celsius = float(input('\nInput ºC value: '))

farenheit = convert_celsius_to_farenheit(celsius)
kelvin = convert_celsius_to_kelvin(celsius)

print('\nSo, {:.1f} ºC (Celsius) equals to: \n {:.1f} ºF (Farenheit); \n {:.1f} K (Kelvin).\n'.format(celsius, farenheit, kelvin))