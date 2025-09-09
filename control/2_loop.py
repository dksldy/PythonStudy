# 반복문
'''
    * 기본구조
        # 반복 가능 객체 : 리스트, 문자열, 튜플, 세트, 딕셔너리, range
        for 변수명 in 반복가능객체:
            반복할내용
    * range 함수
        range(stop) : 0 부터 stop -1 까지 1씩 증가하는 숫자들을 생성 (시퀀스)
        range(start, stop) : start 부터 stop -1 까지 증가하는 시퀀스 생성
        range(start, stop, step) : start 부터 stop -1 까지 step 씩 증가 시퀀스 생성

'''
"""
# * 1 ~ 10 까지 출력
for i in range(1, 11):
    print(i, end = " ")
print()

# * 리스트에 저장되어 있는 요소들을 출력
colors = ["red", "skyblue", "blue", "black"]
for c in colors:
    print(c, end = " ")
print()

# while 문
'''
    * 기본구조

        while 조건식:
            반복할내용
'''
# * while 문 을 사용하여 1 ~ 10 출력
n = 1
while n <= 10:
    print(n, end = " ")
    # n++   # SyntaxError 오류
    # n = n + 1
    n += 1
print()

# * while 문 을 사용하여 
#       사용자 입력이 exit인 경우 종료
#           그렇지 않으면 입력값 출력
while True:
    data = input("단어 입력하세요 (exit 을 입력할경우 종료) : ")

    if data == 'exit':  # 파이썬에서는 문자열의 값 비교 가능
        print("프로그램 종료")
        break
    print(f"입력된값 : {data}")
"""

# * up and down game
# 1 ~ 100 사이의 숫자 맞추기 게임
'''
    ex) 정답 = 55
        사용자 : 20 up!
        사용자 : 60 down!
        사용자 : 55 정답!
'''
'''
import random
print("*===== Up & Down =====")
# o = int(random.random()*100+1)
o = random.randint(1,100)
while True:
    ex = int(input("숫자를 입력하세요 : "))
    if ex > o:
        print(ex, "Down")
    elif ex < o:
        print(ex, "Up")
    elif ex == o:
        print(o, "정답!")
        break
    else:
        print()
'''
'''
import random
x = int(input("랜덤 시작값 입력 : "))
y = int(input("랜덤 마지막값 입력 : "))
r = random.randint(x, y)
while True:
    #u = int(input("입력 : "))
    u = input("입력 : ")
    # isdigit() : 값이 정수로 되어있는지 아닌지 판별
    if not u.isdigit():
        print("숫자만 입력해주세요. ")
        continue
    u = int(u)
    if u == r:
        print(r, "정답!")
        break
    elif u > r:
        print(u, "Down..")
    else:   # u < r 
        print(u, "Up!!")
'''

#-----------------------------------------------------------
# * 가위바위보 ----> 삼세판!
import random
rsp = ["가위", "바위", "보"]
win_case = [("가위","보"), ("바위", "가위"), ("보", "바위")]
'''
for i in range(1,4):
    print(f"round {i}")
'''
s = 1
i = 1
r = 1
while i < 4 and s < 4:
    print(f"======= {r} Round =======")
    r += 1
    user = input("가위, 바위, 보 중 하나만 선택 : ")
    if user in rsp:
        computer = random.choice(rsp)

        print(f"사용자 : {user} \t 컴퓨터 : {computer}")
    
        if user == computer:
            print("비김")
        elif (user, computer) in win_case:
            print("이김")
            i += 1
            if i > 3:
                print("사용자 승리!")
        else:
            print("패배")
            s += 1
            if s > 3:
                print("컴퓨터 승리!")
    else:
        ("잘못입력하셨습니다.")