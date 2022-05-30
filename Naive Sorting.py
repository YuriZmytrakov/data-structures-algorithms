def NaiveSort_modified(dic_A):
    n = len(dic_A)
    keys = list(dic_A.keys())
    # print(keys)
    val = list(dic_A.values())
    # print(val)

    for i in range(n-1):
        for j in range(0, n-i-1):
            if val[j] < val[j+1]:
                #val[j], val[j+1] = val[j+1], val[j]
                keys[j], keys[j+1] = keys[j+1], keys[j]
    return keys


dic_A = {1.1: 3, 2.2: 4, 3.3: -5, 4.4: -6}
print('The original dictionary:', dic_A)
print('sorted_keys', NaiveSort_modified(dic_A))
print('\n')
dic_A = {'a': 3, 'b': 4, 'c': -5, 'd': -6}
print('The original dictionary:', dic_A)
print('sorted_keys', NaiveSort_modified(dic_A))
