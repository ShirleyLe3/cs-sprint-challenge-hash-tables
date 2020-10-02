def has_negatives(a):
    result = []
    d = {}
    
    for num in a:
        if num not in result:
            d[num] = True
    for num in a:
        if num > 0 and num * -1 in d:
            result.append(num)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
