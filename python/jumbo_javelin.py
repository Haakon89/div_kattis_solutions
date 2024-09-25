number_of_rods = int(input())

for i in range(number_of_rods):
    rod_length = int(input())
    if (i == 0):
        javelin_length = rod_length
    else:
        javelin_length += rod_length
        javelin_length -=1
print(javelin_length)