#파이썬 모듈
#Module : 함수, 변수, 클래스 등 파이썬 구성 요소 등을 모아놓은 파일

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def multi(x, y):
    return x * y

def divide(x, y):
    return x / y

def power(x, y):
    return x ** y

# print("-" * 15)
# print("called! inner!")
# print(add(5, 5))
# print(sub(15, 5))
# print(multi(5, 5))
# print(divide(10, 2))
# print(power(5, 3))
# print("-" * 15)

if __name__ == "__main__":
    print("-" * 15)
    print("called! __main__")
    print(add(5, 5))
    print(sub(15, 5))
    print(multi(5, 5))
    print(divide(10, 2))
    print(power(5, 3))
    print("-" * 15)
