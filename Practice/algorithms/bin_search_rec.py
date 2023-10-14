def bin_search(L, element):
    index = len(L) // 2
    med = L[index]
    i = 0
    if element == med:
        return i + index
    if element > med:
        i = bin_search(L[index:], element) + index
    if element < med:
        i = bin_search(L[:index], element)
    return i


L = [x * 2 for x in range(1, 1001, 8)]
print(L)

element = int(input())
index = bin_search(L, element)
print(index == L.index(element), index)
