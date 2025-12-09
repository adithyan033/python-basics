s=input("enter a string")
uppercase=""
numbers=""
special=""
swapped=""

for ch in s:
    if ch.isupper():
        uppercase+=ch
    if ch.isdigit():
        numbers+=ch
    if not ch.isalnum():
        special+=ch
    if ch.isupper():
        swapped+=ch.lower()
    elif ch.islower():
        swapped+=ch.upper()
    else:
        swapped+=ch

print("uppercase letters",uppercase)
print("special letters",special)
print("digits",numbers)
print("swapped",swapped)

