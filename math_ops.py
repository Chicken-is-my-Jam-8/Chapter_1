
# Alexander J. Jackson
# math_ops.py

int_one = int(input("Enter the an integer: "))
int_two = int(input("Enter another integer: "))

int_sum = int_one + int_two

int_difference = int_one - int_two

int_product = int_one * int_two

int_average = int_sum / 2

int_distance = int_difference

int_maximum = max(int_one, int_two)

int_minimum = min(int_one, int_two)

f_sum = "Sum"

f_difference = "Difference"

f_product = "Product"

f_average = "Average"

f_distance = "Distance"

f_maximum = "Maximum"

f_minimum = "Minimum"

print()
print(f'{f_sum:<20}', f'{int_sum:>15}')
print(f'{f_difference:<20}', f'{int_difference:>15}')
print(f'{f_product:<20}', f'{int_product:>15}')
print(f'{f_average:<20}', f'{int_average:>15,.2f}')
print(f'{f_distance:<20}', f'{int_distance:>15}')
print(f'{f_maximum:<20}', f'{int_maximum:>15}')
print(f'{f_minimum:<20}', f'{int_minimum:>15}')
