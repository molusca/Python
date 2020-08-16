'''
Given 3 length values ​​entered, calculate and show whether it is possible to form a triangle with them.
If possible, print the type of triangle that can be formed.
'''

print('\nEXISTENCE CONDITION OF A TRIANGLE\n')

face1 = float(input(' Enter the length of the first side: '))
face2 = float(input(' Enter the length of the second side: '))
face3 = float(input(' Enter the length of the third side: '))


if face1 < (face2 + face3) and face2 < (face1 + face3) and face3 < (face1 + face2):
    print('\nIt is possible to form a triangle with these measures!')
    if face1 == face2 == face3:
        print('An EQUILATERAL triangle will be formed!\n')
    elif face1 != face2 != face3 != face1:
        print('A SCALEN triangle will be formed!\n')
    else:
        print('A ISOSCELES triangle will be formed!\n')

else:
    print('\nIt is NOT possible to form a triangle with these measures\n')
