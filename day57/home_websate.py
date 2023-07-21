def count_gold(pyramid: list[list[int]]) -> int:
    l = []
    for list in pyramid:
        l.append(max(list))
    
    return sum(l)


print("Example:")
print(
    count_gold(
        [
            [1],
            [2, 3],
            [3, 3, 1],
            [3, 1, 5, 4],
            [3, 1, 3, 1, 3],
            [2, 2, 2, 2, 2, 2],
            [5, 6, 4, 5, 6, 4, 3],
        ]
    )
)

# These "asserts" are used for self-checking
assert (
    count_gold(
        [
            [1],
            [2, 3],
            [3, 3, 1],
            [3, 1, 5, 4],
            [3, 1, 3, 1, 3],
            [2, 2, 2, 2, 2, 2],
            [5, 6, 4, 5, 6, 4, 3],
        ]
    )
    == 23
)
assert (
    count_gold(
        [
            [1],
            [2, 1],
            [1, 2, 1],
            [1, 2, 1, 1],
            [1, 2, 1, 1, 1],
            [1, 2, 1, 1, 1, 1],
            [1, 2, 1, 1, 1, 1, 9],
        ]
    )
    == 15
)