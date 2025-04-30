class Minecraft:
    def hello_creeper(self):
        print("Hello, Creeper!")

class Roblox(Minecraft):
    def hello_all(self):
        super().hello_creeper()
        print("Hello, Pozzy!")

hello = Roblox()
hello.hello_all()
