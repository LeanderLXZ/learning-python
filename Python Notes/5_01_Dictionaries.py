ages = {"Dave": 24, "Mary": 42, "John": 58}
print(ages["Dave"])
print(ages["Mary"])
print('\n')

primary = {
    "red": [255, 0, 0],
    "green": [0, 255, 0],
    "blue": [0, 0, 255],
}
print(primary["red"])
# print(primary["yellow"])

# bad_dict = {
#     [1, 2, 3]:"one two three", ----- [1, 2, 3] is mutable
# }
print('\n')

squares = {1: 1, 2: 4, 3: "error", 4: 16}
squares[8] = 64
squares[3] = 9
print(squares)
print(1 in squares)
print("error" in squares)
print(4 not in squares)
print('\n')

pairs = {
    1: "apple",
    "orange": [2, 3, 4],
    True: False,
    None: "True",
    2: 6,
}
print(pairs.get("orange"))
print(pairs.get(7))
print(pairs.get(None))
print(pairs.get(123, "not in dictionary"))
print(pairs.get(2, 5) + pairs.get(5, 3))
