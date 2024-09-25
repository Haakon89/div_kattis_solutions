def diagonal_sums(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    results = []

    # Traverse the diagonals starting from the bottom row and moving to the rightmost column
    for start in range(rows + columns - 1):
        # Determine the starting row and column for the diagonal
        row = min(rows - 1, start)
        col = max(0, start - (rows - 1))

        diag_sum = 0
        carry = 0  # Reset carry for each diagonal
        while row >= 0 and col < columns:
            diag_sum += matrix[row][col]
            row -= 1
            col += 1

        # Add carry from the previous step within the same diagonal and calculate new carry
        diag_sum += carry
        carry, last_digit = divmod(diag_sum, 10)
        print(f"{start}: digit = {last_digit}, carry = {carry}")

        # Save the last digit of the sum
        results.append(last_digit)

    return results

user_input = input()

number1, number2 = user_input.split()

image_width = 7+4*(len(number1)-1)
image_height = 7+4*(len(number2)-1)
digits_list1 = [int(digit) for digit in number1]
digits_list2 = [int(digit) for digit in number2]

list_of_multiplied_numbers = []

for i in range(len(number1)):
    for j in range(len(number2)):
        list_of_multiplied_numbers.append(digits_list1[i]*digits_list2[j])
print(list_of_multiplied_numbers)
digit_matrix = []
inner_list_first_digit = []
inner_list_second_digit = []

for i in range(len(list_of_multiplied_numbers)):
    # When the current index is a multiple of len(number1), reset the inner lists
    if i % len(number1) == 0 and i != 0:
        digit_matrix.append(inner_list_first_digit.copy())
        digit_matrix.append(inner_list_second_digit.copy())
        inner_list_first_digit = []
        inner_list_second_digit = []

    number_str = str(list_of_multiplied_numbers[i])
    first_digit = int(number_str[0]) if len(number_str) > 1 else 0
    second_digit = int(number_str[1]) if len(number_str) > 1 else int(number_str[0])

    inner_list_first_digit.append(first_digit)
    inner_list_second_digit.append(second_digit)

# Append the last group of digits if they are not empty
if inner_list_first_digit:
    digit_matrix.append(inner_list_first_digit)
if inner_list_second_digit:
    digit_matrix.append(inner_list_second_digit)

    
print(f"matrix = {digit_matrix}")
print(diagonal_sums(digit_matrix))
first_digit_insert = []
number = 2
for i in range(len(number2)):
    first_digit_insert.append(number)
    number += 4

second_digit_insert = []
number = 4
for i in range(len(number2)):
    second_digit_insert.append(number)
    number += 4
print(first_digit_insert)
print(second_digit_insert)
print(f"+" + ("-"*image_width) + "+")
counter = -1
multiplier = -3
for i in range(image_height):
    print(f"|", end='')
    if i == 0:
        for j in range(len(number1)):
            print(f"   {digits_list1[j]}", end='')
        print("   ", end='')
    elif i in first_digit_insert:
        print(" ", end='')
        for k in range(len(number1)):
            if (len(str(list_of_multiplied_numbers[k+multiplier])) > 1):
                print(f"|{str(list_of_multiplied_numbers[k+multiplier])[0]} /", end='')
            else:
                print(f"|0 /", end='')
        print("| ", end='')
    elif i in second_digit_insert:
        print(" ", end='')
        for k in range(len(number1)):
            if (len(str(list_of_multiplied_numbers[k+multiplier])) > 1):
                print(f"|/ {str(list_of_multiplied_numbers[k+multiplier])[1]}", end='')
            else:
                print(f"|/ {str(list_of_multiplied_numbers[k+multiplier])[0]}", end='')
        print("| ", end='')
    elif i % 4 == 1:
        print(" " + "+---"*len(number1) + "+ ", end='')
        counter += 1
        multiplier += len(number1)
    elif (i - 3) % 4 == 0 and i >= 3:
        print(" " + "| / "*len(number1) + f"|{digits_list2[counter]}", end='')
    elif i == image_height:
        print(f"|/ 0 / 0 ", end='')
    print("|")
    
print(f"+" + "-"*image_width + "+")