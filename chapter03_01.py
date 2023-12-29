#파이썬 지원 자료형
"""
int : 정수
float : 실수
complex : 복소수
bool : 불린
str : 문자형 (시퀀스)
list : 리스트 (시퀀스)
tuple : 튜플 (시퀀스)
set : 집합
dict : 사전
"""

#데이터 타입
str1 = 'Python'
str2 = 'Java'
bool = True
float_v = 10.0
int_v = 7
list = [str1, str2]
dict = {
    "name" : "Mr.Buttons",
    "color" : "yellow tabby" 
}
tuple = (3, 4, 5)
set = {7, 8, 9}

#데이터 타입 출력
print(type(str1))
print(type(str2))
print(type(bool))
print(type(float))
print(type(int))
print(type(list))
print(type(dict))
print(type(tuple))
print(type(set))

#숫자형 연산자
"""
+
-
*
/
// : 몫
% : 나머지
abs(x) : 절대값
pow(x, y) : x의 y제곱
x ** y 도 pow(x, y)와 같은 의미
"""

#정수 출력
i = 77
i2 = -14
big_int = 777777777777777777777779999999999999

print(i)
print(i2)
print(big_int)
print()

#실수 출력
f = 0.9999
f2 = 3.141592
f3 = -3.9
f4 = 3 / 9

print(f)
print(f2)
print(f3)
print(f4)
print()

#연산
i1 = 39
i2 = 339
big_int1 = 33333333333333333334444444444455555
big_int2 = 99999999999999998888888888777777777
f1 = 1.234
f2 = 3.929

# +
print(">>>>>+")
print("i1 + i2 = ", i1 + i2)
print("f1 + f2 = ", f1 + f2)
print("big_int1 + big_int2 = ", big_int1 + big_int2)
print()

# *
print(">>>>>*")
print("i1 * i2 = ", i1 * i2)
print("f1 * f2 = ", f1 * f2)
print("big_int1 * big_int2 = ", big_int1 * big_int2)
print()

#형 변환
a = 3.
b = 6
c = .7
d = 12.7

print(type(a), type(b), type(c), type(d))

print(float(b))
print(int(c))
print(int(d))
print(int(True))
print(float(False))
print(complex(3))
print(complex('3'))
print(complex(False))
print()

#수치 연산 함수
print(abs(-7))
x, y = divmod(100, 8)
print(x, y)
print(pow(5, 3), 5 ** 3)
print()

#외부 모듈
import math

print(math.pi)
print(math.ceil(5.1))
print()


