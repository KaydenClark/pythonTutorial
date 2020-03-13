house_price = 1000000

buyers_credit = True

if buyers_credit:
    downpayment = house_price * .1
    print(f'you have good credit, your downpayment is ${downpayment}')
else:
    downpayment = house_price * .2
    print(f'you have bad credit, your downpayment is ${downpayment}')


has_high_income = False
has_good_credit = True
criminal_recored = False

if has_good_credit or has_high_income and not criminal_recored: #also works with 'and'
    print('you are eligible for a loan')
else:
    print('you can not get a loan')


temperature = 60

if temperature > 60:
    print('its a hot day')
elif temperature < 60:
    print('its cold outside')
else:
    print('its a nice day')

# Validation
valid = False
while valid == False:
    name = input('Your name: ')
    if len(name) < 3:
        print('your name is not long enough, try again')
    elif len(name) > 25:
        print('your name is too long, try again')
    else:
        valid = True
        print('nice name')