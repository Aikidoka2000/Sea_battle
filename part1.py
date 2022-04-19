class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __repr__(self):
        return f"Dot({self.x}, {self.y})"


a = Dot(1, 1)
b = Dot(3, 2)
c = Dot(1, 1)
aa = [Dot(1, 1), Dot(2, 4), Dot(6, 2), Dot(5, 2), Dot(1, 4)]

print(a in aa)
print(a)
print(a == c)
print(a.x == c.x and a.y == c.y) 