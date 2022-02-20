print('task 1')
a = 13
b = 435
c = 876
print('a = ' + str(a) + ' b = ' + str(b) + ' c = ' + str(c))
a = int(input('vvedite novoe znachenie peremennoj a'))
b = int(input('vvedite novoe znachenie peremennoj b'))
c = int(input('vvedite novoe znachenie peremennoj c'))
print('rezult: ' + str(a) + ' ' + str(b) + ' ' + str(c))

print('task 2')
a = int(input('vvedite kolichestvo sec'))
sec = a % (24 * 3600)
hours = sec // 3600
sec %= 3600
mins = sec // 60
sec %= 60
print(str(hours) + ':' + str(mins) + ':' + str(sec))

print('task 3')
a = int(input("VVedite znachenije peremennoj n"))
n1 = str(a)
n2 = n1 + n1
n3 = n1 + n1 + n1
b = a + int(n2) + int(n3)
print b

#print('task 4')
#a = int(input('Vvedite poloshitelnoe chislo'))
#while a > 10:
#    a / 10
#    while a >

print('task 5')
viruch = int(input('Vvedite kolichestvo viruchki'))
izderch = int(input('Vvedite kolichestvo izderchek'))
answer = 'a'
if viruch > izderch:
    answer = 'Y vas pribyl!'
    print(answer)
else:
    answer = 'Y vas ybitok...'
    print(answer)
if answer == 'Y vas pribyl!':
    u = (viruch - izderch)//viruch
    print('rentabelnost viruchki = ' + str(u))
    p = int(input('vvedite kolichestvo sotrudnikov'))
    print('dohod na odnogo sotrudnika: ' + str(u//p))






