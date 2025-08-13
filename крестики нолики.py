a = '''1 | 2 | 3
➖ ➖  ➖
4 | 5 | 6
➖ ➖  ➖
7 | 8 | 9'''
def pr(n):
  f = ({1, 2, 3}, {1, 5, 9}, {3, 6, 9}, {4, 5, 6}, {7, 8, 9}, {1, 4, 7}, {5, 2, 8}, {3, 5, 7})
  n = set(n)
  if [i for i in f if len(i & n)==3]:
    return True
  else:
      return False
x = list()
y = list()
c = 0
d = list()
c1 = 8
print(a)
b = int(input('ход крестиков: '))
while c1!=0:
  if c ==0:
    x.append(b)
  if b not in d:
    if c%2==0:
      if b==1:
        e = list(a)
        e.pop(e.index('1') + 1)
        u = ''
        for i in e:
          u += i
        a = u
        a = a.replace('1', '❌')
        print(a)
      if b==2:
        e = list(a)
        e.pop(e.index('2') - 1)
        u = ''
        for i in e:
          u += i
        a = u
        a = a.replace('2', '❌')
        print(a)
      if b==3:
        e = list(a)
        e.pop(e.index('3') - 1)
        u = ''
        for i in e:
          u += i
        a = u
        a = a.replace('3', '❌')
        print(a)
      if b==4:
        e = list(a)
        e.pop(e.index('4') + 1)
        u = ''
        for i in e:
          u += i
        a = u
        a = a.replace('4', '❌')
        print(a)
      if b==5:
        e = list(a)
        e.pop(e.index('5') - 1)
        u = ''
        for i in e:
          u += i
        a = u
        a = a.replace('5', '❌')
        print(a)
      if b==6:
        e = list(a)
        e.pop(e.index('6') - 1)
        u = ''
        for i in e:
          u += i
        a = u
        a = a.replace('6', '❌')
        print(a)
      if b==7:
        e = list(a)
        e.pop(e.index('7') + 1)
        u = ''
        for i in e:
          u += i
        a = u
        a = a.replace('7', '❌')
        print(a)
      if b==8:
        e = list(a)
        e.pop(e.index('8') - 1)
        u = ''
        for i in e:
          u += i
        a = u
        a = a.replace('8', '❌')
        print(a)
      if b==9:
        e = list(a)
        e.pop(e.index('9') - 1)
        u = ''
        for i in e:
          u += i
        a = u
        a = a.replace('9', '❌')
        print(a)
      if c>0:
        x.append(b)
      d.append(b)
      if pr(x)==True:
        print('Выиграли крестики')
        break
      b = int(input('ход ноликов: '))
    else:
      if b == 1:
        e = list(a)
        e.pop(e.index('1') + 1)
        u = ''
        for i in e:
          u += i
        a = u
        a = a.replace('1', '⭕')
        print(a)
      if b == 2:
        e = list(a)
        e.pop(e.index('2') - 1)
        u = ''
        for i in e:
          u += i
        a = u
        a = a.replace('2', '⭕')
        print(a)
      if b == 3:
        e = list(a)
        e.pop(e.index('3') - 1)
        u = ''
        for i in e:
          u += i
        a = u
        a = a.replace('3', '⭕')
        print(a)
      if b == 4:
        e = list(a)
        e.pop(e.index('4') + 1)
        u = ''
        for i in e:
          u += i
        a = u
        a = a.replace('4', '⭕')
        print(a)
      if b == 5:
        e = list(a)
        e.pop(e.index('5') - 1)
        u = ''
        for i in e:
          u += i
        a = u
        a = a.replace('5', '⭕')
        print(a)
      if b == 6:
        e = list(a)
        e.pop(e.index('6') - 1)
        u = ''
        for i in e:
          u += i
        a = u
        a = a.replace('6', '⭕')
        print(a)
      if b == 7:
        e = list(a)
        e.pop(e.index('7') + 1)
        u = ''
        for i in e:
          u += i
        a = u
        a = a.replace('7', '⭕')
        print(a)
      if b == 8:
        e = list(a)
        e.pop(e.index('8') - 1)
        u = ''
        for i in e:
          u += i
        a = u
        a = a.replace('8', '⭕')
        print(a)
      if b == 9:
        e = list(a)
        e.pop(e.index('9') - 1)
        u = ''
        for i in e:
          u += i
        a = u
        a = a.replace('9', '⭕')
        print(a)
      d.append(b)
      y.append(b)
      if pr(y)==True:
        print('Выиграли нолики')
        break
      b = int(input('ход крестиков: '))
  else:
    print(a)
    print('сюда уже ходили!')
    c -=1
    b = int(input('думай лучше: '))
    c1 +=1
  c +=1
  c1 -=1
if c==8:
    print(a)
    print('Ничья!')