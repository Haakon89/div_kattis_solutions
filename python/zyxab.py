def letter_value(letter):
    letter = letter.lower()
    return ord(letter) - ord('a') + 1

def word_value(word):
    total_value = 0
    for letter in word:
        if letter.isalpha():
            total_value += letter_value(letter)
    return total_value

def choose_best_name(rounds):
    best_name = ""
    for i in range(int(rounds)):
        new_name = input()
        if len(new_name) >= 5:
            for char in new_name:
                if new_name.count(char) > 1:
                    break
            print(word_value(new_name))
            if word_value(new_name) > word_value(best_name):
                best_name = new_name
    if len(best_name) == 0:
        return "Neibb3"
    return best_name

rounds = input()

print(choose_best_name(rounds))
