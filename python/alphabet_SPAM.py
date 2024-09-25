string_input=input()
whitespace=0
lowercase=0
uppercase=0
symbols=0
for i in range(len(string_input)):
    if string_input[i].isupper():
        uppercase+=1
    elif string_input[i].islower():
        lowercase+=1
    elif string_input[i]=="_":
        whitespace+=1
    else:
        symbols+=1
print(float(whitespace/len(string_input)))
print(float(lowercase/len(string_input)))
print(float(uppercase/len(string_input)))
print(float(symbols/len(string_input)))
