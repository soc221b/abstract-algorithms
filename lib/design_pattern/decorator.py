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
1. Be careful if you want to override __getattr__ method to decorator class.
2. If you want to explicitly call class the decorated's function or else,
   then you can call it from 'decorated_class' property indirectly.
"""


class Decorator():

    def __init__(self, decorated_class):
        self.__decorated_class = decorated_class

    @property
    def decorated_class(self):
        return self.__decorated_class

    def __getattr__(self, name):
        return getattr(self.__decorated_class, name)
