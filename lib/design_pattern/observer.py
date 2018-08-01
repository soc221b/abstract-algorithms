"""
How to use observer:

1. Decorate your observed-class with the ObserverDecorator class,
   which observe some notifier.

2. Implement the update member-function in your the observed-class
   which will be passed only one parameter: event and no return.

3. Decorate your notified-class with the NotifierDecorator class,
   which notify each observer you registered.


example:

    class Phone():
        def __init__(self, name):
            self.__name = name

        def update(self, event):
            if event == "Earthquake warning":
                print("{0} need(s) to run away.".format(self.__name))

    class App():
        def __init__(self, name):
            self.__name = name

        def update(self, event):
            if event == "It will rain":
                print("{0} alert: you need to buy an umbrella.".format(
                    self.__name))

    class EmergencyCenter():
        pass

    class WeatherCenter():
        pass

    def main():
        # Add observer to center object
        emergency_center = NotifierDecorator(EmergencyCenter())
        my_phone = Phone("Lily")
        sam_s_phone = Phone("Sam")

        emergency_center.attach_observer(ObserverDecorator(my_phone))
        emergency_center.attach_observer(ObserverDecorator(sam_s_phone))

        emergency_center.notify("Earthquake warning")

        # or you could attach notifier via decorator itself
        weather_center = NotifierDecorator(WeatherCenter())
        built_in_weather_app = ObserverDecorator(App("Built-in weather app"))
        third_party_weather_app = ObserverDecorator(App("Another weather app"))

        built_in_weather_app.attach_notifier(weather_center)
        third_party_weather_app.attach_notifier(weather_center)

        weather_center.notify("It will rain")

    ### OUTPUT
    Lily need(s) to run away.
    Sam need(s) to run away.
    Built-in weather app alert: you need to buy an umbrella.
    Another weather app alert: you need to buy an umbrella.

note:
1. you can attach a notifier to an observer by itself
   or attach an observer to a notifier.
"""
from lib.design_pattern import Decorator


class ObserverDecorator(Decorator):
    def __init__(self, base):
        super().__init__(base)
        self._notifiers = {}

    def attach_notifier(self, notifier):
        """
        notifier: NotifierDecorator-liked instance
        """
        self._notifiers[notifier] = notifier.attach_observer(self)

    def detach_notifier(self, notifier):
        """
        notifier: NotifierDecorator-liked instance
        """
        notifier.detach_observer(self._notifiers[notifier])
        del self._notifiers[notifier]

    # class which be decorted needs to impelment this function
    def update(self, event):
        """
        event: object
        """
        return self.decorated_class.update(event)


class NotifierDecorator(Decorator):

    def __init__(self, base):
        super().__init__(base)
        self._observers = {}

    def attach_observer(self, observer):
        """
        observer: ObserverDecorator-liked instance
        return: int
                identify the observer
        """
        identifier = len(self._observers)
        self._observers[identifier] = observer
        return identifier

    def detach_observer(self, identifier):
        """
        identifier: int
                    which is returned by attach_observer member-function
        """
        del self._observers[identifier]

    def notify(self, event):
        """
        event: object
        """
        for observer in self._observers.values():
            observer.update(event)
