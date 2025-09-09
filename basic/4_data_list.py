# 리스트 -> 배열 / ArrayList
# 특징 => 중복허용, 순서 유지, 가변(수정가능)

fruits = ["apple", "melon", "딸기", "복숭아", "바나나"]

# 인덱싱
print("첫번째 과일 : ", fruits[0])
print("마지막 과일 : ", fruits[-1]) # 리스트 끝에서부터 접근

# 슬라이싱
print("두번째, 세번째 과일 : ", fruits[1:3])    # 1, 2 인덱스로 접근

# 리스트에 데이터를 추가
fruits.append("무화과")           # append 끝에 추가 
print(fruits)

fruits.insert(3, "블랙베리")      # insert n, 추가할 내용 => 인덱스 지정 내용 추가
print(fruits)

fruits.extend(["두리안","수박"])   # extend 또 다른 리스트 데이터를 끝에 추가
print(fruits)

# 데이터 삭제 : remove, pop
fruits.pop()            # pop 리스트 끝의 데이터를 삭제
print(fruits)
item = fruits.pop()     # pop대입 리스트 끝의 데이터를 삭제 -> 해당 값을 리턴
print(fruits)
print(item)

fruits.remove("무화과") # remove 데이터를 지정하여 삭제
print(fruits)

print("====="*10)

# 정렬

# 오름차순 정렬
nums = [5, 3, 9, 1]
nums.sort()             # sort 오름차순 정렬
print(nums)             #[1, 3, 5, 9]
# 내림차순 정렬
nums.reverse()          # reverse 역순으로 재배치, 내림차순 정렬
print(nums)             #[9, 5, 3, 1]

nums = [5, 3, 9, 1]
nums.sort(reverse=True) # sort 메소드에 reverse 옵션 추가
print(nums)             # (오름차순 정령) -> (역순 내림차순 정렬)

words = ["apple", "banana", "cat"]
words.sort(key=len)      # 데이터 길이를 기준으로 정렬
print(words)

words.sort(key=len, reverse=True)
print(words)