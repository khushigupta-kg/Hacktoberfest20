def uniqueOccurrences(arr):
    count = {}
    freq = set()
    for x in arr:
        count[x] = count.get(x, 0) + 1

    for c in count.values():
        if c in freq:
            return False
        freq.add(c)
    return True
