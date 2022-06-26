message = "b"
output = ""
pattern = [
["a", "b","c"],
["d", "e","f"],
["g", "h","i"],
["j", "k","l"],
["m", "n","o"],
["p", "q","r", "s"],
["t","u", "v"],
["w","x","y","z"] 
]
def split(message):
    return [char for char in message]

preparedMessage = split(message)



for currentChar in preparedMessage:
    continue
for charArray in pattern: 
    for i in charArray:
        if i == "a":
            continue

print(pattern[2])

    