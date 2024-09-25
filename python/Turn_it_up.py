input_integers = input()
input_board = input()

splitted_integers = input_integers.split()

board_size, pos_index, magic_number = map(int, splitted_integers)

board = [int(num) for num in input_board.split()]

# Check if the initial position is already out of bounds
if pos_index < 0:
    print("left")
    print(0)
    exit()
elif pos_index >= board_size:
    print("right")
    print(0)
    exit()

hops = 0
pos_list = set()

while True:
    if pos_index in pos_list:
        print("cycle")
        print(hops)
        break
    else:
        pos_list.add(pos_index)

    if board[pos_index] == magic_number:
        print("magic")
        print(hops)
        break

    next_pos = pos_index + board[pos_index]
    hops += 1

    if next_pos < 0:
        print("left")
        print(hops)
        break
    elif next_pos >= board_size:
        print("right")
        print(hops)
        break
    else:
        pos_index = next_pos
