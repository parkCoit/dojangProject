# problem
class AdvancedList(list):
    def replace(self, old, new):
        while old in self :
            self[self.index(old)] = new

# problem2
class Animal:
    def eat(self):
        print('먹다')
class Wing:
    def flap(self):
        print('파닥거리다')
class Bird(Animal, Wing):
    def fly(self):
        print('날다')








if __name__ == '__main__':
    x = AdvancedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    x.replace(1, 100)
    print(x)

    b = Bird()
    b.eat()
    b.flap()
    b.fly()
    print(issubclass(Bird, Animal))
    print(issubclass(Bird, Wing))