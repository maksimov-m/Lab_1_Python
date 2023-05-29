
class node:
    def __int__(self, number, count):
        self.number = number
        self.mass = []
        for i in range(count):
            if i != number:
                self.mass.append((abs(number - i), i))


class Graph:
    def __init__(self, count):
        self.gr
