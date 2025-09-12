'''
[main.py]
- 사용자에게 게임 선택 메뉴 표시
- 선택한 게임 모듈의 함수를 실행
- 0 입력 시 종료
- 잘못된 입력 처리
'''
from mini_games import play_dice_game, play_number_game, play_rps_game

while True:
    print("1. 주사위 게임")
    print("2. 숫자맞추기 게임")
    print("3. 가위바위보 게임")
    print("4. 게임종료.")
    
    m = int(input("메뉴를 선택하세요 : "))

    if m == 1:
        print("다이스 게임에 입장합니다.")
        play_dice_game()
    elif m == 2:
        print("넘버게임에 입장합니다.")
        play_number_game()
    elif m == 3:
        print("가위바위보 게임에 입장합니다. ")    
        play_rps_game()
    elif m == 4:
        print("종료됩니다.")
        break
    else:
        print("다시 입력해주세요.")
    

