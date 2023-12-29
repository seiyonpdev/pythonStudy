#파이썬 딕셔너리
#범용적으로 가장 많이 사용
#순서 X, 키 중복 X, 수정 O, 삭제 O

# 선언
a = {
    'name' : 'Park',
    'age' : '26',
    'birth' : '000101'
}
b = {0 : "hello python"}
c = {'arr' : [1, 2, 3, 4]}
e = dict([
    ('Name', 'Goodgirl'),
    ('City', 'Rome'),
    ('Age', 26)
])
f = dict(
    Name = 'Goodboy',
    City = 'Berlin',
    Age = 26
)

print('a : ', type(a), a)
print('b : ', type(b), b)
print('c : ', type(c), c)
print('e : ', type(e), e)
print('f : ', type(f), f)

#출력
print('a.name : ', a['name']) #키가 없으면 에러 발생
print('a.name : ', a.get('name1')) # 키가 없으면 None으로 처리

#추가
a['addr'] = '로마시 로마동 로마구'
print('a : ', a)
a['rank'] = [1, 2, 3]
print('a : ', a)

#len 키의 갯수
print(len(a))
print(len(b))
print(len(c))
print(len(e))
print(len(f))

#함수
#주로 반복문에서 사용
print('a : ', a.keys())
print('b : ', b.keys())
print('c : ', c.keys())
print('e : ', e.keys())
print('f : ', f.keys())

print()

print('a : ', a.values())
print('b : ', b.values())
print('c : ', c.values())
print('e : ', e.values())
print('f : ', f.values())

print()

print('a : ', a.items())
print('b : ', b.items())
print('c : ', c.items())
print('e : ', e.items())
print('f : ', f.items())

print()

print('a : ', a.pop('name'))
print('a : ', a)

print()

print('f : ', f.popitem()) #랜덤하게 팝
print('f : ', f)

print()

print('a : ', 'birth' in a)
print('a : ', 'City' in a)

#수정
a['age'] = 101
print('a : ', a)
a.update(age = 55)
print('a : ', a)

print()

temp = {
    'addr' : 'Busan'
}
a.update(temp)
print('a : ', a)