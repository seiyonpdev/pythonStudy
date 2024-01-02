#파이썬 반복문

#코딩의 핵심
#for in <collection>
#   <Loop body>

for v1 in range(10):
    print("v1 is : ", v1)
print()

for v2 in range(1, 11):
    print("v2 is : ", v2)
print()

for v3 in range(0, 11, 2):
    print("v3 is : ", v3)

sum = 0
for v4 in range(1, 1001):
    sum += v4
print("1~1000 sum : ",sum)
print()

#Iterables 자료형 반복
#문자열, 리스트, 튜블, 집합, 사전
#iterable 리턴 함수 : range, reversed, enumerate, filter, map, zip

#예제 1
names = ["Kim", "Park", "Cho", "Lee", "Choi", "Yoo"]

for n in names:
    print("You are : ", n)

#예제 2
lotto_numbers = [11, 19, 21, 28, 36, 37]
for n in lotto_numbers:
    print("Current number : ", n)
print()

#예제 3
word = "Beautiful"

for s in word:
    print("word : ", s)
print()

#예제 4
my_info = {
    "name" : "Park",
    "age" : 26,
    "city" : "Seoul"
}

for key in my_info:
    print("val : ", my_info.get(key))

for v in my_info.values():
    print("values : ", v)
print()

#예제 5

name = "LemONadE"

for n in name:
    if n.isupper():
        print(n)
    else:
        print(n.upper())

#break
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for n in numbers:
    if(n == 34):
        print("Found : ", n)
        break
    else:
        print("Not found : ", n)

#continue

lt = ["1", 2, 5, True, 4.3, complex(4)]

for v in lt:
    if type(v) is bool:
        continue
    print("current type : ", v, type(v))

#for - else
#for를 다 돌고 나서 else를 실행한다
#중간에 break나 return을 하면 else는 실행하지 않는다

for num in numbers:
    if num == 24:
        print("Found : 24")
        break
else:
    print("Not found : 24")


#구구단 출력
    
for i in range(2, 10):
    for j in range(1, 10):
        print("{:4d}".format(i * j), end="")
    print()

#변환 예제

username = "Aceman"

print("Reversed : ", reversed(username))
print("List : ", list(reversed(username)))
print("Tuple : ", tuple(reversed(username)))
print("Set : ", set(reversed(username)))