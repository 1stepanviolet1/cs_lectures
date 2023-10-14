input_srt = 'username1@email.com:10121020;user_name_undefined:01010101010;' \
            'goodusrnm@mail.mail:818392103;sampleemail@mmm.ru:344946590;student@etu.ru:55796485441;' \
            'example@gmail.ru:165456936;example@gmail.ru:130;example@gmail.ru:100030'

pairs = input_srt.split(';')

for item in pairs:  # for i in range(K)
    log, pwd = item.split(':')
    print(log, pwd)
    if len(pwd) > 7:
        print('len > 7')
        continue
    elif pwd.count('0') > 3:
        print('amount of 0 = ', pwd.count('0'))
        break
    elif pwd.startswith('1') and pwd.endswith('0'):  # {}
        print('yes!')
    else:
        print('no!')

print('The end!')

