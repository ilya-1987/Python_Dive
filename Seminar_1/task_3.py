#Вывеcти в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.

for i in [[2,3,4,5],[6,7,8,9]]:
    print('')
    for j in range(1,11):
        print ('%d x %d = %d\t' % (i[0], j, i[0]*j),
               '%d x %d = %d\t' % (i[1], j, i[1]*j),
               '%d x %d = %d\t' % (i[2], j, i[2]*j),
               '%d x %d = %d\t' % (i[3], j, i[3]*j))