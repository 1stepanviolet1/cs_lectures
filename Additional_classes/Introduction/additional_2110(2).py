input_srt = 'username1@email.com:10121020;user_name_undefined:01010101010;' \
            'goodusrnm@mail.mail:818392103;sampleemail@mmm.ru:344946590;student@etu.ru:55796485441;' \
            'example@gmail.ru:165456936;example@gmail.ru:130;example@gmail.ru:100030'

L = input_srt.split(';')

# for i in range(K):  # 0, 1, 2, ...., K-1 ==> start=0; step=1
# for i in range(10, K):  # 10, 11, 12, ...., K-1 ==> step=1
# for i in range(10, K, 5):  # 10, 15, 20, ...., K-5
# for i in range(start, stop, step):  # start+step*0, start+step*1, start+step*2, start+step*3,  ...., stop-step

for i in range(len(L)):
    print(i, L[i])

for item in enumerate(L):
    print(item[0], item[1])

for ind, elem in enumerate(L):
    print(ind, elem)
