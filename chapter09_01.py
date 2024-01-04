#파이썬 파일 입출력

#읽기모드 : r, 쓰기모드 w, 추가모드 a, 텍스트모드 t, 바이너리 모드 b
#텍스트모드가 기본값
#상대경로 : .. (상위 폴더로) .(현재 폴더), 절대경로("주소값")

#예제1
#파일 읽기

f = open("./resource/it_news.txt", "r", encoding='UTF-8')

#속성 확인
print(dir(f))
#인코딩 확인
print(f.encoding)
#파일 이름
print(f.name)
#모드 확인
print(f.mode)

cts = f.read()
print(cts)
f.close()

#예제2
#with문 활용
#close를 알아서 해준다

with open("./resource/it_news.txt", "r", encoding='UTF-8') as f:
    c = f.read()
    print(c)
    print(iter(c))
    print(list(c))

print()

#예제3
#read() : 전체 읽기, read(10) : 10byte만 읽기
with open("./resource/it_news.txt", "r", encoding='UTF-8') as f:
    c = f.read(20)
    print(c)
    c = f.read(20)
    print(c)
    f.seek(0, 0)
    c = f.read(20)
    print(c)

print()

#예제4
#readline() : 한줄씩 읽기
with open("./resource/it_news.txt", "r", encoding='UTF-8') as f:
    line = f.readline()
    print(line)

#예제5
#readlines : 전체를 읽은 후 라인 단위로 리스트에 저장
with open("./resource/it_news.txt", "r", encoding='UTF-8') as f:
    cts = f.readlines()
    print(cts)
    print()
    for c in cts:
        print(c, end='')

print()

#파일 쓰기
#예제1
with open('./resource/contents1.txt', 'w') as f:
    f.write('I Love Python\n')

#예제2
with open('./resource/contents1.txt', 'a') as f:
    f.write('I Love Python2\n')

#예제3
#writelines : 리스트를 파일로 쓴다
with open('./resource/contents1.txt', 'w') as f:
    list = ['Apple\n', 'Pear\n', 'Banana\n', "Mango\n"]
    f.writelines(list)

#예제4
with open('./resource/contents1.txt', 'w') as f:
    print('Test Text Write!', file=f)