import abc


class Set(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def getSize(self):
        pass

    @abc.abstractmethod
    def isEmpty(self):
        pass

    @abc.abstractmethod
    def contains(self, e):
        pass

    @abc.abstractmethod
    def add(self, e):
        pass

    @abc.abstractmethod
    def remove(self, e):
        pass


class Map(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def getSize(self):
        pass

    @abc.abstractmethod
    def isEmpty(self):
        pass

    @abc.abstractmethod
    def contains(self, key):
        pass

    @abc.abstractmethod
    def add(self, key, value):
        pass

    @abc.abstractmethod
    def remove(self, key):
        pass

    @abc.abstractmethod
    def get(self, key):
        pass

    @abc.abstractmethod
    def set(self, key, newvalue):
        pass
