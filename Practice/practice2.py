# practice2.py

# 1. 연도를 입력 받아 윤년인지 아닌지 출력
'''
    * 윤년 판별 기준
      - 연도가 4의 배수이면 윤년
        이때, 100의 배수이면 윤년이 아님
        하지만, 400의 배수이면 윤년

                    4의 배수     100의 배수     400의 배수      윤년 여부
      ex) 2020  =>     O           X             X              O
          1900  =>     O           O             X              X
          2000  =>     O           O             O              O
          2023  =>     X           X             X              X
'''
'''
y = int(input("연도를 입력하세요 : "))
if y % 4 == 0:
    pass
    if y % 100 == 0:
        if y % 400 == 0:
            print(f"{y}년 은 윤년입니다.")
        else:
            print(f"{y}년 은 평년입니다.")
    else:
        print(f"{y}년 은 윤년입니다.")
else:
    print(f"{y}년은 평년입니다.")
'''
'''
if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
    print("윤년입니다.")
else:
    print("평년입니다.")
''' 
# 2. 1 ~ 100 까지의 3의 배수 합 출력
'''
b = 0
sum = 0
for b in range(1, 101):
    if b % 3 == 0:
        sum += b
print(f"1부터 100까지 값 중 3의 배수 총 합 : {sum}")
'''
# 3. 구구단 출력 (2단 ~ 9단)
'''  **** 출력 형식 ****
    2 x 1 = 2   3 x 1 = 3   4 x 1 = 4   ...  9 x 1 = 9
    2 x 2 = 4   3 x 2 = 6   4 x 2 = 8   ...  9 x 2 = 18
    2 x 3 = 6   3 x 3 = 9   4 x 3 = 12   ...  9 x 3 = 27
    ...
    2 x 9 = 18   3 x 9 = 27   4 x 9 = 36   ...  9 x 9 = 81
'''
'''
w = 2
q = 1
while w <= 9 and q <= 9:
    print(w, 'x', q, '=' ,(w*q), end ="  ")
    w += 1
'''
'''
for i in range(2,10):
    for j in range(1,10):
        print(f"{i} * {j} = {i*j}")
    print()

for j in range(1, 10):      # 곱해지는값
    for i in range(2, 10):  # 단
        print(f"{i} * {j} = {i*j}", end="\t ")
    print()
'''
# 4. 문자열을 입력 받아 길이가 5 이상이면 "길어요" 출력. 그렇지 않으면 입력된 값 출력
'''
s = input("문자열을 입력하세요 : ")
if len(s) >= 5:
    print("길어요.")
else:
    print(s)
'''
# 5. 1 ~ 31까지 숫자를 모두 출력하되, 값에 3 또는 6 또는 9가 포함된 경우 "짝👏" 출력
num = [3,6,9]
for i in range(1, 32):
    if i < 10:
        if i in num:
            print("👏",end=" ")
        else:
            print(i, end=" ")
    else:
        if i % 10 in num or\
        i // 10 in num:
            print("👏", end=" ")
        else:
            print(i, end=" ")