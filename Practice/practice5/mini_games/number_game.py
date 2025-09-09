'''
1. 숫자 맞추기 게임
   - number_game.py 모듈
   - 함수명: play_number_game()
   - 기능:
       * 1~10 사이 랜덤 숫자를 생성
       * 사용자 입력을 받아 숫자를 맞추면 "정답!" 출력
       * 틀리면 "틀렸습니다. 정답은 X였습니다." 출력
'''
import random


def play_number_game():
    while(True):
        r = int(random.randint(1, 10))
        u = int(input("1 ~ 10 사이 숫자를 입력하세요 : "))

        if u == r:
            print(f"{u} 정답!")
        elif u != r:
            print(f"틀렸습니다. 정답은 {r} 였습니다.")
        else:
            ()

play_number_game()