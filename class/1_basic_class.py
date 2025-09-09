'''
[클래스 정의]

class 클래스명:
    # 생성자
    def __init__(self, 매개변수):
        # 초기 작업 (초기화)

    # 메소드 (클래스 내의 함수)
    def 메소드명(self, 매개변수):
        # 동작할 내용
'''

# Person 클래스 정의

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print(f"안녕하세요. 저는 {self.name} 입니다.")
        print(f"나이는 {self.age} 살 입니다.")

# Person 객체 생성
p1 = Person("정상수", 50)
p2 = Person("전기충격기", "치지지직")
p3 = Person("안녕", "20안녕")
p1.introduce()
p2.introduce()
p3.introduce()