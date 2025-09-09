# 딕셔너리 => Map 과 유사
#   특징 => 키-밸류 한쌍으로 관리, 키값은 중복허용X

user = {"name":"정상수","age":50,"phone":"123-1234-1234"}
print(user)

print("사용자 이름 : ", user["name"])
print("나이 : ", user.get("age"))

# 데이터 추가
user["hobby"] = "비보잉하기"
print(user)

print("키값들만 조회 : ", user.keys())
print("밸류값들만 조회 : ", user.values())

# 데이터 삭제
user.pop("phone")
print(user)