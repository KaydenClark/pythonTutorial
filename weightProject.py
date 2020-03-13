weight = int(input('What is your weight?: '))

valid_entry = False

while valid_entry == False:
    weight_type = input('(L)bs or (K)g?: ').upper()
    if weight_type == 'L':
        weight *= .45
        print(f'You weigh {weight}kgs')
        break
    elif weight_type == 'K':
        weight /= .45
        print(f'You weigh {weight}lbs')
        break
    else:
        print('You must enter either "L" or "k" for weight type: ')
