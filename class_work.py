class Bird:
    def __init__(self):
        self.flying = True

    def birdsong(self):
        print("새소리")


class Sparrow(Bird):
    def birdsong(self):
        print("짹짹")

class swalow(Bird):
    def birdsong(self):
        print("무음")
    
    
my_pet = Sparrow()
my_pet2 = swalow()

print(my_pet.flying)
my_pet.birdsong()
my_pet2.birdsong()