class Observer():
    def __init__(self, decorator=None):
        self._notifiers = {}
        self._decorator = decorator

    def __getattr__(self, name):
        if self._decorator is not None:
            return getattr(self._decorator, name)
        else:
            raise AttributeError

    def attach_notifier(self, notifier):
        self._notifiers[notifier] = notifier.attach_observer(self)

    def detach_notifier(self, notifier):
        notifier.detach_observer(self._notifiers[notifier])
        del self._notifiers[notifier]

    # class which be decorted needs to impelment this function
    def update(self, event):
        return self._decorator.update(event)


class Notifier():

    def __init__(self, decorator=None):
        self._observers = {}
        self._decorator = decorator

    def __getattr__(self, name):
        if self._decorator is not None:
            return getattr(self._decorator, name)
        else:
            raise AttributeError

    def attach_observer(self, observer):
        """
        observer: Observer
        return: int
                identify the observer
        """
        identifier = len(self._observers)
        self._observers[identifier] = observer
        return identifier

    def detach_observer(self, identifier):
        del self._observers[identifier]

    def notify(self, event):
        for observer in self._observers.values():
            observer.update(event)
