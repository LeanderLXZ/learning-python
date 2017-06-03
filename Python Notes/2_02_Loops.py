# while Loops
i = 1
while i <= 5:
    print(i)
    i = i + 1
print("Finished!")
print('\n')

# break
i = 0
while 1 == 1 :
    print(i)
    i += 1
    if i >= 5:
        print("Breaking")
        break
print("Finished!")
print('\n')

# continue
i = 0
while True:
    i += 1
    if i == 2:
        print("Skipping 2")
        continue
    if i == 5:
        print("Breaking")
        break
    print(i)
print("Finished!")
print('\n')


# for Loops
words = ["hello", "world", "spam", "eggs"]
for word in words:
    print(word + "!")
print('\n')

for i in range(5):
    print("hello!")