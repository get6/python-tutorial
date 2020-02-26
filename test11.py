class MyClass:
    pass


class Rectangle:
    count = 0  # 클래스 변수

    # 초기자(initializer)
    def __init__(self, width, height):
        # self.* : 인스턴스변수
        self.width = width
        self.height = height
        Rectangle.count += 1

        # private 변수 __area
        self.__area = width * height

    # 인스턴스 메서드
    def calcArea(self):
        area = self.width * self.height
        return area

    # 정적 메서드
    @staticmethod
    def isSquare(rectWidth, rectHeight):
        return rectWidth == rectHeight

    # 클래스 메서드
    @classmethod
    def printCount(cls):
        print(cls.count)

    def __add__(self, other):
        obj = Rectangle(self.width + other.width, self.height + other.height)
        return obj

    def __internalRun(self):
        pass


# 테스트
square = Rectangle.isSquare(5, 5)
print(square)
rect1 = Rectangle(5, 5)
rect2 = Rectangle(2, 5)
print(rect1.calcArea())
rect1.printCount()
print(Rectangle.count)
r3 = rect1 + rect2
print(r3.calcArea())
print("width = ", r3.width)
r3.width = 10
print("width = ", r3.width)
print(Rectangle.count)
r3.count = 5
print(r3.count)
r4 = Rectangle(10, 10)
print(r3.count)
print(Rectangle.count)

Rectangle.count = 50
r4.count = 10  # count 인스턴스 변수가 새로 생성됨

print(r4.count, Rectangle.count)
# print(r4.__dict__)
# print(Rectangle.__dict__)


class Animal:
    def __init__(self, name):
        self.name = name

    def move(self):
        print("move")

    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        print("bark")


# class Duck(Animal, Dog): 에러 발생 Cannot create a consistent method resolution order (MRO) for bases Animal, Dog
# class Duck(Dog, Animal): 에러 발생 안함
class Duck(Animal):
    def speak(self):
        print("quack")


dog = Dog("doggy")
n = dog.name
dog.move()
dog.speak()

animals = [Dog("tofu"), Duck("duck")]
for a in animals:
    a.speak()


class Base1:
    pass


class Base2:
    pass


class MultiDerived(Base1, Base2):
    pass


# 예외처리까지 봤다~!
