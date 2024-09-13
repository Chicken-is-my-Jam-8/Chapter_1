
# Alexander J. Jackson
# operators.py

int_one = int(input("Enter the an integer: "))
int_two = int(input("Enter another integer: "))

int_sum = int_one + int_two

int_difference = int_one - int_two

int_product = int_one * int_two

int_division = int_one / int_two

int_average = int_sum / 2

int_remainder = int_one % int_two

int_exponent = int_one ** int_two

f_sum = "Sum"

f_difference = "Difference"

f_product = "Product"

f_division = "Integer Division"

f_average = "Average"

f_remainder = "Remainder"

f_exponent = "Exponent"

print()
print(f'{f_sum:<20}', f'{int_sum:>15}')
print(f'{f_difference:<20}', f'{int_difference:>15}')
print(f'{f_product:<20}', f'{int_product:>15}')
print(f'{f_division:<20}', f'{int_division:>15,.3f}')
print(f'{f_average:<20}', f'{int_average:>15,.2f}')
print(f'{f_remainder:<20}', f'{int_remainder:>15}')
print(f'{f_exponent:<20}', f'{int_exponent:>15}')
