#파이썬 문자형

#문자열 생성
str1 = "Hello"
str2 = "Python"
str3 = """Good day"""
str4 = '''Good night'''

print(len(str1), len(str2), len(str3), len(str4))

#빈 문자열
str5 = ''
str6 = str()

print(type(str5), len(str5))
print(type(str6), len(str6))

#이스케이프 문자
"""
\n : 개행
\t : 탭
\\ : \문자
\' : ' 문자
\" : " 문자
\000 : 널 문자
"""

print("I'm a girl")
print('I\'m a girl')
print("a \t b")
print("a \"\" b")
print()

#Raw String
raw_s1 = r'D:\python\test'
print(raw_s1)
print()

#멀티라인 입력
multi_str = \
""" 
String
Multi line
Test
"""
print(multi_str)
print()

#문자열 연산
str_o1 = "python"
str_o2 = "apple"
str_o3 = "How are you doing"
str_o4 = "Seoul London Paris NewYork"

print(str_o1 * 3)
print(str_o1 + str_o2)
print('y' in str_o1)
print('k' in str_o1)
print('k' not in str_o1)

#문자열 형 변환
print(str(66), type(str(66)))
print()

#문자열 함수(upper, isalnum, startswith, count, endswith, isalpha)
print("Capitalize : ", str_o1.capitalize())
print("endswith? : ", str_o2.endswith("s"))
print("replace : ", str_o1.replace("thon", "good"))
print("sorted : ", sorted(str_o1))
print("split : ", str_o4.split(" "))
print("count : ", str_o4.count("a"))

#반복(시퀀스)
im_str = "Good Boy!"
# print(dir(im_str))

for i in im_str :
    print(i)
print()

#슬라이싱
str_sl = "Nice Python"

print(str_sl[0:3])
print(str_sl[5:])
print(str_sl[:len(str_sl)])
print(str_sl[1:9:2])
print(str_sl[::2])
print(str_sl[-5:])
print(str_sl[1:-2])
print(str_sl[::-1])
print()

#아스키 코드
a = "z"
print(ord('a'))
print(chr(122))