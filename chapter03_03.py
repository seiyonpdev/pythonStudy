#파이썬 리스트

a = []
b = list()
c = [70, 75, 80, 85]
d = [5, 12.1, 'Ace', 'Queen', 'Jack']
e = [1000, 10000, ['Ace', 'Queen', 'Jack']]
f = [21.42, 'football', 3, 4, False, 3.141592]

#인덱싱
print()
print('d : ', type(d), d)
print("d[1] : ", d[1])
print("d : ", d[0] + d[1] + d[1])
print("d: ", d[-1])
print("e : ", e[-1][1])
print()

#슬라이싱
print("d : ", d[0:3])
print("d : ", d[2:])
print("e : ", e[-1][1:3])
print()

#리스트 연산
print("c + d = ", c + d)
print("c * 3 = ", c * 3) 
print('Test' + str(c[0]))
print()

#값 비교
print(c == c[:3] + c[3:])
print(c)
print(c[:3] + c[3:])
print()

#Identity(id)
temp = c
print(temp, c)
print(id(temp))
print(id(c))
print()

#리스트 수정, 삭제
c[0] = 4
print("c : ", c)
c[1:2] = ['a', 'b', 'c'] #[['a', 'b', 'c']]
print("c : ", c)
c[1] : ['a', 'b', 'c']
print("c : ", c)
c[1:3] = [] #삭제
print("c : ", c)
del c[2] #삭제
print("c : ", c)
print()

#리스트 함수
a = [5, 2, 3, 1, 4]
print("a : ", a)
a.append(10)
print("a : ", a)
a.sort()
print("a : ", a)
a.reverse()
print("a : ", a)
print(a.index(3), a[3])
a.insert(2, 7) #인덱스 2 자리에 7을 넣고 뒤의 원소들을 뒤로 밀어버린다
print("a : ", a)
a.remove(10)
print("a : ", a)
print("a : ", a.pop())
print("a : ", a)
a.extend([8, 9])
print("a : ", a)

#삭제 : remove, pop, del