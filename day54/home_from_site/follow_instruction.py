def follow(instructions: str):
    l = [ 0 , 0]
    for direction in instructions:
        if direction == "f":
            l[1] += 1
            continue
        elif direction == "b":
            l[1] -= 1
            continue
        elif direction == "l":
            l[0] -= 1
            continue
        elif direction == "r":
            l[0] += 1
            continue
    return l


print("Example:")
print(list(follow("fflff")))

# These "asserts" are used for self-checking
print(list(follow("fflff"))) == [-1, 4]
print(list(follow("ffrff"))) == [1, 4]
print(list(follow("fblr"))) == [0, 0]

print("The mission is done! Click 'Check Solution' to earn rewards!")
