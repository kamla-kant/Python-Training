"""
 This is calculator project
 """


class MyCalculator:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b


if __name__ == "__main__":
    m = MyCalculator()
    r1 = m.add(10, 20)
    print("r1 : ", r1)
    r2 = m.sub(10, 20)
    print("r2 : ", r2)

