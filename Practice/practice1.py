# practice1.py
'''
    입력함수 => input(출력할 내용) : 입력된값을 리턴
            -> 기본적으로 입력된 값을 문자열 타입으로 리턴

        ex) name = input("이름입력 : ")
'''
# 1. 이름, 성별, 나이, 키 입력받아 출력
#  * 출력 형식 : 이름: xxx, 성별: xx, 나이: xx, 키: xx.xxcm

name = input("이름 입력 : ")
gen = input("성별 입력 : ")
age = input("나이 입력 : ")
hei = input("키 입력 : ")
print(f"이름 : {name}, 성별 :  {gen}, 나이 :  {age}, 키 :  {hei}cm")
print()


# 2. 두 정수 입력받아 합, 차, 곱, 몫, 나머지 계산 후 출력

n1 = int(input("정수 입력 : "))
n2 = int(input("정수 입력 : "))
print(f"{n1} + {n2} = {n1+n2}")
print(f"{n1} - {n2} = {n1-n2}")
print(f"{n1} * {n2} = {n1*n2}")
print(f"{n1} / {n2} = {n1/n2}")
print(f"{n1} // {n2} = {n1//n2}")
print(f"{n1} % {n2} = {n1%n2}")

# 3. 영어 문자열 입력받아 앞 세 글자 출력
str1 = input("영어 문자열 입력 : ")
print("앞 세글자 : ", str1[0:3])

# 4. 실수 2개 입력받아 합, 차, 곱, 나누기 출력
f1 = float(input("실수 입력 : "))
f2 = float(input("실수 입력 : "))
print(f"{f1} + {f2} = {f1+f2}")
print(f"{f1} - {f2} = {f1-f2}")
print(f"{f1} * {f2} = {f1*f2}")
print(f"{f1} / {f2} = {f1/f2}")
print(f"{f1} // {f2} = {f1//f2}")
print(f"{f1} % {f2} = {f1%f2}")

# 5. 두 수 입력받아 제곱과 제곱근 계산
n3 = int(input("숫자1 입력 : "))
n4 = int(input("숫자2 입력 : "))
print(f"{n3} ** 2 = {n3 ** 2}")
print(f"{n3} ** 0.5 = {n3 ** 0.5}")
print(f"{n4} ** 2 = {n4 ** 2}")
print(f"{n4} ** 0,5 = {n4 ** 0.5}")

# 6. 문자열 입력받아 대문자/소문자/글자 수 출력
str2 = input("문자열 입력 : ")
print("대문자 : ", str2.upper())
print("소문자 : ", str2.lower())
print("길이 : ", len(str2))

# 7. 좋아하는 음식 3개 입력받아 리스트처럼 저장 후 출력
foods = []

# foods[food1, food2, food3]
food1 = input("좋아하는 음식1 : ")
food2 = input("좋아하는 음식2 : ")
food3 = input("좋아하는 음식3 : ")
foods.append(food1)
foods.append(food2)
foods.append(food3)

print("좋아하는 음식 리스트:", foods)
print("첫 번째 음식:", foods[0])
print("마지막 음식:", foods[-1])
foods.sort()                  #기본 오름차순 정렬
print("오름차순 정렬 : ", foods)
foods.reverse()   # sort() 후 reverse() 할 경우 내림차순 정렬
foods.sort(reverse=True)      #내림차순 정렬
print("내림차순 정렬 : ", foods)
print()


# 8. 세 개의 숫자 입력받아 합과 평균 계산 후 출력
# 합 => 모두 더하기
# 평규 => 합 / 개수
num1 = int(input("숫자 1 : "))
num2 = int(input("숫자 2 : "))
num3 = int(input("숫자 3 : "))

total = num1 + num2 + num3
print(f"합 : {num1} + {num2} + {num3} = {total}")
print(f"평균 : {total / 3}")
print(f"평균 : {total // 3}")

# 9. 문자열 입력받아 앞 3글자 + 뒤 2글자 합쳐서 출력
data = input("문자열 입력 : ")

print(data[:3] + data[-2:])

# 10. 문자열 입력받아 대문자로 변환 후, 앞 5글자만 출력
str3 = input("문자열 입력 : ")
s1 = str3.upper()
s2 = s1[:5]
print("대문자 변환 : ", s1, "앞 5글자 : ", s2)