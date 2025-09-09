# 상속 : 부모 클래스의 속성, 메소드들을 새로 정의하지 않고 사용할수 있는 기술, 방법

# Animal 클래스 정의
class Animal:
    def eat(self):
        print("간식을 먹습니다.")
    
    def speak(self):
        print("소리를 냅니다.")
    
# Dog 클래스 정의
class Dog(Animal):      # => 부모클래스 상속 (eat, speak 부모클래스에 있기때문)
    '''
    def speak(self):
        print("멍멍")
    def eat(self):
        print("간식을 먹습니다.")
    '''
    def speak(self):        # 오버라이딩(재정의)
        print("멍멍")
    def eat(self):
        print("깐식깐식")
    def play_ball(self):
        print("공을 가지고 놀기")

# Dog 클래스 생성
d = Dog()
d.play_ball()
d.eat(), d.speak(),