def bigger_price(limit: int, data: list[dict]) -> list[dict]:
    """
    TOP most expensive goods
    """
    
    sort_list_price = list(sorted(map(lambda x: (x['price'], x['name']) ,data )))
    sort_list_price = dict(sort_list_price[::-1]) 
    res = {v:k for k, v in sort_list_price.items()}
    d = []
    for key, val in res.items():
        d.append({'name':key, 'price': val})
    return d[:limit]
print("Example:")
print(
    bigger_price(
        2,
        [
            {"name": "bread", "price": 100},
            {"name": "wine", "price": 138},
            {"name": "meat", "price": 15},
            {"name": "water", "price": 1},
        ],
    )
)
print(bigger_price(
    2,
    [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1},
    ],
))# == [{"name": "wine", "price": 138}, {"name": "bread", "price": 100}]
print(bigger_price(
    1, [{"name": "pen", "price": 5}, {"name": "whiteboard", "price": 170}]
))# == [{"name": "whiteboard", "price": 170}]

print("The mission is done! Click 'Check Solution' to earn rewards!")
