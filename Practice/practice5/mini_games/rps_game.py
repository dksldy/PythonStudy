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
    r = ["가위","바위","보"]
    w = [("가위","보"),("바위","가위"),("보","바위")]
    while True:
        u3 = input("가위, 바위, 보 입력 (end 누르면 종료) : ")
        if u3 == 'end':
            print("종료합니다.")
            break
        if u3 in r:
            p3 = random.choice(r)
            print(f"유저 : {u3}\t 컴퓨터 : {p3}")
            
            if u3 == p3:
                print(f"유저 : {u3} 컴퓨터 : {p3} 결과 : 비김")
            elif (u3,p3) in w:
                print(f"유저 : {u3} 컴퓨터 : {p3} 결과 : 유저 승")
            else:
                print(f"유저 : {u3} 컴퓨터 : {p3} 결과 : 유저 패")
      

         