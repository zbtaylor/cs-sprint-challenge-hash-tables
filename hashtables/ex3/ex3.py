def intersection(arrays):
    num = len(arrays)
    result = []
    storage = {}

    for a in arrays:
        for i in a:
            if i in storage.keys():
                storage[i] += 1
            else:
                storage[i] = 1

    for k in storage:
        if storage[k] == num:
            result.append(k)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
