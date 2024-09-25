white_space = 0
lowercase = 0
uppercase = 0
symbols = 0
message = input()
for i in range(len(message)):
    if message[i].islower:
        lowercase += 1
    elif message[i].isupper:
        uppercase += 1
    elif message[i] == "_":
        white_space += 1
    else:
        symbols +=1
print(float(white_space/len(message)))
print(float(lowercase/len(message)))
print(float(uppercase/len(message)))
print(float(symbols/len(message)))

