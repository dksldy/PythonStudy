# 세트 => 자바 Set 구조와 유사
#   특징 => 순서유지 X, 중복허용 X

s = {1, 2, 3, 2}
print(s)            #{ } == set 중복된 데이터는 제거됨

# 데이터 추가
s.add(6)            # add() 데이터 추가
print(s)

s.add(3)            # 내용과 중복된 값은 추가는 안됨
print(s)

# 데이터 삭제
s.discard(2)        # 2 discard 데이터 삭제
print(s)
s.discard(2)        # 없는 데이터를 삭제하고자 할 경우 무시(따로 처리 X)
print(s)
s.remove(3)         # 3 remove 데이터 삭제
print(s)
#s.remove(3)        # 없는 데이터를 삭제하고자 할 경우 KeyError 오류 발생
#print(s)

# 집합 연산
s2 = {1, 2, 3}
s3 = {3, 4, 5}
print("합집합 : ", s2 | s3, s2.union(s3))
print("교집합 : ", s2 & s3, s2.intersection(s3))
print("차집합 : ", s2 - s3, s2.difference(s3))

# 데이터 접근(조회)
for item in s2:
    print(item)