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

        def update(self, event):
            if event == "earthquake warning":
                print("I need to run away.")


    class App():

        def update(self, event):
            if event == "it will rain":
                print("I need to buy an umbrella.")


    class EmergencyCenter():
        pass


    class WeatherCenter():
        pass


    def main():
        emergency_center = NotifierDecorator(EmergencyCenter())
        weather_center = NotifierDecorator(WeatherCenter())
        my_phone = ObserverDecorator(Phone())
        my_home_weather_app = ObserverDecorator(App())

        emergency_center.attach_observer(my_phone)
        my_home_weather_app.attach_notifier(weather_center)

        emergency_center.notify("earthquake warning")
        weather_center.notify("it will rain")

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
