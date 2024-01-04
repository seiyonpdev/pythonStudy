#행맨 미니게임 제작
#프로그램 완성 및 최종 테스트

import time
import csv
import random
import winsound

#처음 인사
name = input("What is your name?")

print("Hi, " + name, "Time to play hangman game!")

print()
time.sleep(1)

print("Start Loading...")
print()
time.sleep(0.5)

#CSV 단어 리스트
words = []

#문제 CSV 파일 로드
with open('./resource/word_list.csv', 'r') as f:
    reader = csv.reader(f)
    #Header skip
    next(reader)
    for c in reader:
        words.append(c)

#리스트 섞기
random.shuffle(words)

#단어 뽑기
q = random.choice(words)

#정답 단어
word = q[0].strip()

#추측 단어
guesses = ''

#기회
turns = 10

#핵심 while loop
#찬스 카운트가 남아있을 경우
while turns > 0:
    #실패 횟수
    failed = 0
    #정답 단어 반복
    for char in word:
        if char in guesses:
            #추측 단어 출력
            print(char, end=' ')
        else:
            #틀린 경우 대시로 처리
            print("_", end=' ')
            failed += 1
    #단어 추측이 성공한 경우
    if failed == 0:
        print()
        print()
        #성공 사운드
        winsound.PlaySound('./sound/good.wav', winsound.SND_FILENAME)
        print('Congratulations!')
        break
    print('Hint : {}'.format(q[1].strip()))

    #추측 단어 문자 단위 입력
    guess = input("guess a character : ")
    #단어 더하기
    guesses += guess
    
    if guess not in word:
        #기회 횟수 감소
        turns -= 1
        #오류 메시지
        print('Oops! Wrong')
        #남은 기회 출력
        print('You have', turns, 'more guesses!')
        if turns == 0:
            #실패 메시지
            winsound.PlaySound('./sound/bad.wav', winsound.SND_FILENAME)
            print('Game over!')