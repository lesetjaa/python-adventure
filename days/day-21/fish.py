from animal import Animal


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def swim(self):
        print("moving in water")


nemo = Fish()
print(nemo.num_of_eyes)
