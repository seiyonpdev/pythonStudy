#파이썬 예외처리

#예외 종류
#SyntaxError : 문법이 틀렸을 경우
#TypeError : 서로 계산할 수 없는 자료형을 계산했을 때
#NameError : 없는 변수를 참조할 때
#IndexError : 존재하지 않는 인덱스를 참조할 경우
#ValueError
#KeyError

#문법적으로는 예외가 없지만 코드 실행 단계에서 발생하는 예외도 중요
#1. 예외는 반드시 처리
#2.로그는 반드시 남긴다
#3.예외는 던져진다
#4.예외 무시

#SyntaxError : 문법 오류
#print('error)
#print('error'))

#NameError : 참조 없음
#a, b = 10, 15
#print(c)

#ZeroDivisionError
#print(100 / 0)

#IndexError
# x = [50, 60, 70]
# print(x[1])
# print(x[4])

#KeyError : 없는 키를 사용할 때
# dic = {"name" : "Lee", "age" : 10, "city" : "Boston"}
# print(dic['hobby'])

 #AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용 예외
# import time
# print(time.time2())

#ValueError : 시퀀스 자료형 안에서 없는 자료를 참조하려 할 때 
# x = [10, 20, 30]
# x.remove(40)

#FileNotFoundError : 없는 파일을 열려고 할 때
#f = open('test.txt')

#TypeError : 자료형에 맞지 않는 연산을 수행 할 경우
# x = [1, 2]
# y = (1, 2)
# z = 'test'
# print(x + y)
# print(y + z)
# print(x + z)

#예외 처리 기본
#try : 예외가 발생 할 가능성이 있는 코드 실행
#except 예외명1 : 여러개 가능
#except 예외명2 :
#else : try 블록에 예외가 없을 경우 실행
#finally : 항상 마지막에 실행

name = ["Lee", "Kim", "Park"]

#예제 1
# try:
#     z = 'Kim' #Cho
#     x = name.index(z)
#     print("{} Found it! {} in name".format(z, x + 1))
# except ValueError:
#     print("Not found it! - Occurred ValueError")
# else:
#     print("OK! else")

# print()

#예제 2
# try:
#     z = 'Kim' #Cho
#     x = name.index(z)
#     print("{} Found it! {} in name".format(z, x + 1))
# except Exception:
#     print("Not found it! - Occurred ValueError")
# else:
#     print("OK! else")

# print()

#예제 3
try:
    z = 'Cho'
    x = name.index(z)
    print("{} Found it! {} in name".format(z, x + 1))
except Exception as e:
    print(e)
    print("Not found it! - Occurred ValueError")
else:
    print("OK! else")
finally:
    print("OK! finally")
print()

#예제 4
#예외 발생 : raise
#raise 키워드로 예외 직접 발생
try:
    a = "Park"
    if a == "Kim":
        print("OK! pass")
    else:
        raise ValueError
except ValueError:
    print("Occurred! Exception!")
else :
    print("OK! else")