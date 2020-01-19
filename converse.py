birth_year = int(input('Year you were born: '))
age = 2019 - birth_year
print(age)

weight_lbs = int(input('Weight in pounds: '))
weight_kg = weight_lbs * 0.45359237
print('Weight in Kilograms: ' + str(weight_kg) + 'kg')

string = "Hello, I am a string"
string_copy = string[:]
string = "Help, I've been replaced"
print(string[:], string_copy)

first = "Kayden"
last = "Clark"
msg = f'{first} [{last}] is kool'
print(msg)

