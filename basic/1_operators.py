# 연산자

''' 산술 연산자
# n1 = 15; n2 = 4
# => 한줄에 변수를 여러개 선언할 경우 세미콜론(;) 으로 구분 '''
n1 = 15
n2 = 4
print("산술연산자 ====")
print("n1 + n2 = ", n1 + n2)
print("n1 - n2 = ", n1 - n2)
print("n1 * n2 = ", n1 * n2)

print("n1 / n2 = ", n1 / n2)        # 실수 나누기
print("n1 // n2 = ", n1 // n2)      # 정수 나누기
print("n1 % n2 = ", n1 % n2)        # 나머지

print("n1 ** n2 = ", n1 ** n2)      # 제곱

print() # 줄바꿈

# 큰수 표현 : en표현
print(5 * 10 ** 13) # 5 x 10^13
print(5e13)

print(5e16)   # 5e+16

print()

# 비교 연산자 -> 자바와 동일
print("비교연산자 ====")
print("n1 == n2 ? ", n1 == n2)
print("n1 != n2 ? ", n1 != n2)
print("n1 < n2 ? ", n1 < n2)
print("n1 > n2 ? ", n1 > n2)
print("n1 <= n2 ? ", n1 <= n2)
print("n1 >= n2 ? ", n1 >= n2)
print()

# 논리연산자 => adn or not
x = True
y = False
print("논리연산자 ====")
print("x and y ? ", x and y)
print("x or y ? ", x or y)
print("not x ? ", not x)
print("not y ? ", not y)