# open source file in read mode
f1 = open("sample1.txt", "r")

# read contents from source file
data = f1.read()

f1.close()

# open destination file in write mode
f2 = open("duplicate.txt", "w")

# write contents into destination file
f2.write(data)

f2.close()

print("File contents duplicated successfully")
