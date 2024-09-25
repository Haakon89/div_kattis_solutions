import sys

digit_representation = {
    '0': ["xxxxx", "x...x", "x...x", "x...x", "x...x", "x...x", "xxxxx"],
    '1': ["....x", "....x", "....x", "....x", "....x", "....x", "....x"],
    '2': ["xxxxx", "....x", "....x", "xxxxx", "x....", "x....", "xxxxx"],
    '3': ["xxxxx", "....x", "....x", "xxxxx", "....x", "....x", "xxxxx"],
    '4': ["x...x", "x...x", "x...x", "xxxxx", "....x", "....x", "....x"],
    '5': ["xxxxx", "x....", "x....", "xxxxx", "....x", "....x", "xxxxx"],
    '6': ["xxxxx", "x....", "x....", "xxxxx", "x...x", "x...x", "xxxxx"],
    '7': ["xxxxx", "....x", "....x", "....x", "....x", "....x", "....x"],
    '8': ["xxxxx", "x...x", "x...x", "xxxxx", "x...x", "x...x", "xxxxx"],
    '9': ["xxxxx", "x...x", "x...x", "xxxxx", "....x", "....x", "xxxxx"],
    '+': [".....", "..x..", "..x..", "xxxxx", "..x..", "..x..", "....."],
    '-': [".....", ".....", ".....", "xxxxx", ".....", ".....", "....."]
}

def parse_input(input_lines):
    chars = []
    width = len(input_lines[0])
    
    for i in range(0, width, 6):  # Assuming 5 width + 1 space between characters
        char_representation = [line[i:i+5] for line in input_lines]
        for char, rep in digit_representation.items():
            if rep == char_representation:
                chars.append(char)
                break
    
    return ''.join(chars)

def evaluate_expression(expression):
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return str(e)

def convert_to_style(result):
    lines = [""] * 7  # Each digit representation has 7 lines
    for char in result:
        char_rep = digit_representation[char]
        for i in range(7):
            lines[i] += char_rep[i] + "."
    
    return lines

def main(input_lines):
    expression = parse_input(input_lines)
    result = evaluate_expression(expression)
    result_in_style = convert_to_style(result)
    return result_in_style

# Example input
input = sys.stdin.read
input_lines = input()

result = main(input_lines)
for line in result:
    print(line)
