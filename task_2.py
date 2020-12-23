sec_1 = int(input('Введите секунды: '))
hour = sec_1 // 3600
minuts = (sec_1 // 60) % 60
sec_2 = sec_1 % 60
if minuts < 10:
    minuts = ('0' + str(minuts))
else:
    minuts = minuts
if sec_2 < 10:
    sec_2 = ('0' + str(sec_2))
else:
    sec_2 = sec_2
print(str(hour) + ':' + str(minuts) + ':' + str(sec_2))