def flatten(dictionary: dict[str, str | dict]) -> dict[str, str]:
    res = {}
    def func(next_key,string):
        if not isinstance(next_key, dict):
            res[string] = next_key
        else:
            if next_key == {}:
                res[string] = ""
                return string,""
            for new_dict, val in next_key.items():
                    string += '/' + new_dict
                    func(next_key[new_dict], string)
                    string = string[:-string[::-1].find('/')-1]
    for key in dictionary.keys():
        if isinstance(dictionary[key], dict):
            func(dictionary[key],key)
        else:
            res[key] = dictionary[key]
    return res
    



print("Example:")
print(flatten({"key": "value"}))

# These "asserts" are used for self-checking
print(flatten({"key": "value"}))# == {"key": "value"}
print(flatten({"key": {"deeper": {"more": {"enough": "value"}}}}))# == {"key/deeper/more/enough": "value"}
print(flatten({"empty": {}}))# == {"empty": ""}
print(flatten(
    {
        "name": {"first": "One", "last": "Drone"},
        "job": "scout",
        "recent": {},
        "additional": {"place": {"zone": "1", "cell": "2"}},
    }
) == {
    "name/first": "One",
    "name/last": "Drone",
    "job": "scout",
    "recent": "",
    "additional/place/zone": "1",
    "additional/place/cell": "2",
})

print("The mission is done! Click 'Check Solution' to earn rewards!")