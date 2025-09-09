# 문자열

# 문자열 데이터 표현 : " ", ' '
s1 = "하늘색"
s2 = 'sky blue'

print(s1,s2)

# 삼중 따옴표 (""" """) (''' ''')
s3 = ''' 
오늘 점심은
맛있었다.
그래서 배부르다.
'''
print(s3)
# => 여러행을 포함한 데이터를 표현할때 사용

# 이스케이프 문자
s4 = "Hello\nWorld\nPython"
print(s4)

# 형식 지정
name = '정상수'
age = 50

s5 = f"내 이름 {name} 나이 {age} 반말하지마라"
print(s5)

# 문자열 반복
# *Java 문자열.repeat(반복횟수)
s6 = "happy"
print(s6*5)
print("===="*20)

# 문자열 인덱싱 -> 인덱스로 처리
print("s6[0] : ", s6[0])    # s6 변수에 저장된 문자열의 첫번째 글자 'h'
print("s6[-1] : ", s6[-1])  # s6 변수에 저장된 문자열의 끝에서 첫번째 글자 'y'

# 슬라이싱 -> 인덱스로 부분 추출
print("s6[0:4] : ", s6[0:4])    # s6 문자열의 0번 인덱스부터 3번 인덱스까지

print()

# 문자열 관련 메소드
print("길이 : ", len(s6))
print("대문자로 변환 : ", s6.upper()) # *Java 문자열.toUpperCase()
print("소문자로 변환 : ", s6.lower()) # *Java 문자열.toLowerCase()
print("값을 변경 : ", s6.replace('pp', 'xx'))
print("값을 찾기 : ", s6.find('y'))     # *Java 문자열.indexof(찾을값)