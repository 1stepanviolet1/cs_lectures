flag = True
k = 0

while flag:
    print('k =', k)
    k += 1
    if k == 3:
        print('k == 3, continue')
        continue
    if k == 6:
        print('k == 6, break')
        break
    print('end iter')
else:
    print('else')

print('-'*80, end='\n\n')
k = 0

while flag:
    k += 1
    print('k =', k)
    if k == 5:
        print('k == 5, continue')
        flag = False
        continue
    print('end iter')
else:
    print('else')