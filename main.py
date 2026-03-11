class Bird:
    def __init__(self, name):
        self.name = name
        

    def move(self):
        self.position += 3
       
 
class Pigeon(Bird):
    def move(self):
        self.position += 4

class Hawk(Bird):
    def move(self):
        self.position += 10

boncuk = Bird("Boncuk")
doner = Pigeon("Döner Kuş")
hawk_eye = Hawk("Hawk Eye")

print(boncuk.position)
boncuk.move()
print(boncuk.position)

print("------")

print(doner.position)
doner.move()
print(doner.position)

print("------")
