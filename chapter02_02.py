#파이썬 변수

#기본 선언
n = 700

#출력
print(n)
print(type( n))
print()

#동시 선언
x = y = z = 500
print(x, y, z)
print()

#재선언
var = 75
var = "Change Value"
print(var)
print(type(var))
print()

# Object References
# 변수 값 할당 상태
# 1. 타입에 맞는 오브젝트 생성
# 2. 값 생성
# 3. 콘솔에 출력

n = 777
m = n

print(m, n)

m = 555
print(m, n)
print()

#id(identity) 확인 : 객체의 고유값 확인
m = 800
n = 655

print(id(m))
print(id(n))
print(id(m) == id(n))
print()

#같은 오브젝트 참조
m = 800
n = 800

print(id(m))
print(id(n))
print(id(m) == id(n))
print()

