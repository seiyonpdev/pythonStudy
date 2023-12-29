#집합 특징
#순서 X, 중복 X, 수정 O, 삭제 O

#선언
a = set()
b = set([1, 2, 3, 4])
c = set([1, 5, 6, 7])
d = set([1, 2, 'Pen', 'Cap', 'Plate'])
e = {'dog', 'cat', 'hamster', 'bird'}
f = {42, 'lizard', (1, 2, 3), 3.14}

print(2 in b)

#셋을 튜플로, 셋을 리스트로 변환 가능

#len으로 길이를 가져올 수 있다

#집합 자료형 활용
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print('s1 & s2 : ', s1 & s2)
print('s1 & s2 : ', s1.intersection(s2))

print('s1 | s2 : ', s1 | s2)
print('s1 | s2 : ', s1.union(s2))

print('s1 - s2 : ', s1 - s2)
print('s1 - s2 : ', s1.difference(s2))

#중복 원소 확인, 있으면 false 없으면 true
print('s1 & s2 : ', s1.isdisjoint(s2))

#부분 집합 확인
print('subset : ', s1.issubset(s2))
print('superset : ',s1.issuperset(s2))

#추가 & 제거
s1 = set([1, 2, 3, 4])
s1.add(5)
print('s1 : ', s1)

s1.remove(2) #없는 값을 지우려 하면 에러
print('s1 : ', s1)

s1.discard(3) #없는 값을 지우려 해도 에러 X
print('s1 : ', s1)

s1.clear()
print('s1 : ', s1)

