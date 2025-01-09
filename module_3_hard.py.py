def calculate_structure_sum(data):
    total = 0

    if isinstance(data, int):
        return data

    elif isinstance(data, str):
        return len(data)

    elif isinstance(data, dict):
        for key in data.keys():
            total += calculate_structure_sum(key)

        for value in data.values():
            total += calculate_structure_sum(value)

    else:
        try:
            for item in data:
                total += calculate_structure_sum(item)
        except TypeError:
            pass

    return total


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)