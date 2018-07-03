"""
How to use observer:

1. Inherit the Decorate class from your decorator class
2. Call the Decorate class's init function in your decorator class's __init__
   and pass which object will be decorated to it.


example:

    class RealWorldDecorator(Decorator):

        def __init__(self, base):
            super().__init__(base)

note:
1. be careful if you want to override __getattr__ method to decorator class.
"""


class Decorator():

    def __init__(self, base):
        self.__base = base

    def __getattr__(self, name):
        return getattr(self.__base, name)
