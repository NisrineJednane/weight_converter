# a simple weight converter

user_weight = float(input('enter weight '))
weight_unit = input('weight in L or K? ')

if weight_unit.upper() == 'K':
    print(f'your weight is {round(user_weight*2.205, 2)} pounds')
elif weight_unit.upper() == 'L':
    print(f'your weight is {round(user_weight/2.205, 2)} kilograms')
else:
    print("error")
