import math

area = int(input())

length_of_side = math.sqrt(area)

perimeter = length_of_side * 4

if perimeter.is_integer():
    print(int(perimeter))
else:
    print(perimeter)
