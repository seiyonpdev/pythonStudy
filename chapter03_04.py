#파이썬 튜플
#리스트와 비교 중요
#불변
#순서 O, 중복 O, 수정 X, 삭제X

#선언
a = ()
b = (1, ) #괄호는 생략 가능
c = (11, 12, 13, 14)
d = (100, 1000, 'Heart', 'Spade', 'Club')
e = (100, 1000, ('Heart', 'Spade', 'Club'))

#인덱싱
print("d : ", d[1])
print("d : ", d[0] + d[1] + d[1])
print("d : ", d[-1])
print("e : ", e[-1])
print("e : ", e[-1][1])
print("e : ", list(e[-1][1]))
print()

#수정 x
# d[0] = 1500
# print(d[0])

#슬라이싱
print('d : ', d[0:3])
print('d : ', d[2:])
print('d : ', e[2][1:3])
print()

#튜플 연산
print("c + d = ", c + d)
print("c * 3 = ", c * 3)
print()

#튜플 함수
a = (5, 2, 3, 1, 4)
print("a : ", a)
print("a : ", a.index(3))
print("count : ", a.count(2))
print()

#팩킹 & 언팩킹
#팩킹
t = ('dog', 'cat', 'frog', 'bear')
print(t)
print(t[0])
print(t[-1])

#언팩킹
(x1, x2, x3, x4) = t

print(type(x1), type(x2), type(x3), type(x4))
print(x1, x2, x3, x4)