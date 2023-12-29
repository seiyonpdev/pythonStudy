#print 사용법

#기본 출력
print('hello world')
print("hello python")
print('''python Starts''')
print("""finally!!""")

#개행
print()

#seperator 옵션
print('p', 'y', 't', 'h', 'o', 'n', sep='|')
print('010', '7777', '1234', sep='-')
print('aaa', 'naver.com', sep='@')
print()

#end 옵션
print('Welcome to', end=' ')
print('my home', end='!')
print()

#file 옵션
import sys
print('Learn Python', file=sys.stdout)
print()

#format 사용(d : 3, s : 'python' , f : 3.14)
print('%s %s' % ('one', 'two'))
print('{} {}'.format('one', 2) )
print('{1} {0}'.format('one', 'two'))

#%s
print('%10s' % ('nice'))
print('{:>10}'.format('nice'))

print('%-10s' % ('nice'))
print('{:10}'.format('nice'))

print('{:_>10}'.format('nice'))
print('{:^10}'.format('nice'))

print('%.5s' % ('nice'))
print('%.5s' % ('pythonstudy'))
print('%5s' % ('pythonstudy'))
print('{:>10.5}'.format('pythonstudy'))
print()

# %d
print('%d %d' % (1, 2))
print('{} {}'.format(1, 2))

print('%4d' % (42))
print('{:4d}'.format(42))
print()

# %f
print( '%f' % (3.1434343434))
print('{:f}'.format(3.1434343434))
print('{:1.4f}'.format(3.1434343434))

print('%06.2f' % (3.1434343434))
print('{:06.2f}'.format(3.1434343434))
print()

#3가지 format practice
x = 50
y = 100
text = 1234567
n = 'Park'

#출력 1
ex1 = 'n = %s, s = %s, sum=%d' % (n, text, (x + y))
print(ex1)

#출력 2
ex2 = 'n = {n}, s = {s}, sum={sum}'.format(n=n, s=text, sum=x+y)
print(ex2)

#출력 3
ex3 = f'n = {n}, s = {text}, sum={x + y}'
print(ex3)
print()

#구분기호
m = 100000000

print(f'm : {m:,}')
print()

#정렬
# ^ : 가운데, < : 왼쪽, > : 오른쪽
t = 20
print(f't : {t:10}')
print(f't center : {t:^10}')
print(f't left : {t:<10}')
print(f't right : {t:>10}')
print()

print(f't center : {t:*^10}')