'''
3. 주사위 게임
   - dice_game.py 모듈
   - 함수명: play_dice_game()
   - 기능:
       * 사용자와 컴퓨터 각각 1~6 사이 랜덤 수 생성
       * 주사위 값 비교 후 결과 출력 (이김, 짐, 비김)
'''
import random

def play_dice_game():
    
    u1 = random.randint(1,6)
    p1 = random.randint(1,6)
    
    if u1 > p1:
        print(f"유저 : {u1} 컴퓨터 : {p1} 결과 : 유저 승")
    elif u1 == p1:
        print(f"유저 : {u1} 컴퓨터 : {p1} 결과 : 비김")
    elif u1 < p1:
        print(f"유저 : {u1} 컴퓨터 : {p1} 결과 : 컴퓨터 승")
