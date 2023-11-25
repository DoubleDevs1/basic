def CtoF(x):
    return (x * 9 / 5) + 32

def CtoK(x):
    return x + 273.15

def FtoC(x):
    return (x - 32) * 5 / 9

def FtoK(x):
    return (x - 32) * 5 / 9 + 273.15

def KtoC(x):
    return x - 273.15

def KtoF(x):
    return (x - 273.15) * 9 / 5 + 32
    
print('A Temperture Conversion...')
print()

print('Select the conversion:')
print('1. Celcius -> Fahrenheit')
print('2. Celcius -> Kelvin')
print('3. Fahrenheit -> Celcius')
print('4. Fahrenheit -> Kelvin')
print('5. Kelvin -> Celcius')
print('6. Kelvin -> Fahrenheit')

tmpt = input('enter the conversion: ')

num1 = float(input('enter the the number: '))
num2 = float(input('enter the 2st number: '))

if tmpt == '1':
    result = CtoF(num1)
elif tmpt == '2':
    result = CtoK(num1)
elif tmpt == '3':
    result = FtoC(num1)
elif tmpt == '4':
    result = FtoK(num1)
elif tmpt == '5':
    result = KtoC(num1)
elif tmpt == '6':
    result = KtoF(num1)
else:
    print('Wrong Input!')

print('Result:', result)
