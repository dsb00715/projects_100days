# Inheritance
class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, Exhale.")


class Fish(Animal):
    def __init__(self):
        super().__init__()
        self.tail = True

    def swim(self):
        print("swim in water")

    def breathe(self):
        super().breathe()
        print("doing this under water!")


nemo = Fish()
nemo.breathe()
