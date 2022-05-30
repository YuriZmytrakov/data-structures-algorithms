def Orders(array, start, end):
    if len(start) < 1:
        array.append(end)
        return array
    else:
        n = len(start)
        i = 0
        while i <= n-1:
            next_end = end + start[i:i+1]
            next_start = start[:i] + start[i+1:]
            i += 1
            Orders(array, next_start, next_end)
    return array


all = (Orders([], ['1', '2', '3'], []))
print(all)

n1 = range(1, 5, 1)
n2 = range(1, 9, 1)
n3 = range(1, 17, 1)

print('n = 4 ->', len(Orders([], list(n1), [])))
print('n = 8 ->', len(Orders([], list(n2), [])))
