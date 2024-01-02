#파이썬 사용자 입력
#Input 사용법
#기본 타입은 str

#예제 1
name = input("Enter Your Name : ")
grade = input("Enter Your Grade : ")
company = input("Enter Your Company name : ")

print(name, grade, company)

#예제 2
number = input("Enter number : ")
name = input("Enter name : ")

print("type of number : ", type(number))
print("type of name : ", type(name))

#예제 3 : 계산
first_num = int(input("Enter num1 : "))
second_num = int(input("Enter num2 : "))
print("num1 + num2 = ", first_num + second_num)

#예제 4
float_num = float(input("Enter a float number : "))
print("input float : ", float_num)
print("input type : ", type(float_num))

#예제 5
print("FirstName : {0}, LastName : {1}".format(input("Enter fist name : "), input("Enter last name : ")))

