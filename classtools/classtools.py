from collections import UserDict


class NoMethodCollisionDict(UserDict):
    def __setitem__(self, key, value):
        if key in self.data:
            if (callable(value) and not isinstance(value, property)) or isinstance(value, classmethod):
                raise TypeError
        self.data[key] = value


class NoMethodCollisionsMeta(type):
    def __new__(metacls, name, bases, namespace):
        # namespace must return a python internal `dict` and not a custom one
        new_cls = super().__new__(metacls, name, bases, dict(namespace))
        return new_cls

    @classmethod
    def __prepare__(metacls, name, bases):
        return NoMethodCollisionDict()


class NoMethodCollisions(metaclass=NoMethodCollisionsMeta):
    pass
