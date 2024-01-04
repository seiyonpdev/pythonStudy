#파이썬 내장(Built-in) 함수

#절대값
#abs()

print(abs(-3))

#all : iterable요소를 검사해서 모두 true일 때 true 반환
print(all([1, 2, 3]))
print(all([1, 2, 0]))

#any : iterable요소를 검사해서 하나라도 true일 때 true 반환
print(any([1, 2, 0]))
print(any([0, 0, 0]))

#chr : 아스키 코드를 문자로
#ord : 문자를 아스키코드로
print(chr(67))
print(ord("C"))

#enumerate : 인덱스 + Iterable 객체 생성
for i, name in enumerate(['a', 'b', 'c']):
    print(i, name)

#filter : 반복가능한 객체 요소를 지정한 함수 조건에 맞는 값 추출

def conv_pos(x):
    return abs(x) > 2

print(list(filter(conv_pos, [1, -3, 2, 0, -5, 6])))
print(list(filter(lambda x: abs(x) > 2, [1, -3, 2, 0, -5, 6])))

#id : 객체의 주소값 반환
print(id(int(5)))
print(id(4))

#len : 요소의 길이 반환
print(len('abcdefg'))
print(len([1, 2, 3, 4, 5, 6, 7, 8, 9]))

#max, min : 최대값 최소값
print(max([1, 2, 3]))
print(max('pythonstudy'))

print(min([1, 2, 3]))
print(min('pythonstudy'))

#map : 반복가능한 객체 요소를 지정한 함수 실행 후 추출 
def conv_abs(x):
    return abs(x)

print(list(map(conv_abs, [1, -3, 2, 0, -5, 6])))
print(list(map(lambda x : abs(x), [1, -3, 2, 0, -5, 6])))

#pow : 제곱값 반환
print(pow(2, 10))

#range : 반복 가능한 객체(iterable) 반환
print(range(1, 10, 2))
print(list(range(1, 10, 2)))
print(list(range(0, -15, -1)))

#round : 반올림
print(round(8.5781, 2))
print(round(5.6))

#sorted : 반복가능한 객체(iterable)을 정렬
print(sorted([6,7,4,3,1,2]))

#sum : 반복가능한 객체의 합 반환
print(sum([6, 7, 8, 9, 10]))
print(sum(range(1, 101)))

#type : 자료형 확인
print(type(3))
print(type({}))
print(type(()))
print(type([]))

#zip : 반복가능한 객체의 요소를 묶어서 반환
print(list(zip([10, 20, 30], [40, 50, 60])))