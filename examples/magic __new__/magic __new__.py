class Point:
    def __new__(cls, *args, **kwargs):
        print(f"Вызов __new__ для {cls}")
        return super().__new__(cls)

    def __init__(self, x=0, y=0):
        print(f"Вызов __init__ для {self}")
        self.x = x 
        self.y = y


pt = Point(1, 2)
print(pt)
