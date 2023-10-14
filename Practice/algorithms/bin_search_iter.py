def bin_search(L, element):
    i = 0
    low = 0
    high = len(L)
    while low < high:
        index = high // 2
        med = L[index]
        if element == med:
            return i + index
        if element > med:
            i += index
            L = L[index:]
        if element < med:
            L = L[:index]
        high = len(L)



L = [x + 5 for x in range(1, 200, 6)]
print(L)
element = int(input())
res_index = bin_search(L, element)

print(res_index == L.index(element), res_index)
