'''
Calculate the roots of a quadratic equation
Variable "a" must be different from zero. If not, print the message "Not a quadratic equation"

If delta < 0, there's no real root. Print the message "Root doesn't exists"
If delta = 0, theres ONE real root. Print the root and the message "Only one root"
If delta >= 0, print the two real roots
'''

print('\nQUADRATIC EQUATION CALCULATOR\n')

#ax² +/- bx +/- c = 0

def calculate_delta(equation_a, equation_b, equation_c):
    results = (((-1* equation_b) ** 2) - 4 * equation_a * equation_c)
    return results

def calculate_delta_root(delta):
    root = delta ** (1/2)
    return root

def calculate_equation_roots(raiz_delta, equation_a, equation_b):
    root1 = ((-1 * equation_b) + raiz_delta) / (2 * equation_a)
    root2 = ((-1 * equation_b) - raiz_delta) / (2 * equation_a)
    return root1, root2

equation_a = int(input(' Input "a" value: '))
equation_b = int(input(' Input "b" value: '))
equation_c = int(input(' Input "c" value: '))

delta = calculate_delta(equation_a, equation_b, equation_c)

print('\nSo, the equation looks like this: ({}x²)+({}x)+({})=0\n'.format(equation_a, equation_b, equation_c))

if equation_a == 0:
    print('This is not a quadratic equation!\n')

elif delta < 0:
    print('Delta doesn\'t returns a real number, so there are no roots for this equation!\n')

elif delta == 0:
    print('Delta is equal to 0. Then, there\'s only one root for this equation!\n')
    raiz_delta = calculate_delta_root(delta)
    root1, root2 = calculate_equation_roots(raiz_delta, equation_a, equation_b)

    print('Delta root is equal to {:.2f}'.format(raiz_delta))  
    print('Equation only root is equal to {:.2f}'.format(root1))

elif delta > 0:
    raiz_delta = calculate_delta_root(delta)
    root1, root2 = calculate_equation_roots(raiz_delta, equation_a, equation_b)

    print('Delta root is equal to {:.2f}'.format(raiz_delta))  
    print('Equation first root (x\') is equal to {:.2f}'.format(root1))
    print('Equation second root (x\") is equal to {:.2f}\n'.format(root2))
