'''
2. 가위바위보 게임
   - rps_game.py 모듈
   - 함수명: play_rps_game()
   - 기능:
       * 사용자 입력: "가위", "바위", "보"
       * 컴퓨터 랜덤 선택
       * 결과 출력 (이김, 짐, 비김)
'''
import random

def play_rps_game():
    
    u = input("가위, 바위, 보 입력 : ")
    p = random.choice["가위", "바위", "보"]
    
    if u == p:
        print(f"유저 : {u} 컴퓨터 : {p} 결과 : 비김")
        if u == "가위" and p[1]:
            print(f"유저 : {u} 컴퓨터 : {p} 결과 : 유저 패")
        else:
            print(f"유저 : {u} 컴퓨터 : {p} 결과 : 유저 승")
    
