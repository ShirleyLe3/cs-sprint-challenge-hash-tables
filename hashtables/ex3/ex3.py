def intersection(arrays):
    inter = {}
    result = []

    for arr in arrays:
        for num in arr:
            if num not in inter:
                inter[num] = 0
            inter[num] += 1
    
    inter_list = list(inter.items())

    for item in inter_list:
        if item[1] == len(arrays):
            result.append(item[0])

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
