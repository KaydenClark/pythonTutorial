# learning input

birth_year = int(input('Year you were born: '))
age = 2019 - birth_year
print(age)

weight_lbs = int(input('Weight in pounds: '))
weight_kg = weight_lbs * 0.45359237
print('Weight in Kilograms: ' + str(weight_kg) + 'kg')

# learning str

string = "Hello, I am a string"
string_copy = string[:] #WTF IS THIS
string = "Help, I've been replaced"
print(string[:], string_copy)

#learning a complex string and using varibles

first = "Kayden"
last = "Clark"
msg = f'{first} {last} is Cool'
print(msg)

