class ComputedProperty:
    _setter_allowed = False

    def __init__(self, prop: object, func: callable, attr_names: tuple[str]):
        self.prop = prop
        self.func = func
        self.attr_names = attr_names

    def __get__(self, instance, owner):
        if not instance:
            return self.prop
        
        value = [getattr(instance, attr, None) for attr in self.attr_names]
        if hasattr(instance, "_cache") and instance._cache[self.attr_names]["value"] == value:
            return instance._cache[self.attr_names]["result"]
        else:
            result = self.func(instance)
            instance._cache = {self.attr_names: {"value": value, "result": result}}
            return result

    def __set__(self, instance, value):
        if not self._setter_allowed:
            raise AttributeError
        getattr(self, f"set_{self.attr_names[0]}")(instance, value)

    def setter(self, value):
        setattr(self, f"set_{self.attr_names[0]}", value)
        self._setter_allowed = True
        return self


class computed_property:

    def __init__(self, *attr_names: str) -> None:
        self.attr_names = attr_names

    def __call__(self, func, *args, **kwargs):
        return ComputedProperty(self, func, self.attr_names)

    def __get__(self, instance, owner):
        return getattr(instance, self.attr_names[0])


if __name__ == '__main__':
    class MyClass:
        def __init__(self, value1, value2):
            self._value1 = value1
            self._value2 = value2

        @computed_property('_value1', '_value2')
        def value(self):
            return self._value1 * self._value2

    obj = MyClass(2, 3)
    print(obj.value)  # prints 6
    obj._value1 = 4
    print(obj.value)  # prints 12
    obj._value1 = 2
    obj._value2 = 4
    print(obj.value)  # prints 8
