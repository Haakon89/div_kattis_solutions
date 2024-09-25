#input_integers = input()
#input_board = input()
import random

counter = 0

while counter < 5:
    input_integers = (f"{random.randint(1, 400)} {random.randint(-200, 200)}")
    input_board = ""

    splitted_integers = input_integers.split()

    #board_size, pos_index, magic_number = map(int, splitted_integers)
    board_size, magic_number = map(int, splitted_integers)

    pos_index = random.randint(0, board_size-1)

    used_numbers = []
    for i in range(board_size):
        new_number = random.randint(-200, 200)
        while new_number in used_numbers:
            new_number = random.randint(-200, 200)
        input_board += (str(new_number) + " ")
        used_numbers.append(new_number)
    board = [int(num) for num in input_board.split()]

    if magic_number not in board:
        random_index = random.randint(0, board_size-1)
        board[random_index] = magic_number

    hops = 0
    print(f"player position = {pos_index}, magic number = {magic_number}")
    pos_list = []
    print(board)
    while True:
        if board[pos_index] in pos_list:
            print("cycle")
            print(hops)
            break
        else:
            pos_list.append(board[pos_index])
        
        if board[pos_index] == magic_number:
            print("magic")
            print(hops)
            break
        
        if board[pos_index] > 0 and board.index(board[pos_index])+board[pos_index] <= board_size-1:
            pos_index = board.index(board[board.index(board[pos_index])+board[pos_index]])
            hops +=1
        elif board[pos_index] < 0 and board.index(board[pos_index])+board[pos_index] >= 0:
            pos_index = board.index(board[board.index(board[pos_index])+board[pos_index]])
            hops += 1
        elif board.index(board[pos_index])+board[pos_index] > board_size-1:
            hops+=1
            print("right")
            print(hops)
            break
        elif board.index(board[pos_index])+board[pos_index] < 0:
            hops+=1
            print("left")
            print(hops)
            break
    counter+=1
