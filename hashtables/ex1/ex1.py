def get_indices_of_item_weights(weights, length, limit):
    storage = {}

    for i, w in enumerate(weights):
        if w in storage.keys():
            storage[w].append(i)
        else:
            storage[w] = [i]

    for key in storage:
        # only one item with a given weight
        if len(storage[key]) == 1:
            # if we find a complimentary weight
            if limit - key in storage.keys():
                # determine return order by index size
                if storage[key] > storage[limit - key]:
                    return (storage[key][0], storage[limit - key][0])
                else:
                    return (storage[limit - key][0], storage[key][0])
        # two items with the same weight given
        else:
            if limit / key == 2:
                # determine return order by index size
                if storage[key][0] > storage[key][1]:
                    return (storage[key][0], storage[key][1])
                else:
                    return (storage[key][1], storage[key][0])

    return None
