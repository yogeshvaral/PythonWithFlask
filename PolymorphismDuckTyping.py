class Pycharm:
    def execute(self):
        print("compiling")
        print("Running")


class Eclipse:
    def execute(self):
        print("Checking")
        print("verifying")
        print("compiling")
        print("running")


class Laptop:

    def code(self,ide):
        ide.execute()


ide = Pycharm()
ide1 = Eclipse()
lap1 = Laptop()
lap1.code(ide)
lap1.code(ide1)
""" This lap1.code will accept and work properly with any type of object until it has the execute method.
THIs is called is Duck Typing.Any Bird which has even single feature of duck can be duck"""
