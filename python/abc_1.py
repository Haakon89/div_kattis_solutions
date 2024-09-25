numbers=input()
order=input()

numbers=numbers.split(" ")

if int(numbers[0])<int(numbers[1]) and int(numbers[0])<int(numbers[1]):
    A=numbers[0]
elif int(numbers[1])<int(numbers[0]) and int(numbers[1])<int(numbers[2]):
    A=numbers[1]
else:
    A=numbers[2]

if int(numbers[0])>int(numbers[1]) and int(numbers[0])>int(numbers[2]):
    C=numbers[0]
elif int(numbers[1])>int(numbers[0]) and int(numbers[1])>int(numbers[2]):
    C=numbers[1]
else:
    C=numbers[2]

if numbers[0] not in A and numbers[0] not in C:
    B=numbers[0]
elif numbers[1] not in A and numbers[1] not in C:
    B=numbers[1]
else:
    B=numbers[2]

output=""

if order[0] == "A":
    output+=f"{A} "
elif order[0] == "B":
    output+=f"{B} "
else:
    output+=f"{C} "

if order[1] == "A":
    output+=f"{A} "
elif order[1] == "B":
    output+=f"{B} "
else:
    output+=f"{C} "

if order[2] == "A":
    output+=A
elif order[2] == "B":
    output+=B
else:
    output+=C

print(output)

