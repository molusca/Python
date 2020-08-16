number = int(input('\n Type a number between 0 and 9999: '))
ones = number // 1 % 10
tenths = number // 10 % 10
hundredths = number // 100 % 10
thousandths = number // 1000 % 10

print(f'\nAnalysing number {number}')
print(f' Thousandths: {thousandths}')
print(f' Hundredths: {hundredths}')
print(f' Tenths: {tenths}')
print(f' Ones: {ones}\n')

