# Create the translator dictionary
translator = {
    "a": "@",
    "b": "8",
    "c": "(",
    "d": "|)",
    "n": "[]\\[]",
    "o": "0",
    "p": "|D",
    "q": "(,)",
    "e": "3",
    "r": "|Z",
    "f": "#",
    "s": "$",
    "g": "6",
    "t": "']['",
    "h": "[-]",
    "u": "|_|",
    "i": "|",
    "v": "\\/",
    "j": "_|",
    "w": "\\/\\/",
    "k": "|<",
    "x": "}{",
    "l": "1",
    "y": "`/",
    "m": "[]\\/[]",
    "z": "2"
}

sentence = input()

translation = ""

for letter in sentence:
    translation += translator.get(letter.lower(), letter)

print(translation)
