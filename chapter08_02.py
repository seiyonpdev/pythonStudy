#파이썬 외장함수
#종류 : sys, pickle, shutil, temfile, time, random

#예제1
import sys
print(sys.argv)

#예제2
#강제종료
#sys.exit()

#예제3
#파이썬 패키지 위치
print(sys.path)

#예제4
#pickle : 객체 파일 쓰기
import pickle
f = open("test.obj", "wb")
obj = {1 : "python", 2 : "study", 3 : "basic"}
pickle.dump(obj, f)
f.close()

#예제5
#pickle : 객체 파일 읽기
f = open("test.obj", "rb")
data = pickle.load(f)
print(data, type(data))
f.close()

#예제6
#os : 환경 변수, 디렉토리 처리 관련, 운영체제 작업 관련
#mkdir, rmdir(비어있으면 삭제), rename, 

import os
print(os.environ)
print(os.environ["USERNAME"])

#예제7
#현재 경로
print(os.getcwd())

#예제8
#time : 시간 관련 처리
import time
print(time.time())

#예제9 (형태 변환)
print(time.localtime(time.time()))

#예제10 (간단 표현)
print(time.ctime())

#예제11 (형식 표현)
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))

#예제12 (시간 간격 발생)
# for i in range(5):
#     print(i)
#     time.sleep(1)

#예제13
#random : 난수 리턴
import random

#0~1 사이의 실수
print(random.random()) 

#예제14
print(random.randint(1, 45))
print(random.randrange(1, 45))

#예제15 (섞기)
d = [1, 2, 3, 4, 5]
random.shuffle(d)
print(d)

#예제16 (무작위 선택)
c = random.choice(d)
print(c)

#예제17
#webbrowser : 본인 OS의 웹 브라우저 실행
import webbrowser
webbrowser.open("https://www.naver.com/")
webbrowser.open_new("https://www.naver.com/")