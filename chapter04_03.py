#파이썬 while

#while <expr>:
#    <statement(s)>

#예제 1
n = 5
while n > 0:
    print(n)
    n -= 1

#예제 2
a = ["lemon", "apple", "cherry"]

while a:
    print(a.pop())

#if 중첩
#예제 3
#break, continue

n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print("Loop ended")

#예제 4
m = 5
while m > 0:
    m -= 1
    if m == 2:
        continue
    print(m)
print("Loop ended")
print()

#예제 5
i = 1

while i <= 10:
    print("i : ", i)
    if i == 6:
        break
    i += 1

#while-else
#예제 6
    
n = 10
while n > 0:
    n -= 1
    print(n)
else:
    print("else out")
print()

#예제 7
a = ["apple", "banana", "dragonfruit", "peach"]
s = "bear"

i = 0
while i < len(a):
    if a[i] == s:
        break
    i += 1
else :
    print(s, "not found in list")

print()

#무한반복
#while True:
#   print("hello")
    
#예제 8
while True:
    if not a:
        break
    print(a.pop())