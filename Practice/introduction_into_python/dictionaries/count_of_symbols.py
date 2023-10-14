input_str = input()
result = {}

for i in input_str:
    if i in result:
        result[i] += 1
    else:
        result.update({i: 1})

print(result)