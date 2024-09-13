
# Alexander J. Jackson
# f_to_c.py

fahrenheit_input = int(input("Enter a temperature in degrees fahrenheit: "))

f_to_c_1 = fahrenheit_input - 32
five_divided_by_nine = 5 / 9
f_to_c_2 = f_to_c_1 * five_divided_by_nine
Celsius = "Celsius"

print()
print(f'{Celsius:<20}', f'{f_to_c_2:>15,.3f}')
