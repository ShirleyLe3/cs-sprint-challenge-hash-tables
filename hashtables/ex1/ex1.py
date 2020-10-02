def get_indices_of_item_weights(weights, length, limit):
    result = None
    wd = {}

    for i, item in enumerate(weights):
        if item not in wd:
            wd[item] = []
        wd[item].append(i)

    if length > 1:
        for i, item in enumerate(weights):
            if limit - item in wd:
                if limit - item == item and len(wd[item]) > 1:
                    i = wd[item][0]
                    i2 = wd[item][1]
                else:
                    i2 = wd[limit - item][0]
                result = [max(i, i2), min(i, i2)]
                break

    return result