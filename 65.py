userInteger = int(input('Enter number up to 100:\t'))
if userInteger > 100:
    print('a shouldn`t be bigger 100!')
else:
    userIntegerToSrting = str(userInteger)
    firstIndex = (userIntegerToSrting[0])
    secondIndex = (userIntegerToSrting[1])
    firstIndexToInteger = int(firstIndex)
    secondIndexToInteger = int(secondIndex)
    if userInteger**2 == (firstIndexToInteger + secondIndexToInteger)**3:
        print('Equal')
    else:
        print('Unequal')
