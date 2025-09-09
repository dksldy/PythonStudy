# 다형성
# : 같은 이름의 메소드지만, 객체에 따라 다른 동작을 수행하는 성질
#   상속 관계에서 많이 활용된다.

# Animal 클래스 정의
class Animal:
    def sound(self):
        print("소리를 냅니다.")

# Cat 클래스 정의
class Cat(Animal):
    def sound(self):
        print("야옹~")

# Cow 클래스 정의
class Cow(Animal):
    def sound(self):
        print("음머~")

# 동물 리스트
animals = [Cat(), Cow(), Animal()]  # [고양이, 소, 동물]

for a in animals:
    a.sound()