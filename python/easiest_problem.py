input = input()
sum_of_N = 0
for i in range(len(input)):
    sum_of_N += int(input[i])
p = 1
sum_test = 0
while (sum_of_N != sum_test):
    sum_test = 0
    test = 0
    p += 1
    test = int(input)*p
    length = len(str(test))
    for i in range(length):
        sum_test += int(str(test)[i])
print(p)