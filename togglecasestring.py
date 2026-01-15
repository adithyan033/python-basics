def toggle_case(s):
    result = ""

    for ch in s:
        if ch.isupper():
            result = result + ch.lower()
        elif ch.islower():
            result = result + ch.upper()
        else:
            result = result + ch

    return result


# main program
string = input("Enter a string: ")

output = toggle_case(string)

print("String after toggling cases:")
print(output)
