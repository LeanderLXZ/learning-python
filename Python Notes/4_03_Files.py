file = open("filename.txt", "r")
cont = file.read()
print(cont)
print(file.read(16))
print(file.read(4))
print(file.read())
file.close()
print('\n')

file = open("filename.txt", "r")
str = file.read()
print(len(str))
file.close()
print('\n')

file = open("filename.txt", "r")
print(file.readlines())
file.close()
print('\n')

file = open("filename.txt", "r")
for line in file:
    print(line)
file.close()
print('\n')

len(open("test.txt").readlines())


file = open("newfile.txt", "w")
file.write("This has been written to a file")
file.close()
file = open("newfile.txt", "w")
print(file.read())
file.close()
print('\n')

msg = "Hello world!"
file = open("newfile.txt", "w")
amount_written = file.write(msg)

# number of bytes written to a file
print(amount_written)
file.close()
print('\n')


try:
    f = open("filename.txt")
    print(f.read())
finally:
    f.close()
    print('\n')

with open("filename.txt") as f:
    print(f.read())
