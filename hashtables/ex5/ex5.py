# Your code here



def finder(files, queries):
    d = {}
    result = []

    for path in files:
        filename = path.split('/')[-1]
        if filename not in d:
            d[filename] = []
        d[filename].append(path)

    for q in queries:
        if q in d:
            for path in d[q]:
                result.append(path)

    print(result)
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
